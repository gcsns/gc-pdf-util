
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import FigureElement, InputFormat, Table
from docling_core.types.doc import ImageRefMode, PictureItem, TableItem
from pathlib import Path

import tempfile
from PIL import Image
import os
import markdown
import pdfkit
import sys
from fastapi import APIRouter, File, Form, UploadFile, HTTPException
from fastapi.responses import FileResponse, Response
import subprocess
import configs

from logger import logger

import base64

import shutil
import zipfile
import fitz  # PyMuPDF
import re
import unicodedata

from pydantic import BaseModel
from typing import List


IMAGE_RESOLUTION_SCALE = 2.0
pipeline_options = PdfPipelineOptions()
pipeline_options.images_scale = IMAGE_RESOLUTION_SCALE
pipeline_options.generate_page_images = True
pipeline_options.generate_picture_images = True

doc_converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
)



# Helper functions to convert a pdf to a set of images and back to a pdf
def convert_pdf_to_images_fitz(pdf_path, dpi= configs.PDF_TO_IMAGE_CONVERSION_DPI):
    """
    Converts each page of a PDF into an image using PyMuPDF (fitz).
    Returns a list of PIL images.
    """
    doc = fitz.open(pdf_path)
    images = []
    
    for page_num in range(len(doc)):
        pix = doc[page_num].get_pixmap(matrix=fitz.Matrix(dpi/72, dpi/72))  # Scale DPI
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append(img)
    
    doc.close()
    return images

def merge_images_into_pdf_fitz(images, output_pdf_path):
    """
    Merges a list of images into a new PDF.
    """
    if not images:
        raise ValueError("No images to merge into a PDF.")
    
    images[0].save(output_pdf_path, save_all=True, append_images=images[1:])
    print(f"Image-based PDF saved: {output_pdf_path}")

def convert_pdf_to_image_pdf_fitz(input_pdf, output_pdf):
    """
    Converts a PDF into an image-based PDF by rendering each page as an image,
    then merging them into a new PDF.
    """
    images = convert_pdf_to_images_fitz(input_pdf)
    merge_images_into_pdf_fitz(images, output_pdf)

# define the structure of a ressponse model that has the page images, picture images, table images, pdf, all as base64 strings
class ResponseModel(BaseModel):
    # page_images: List[str]
    # picture_images: List[str]
    # table_images: List[str]
    images : List[str]
    doc: str
    markDownText: str

# Helper function to detect if text is corrupted or not
def is_text_corrupted(text, threshold = configs.CORRUPTED_TEXT_THRESHOLD):
    """
    Detects if the extracted text is corrupted.
    - Allows Unicode text (Arabic, Chinese, etc.)
    - Flags excessive non-printable characters
    - Detects corruption patterns like '������'
    """
    if not text.strip():
        return True  # Empty text means extraction failed

    total_chars = len(text)
    printable_chars = sum(1 for char in text if unicodedata.category(char)[0] not in ["C"])  # Exclude control characters
    rtl_chars = sum(1 for char in text if "\u0600" <= char <= "\u06FF")  # Arabic Unicode range


    print('percentage:')
    print((total_chars - printable_chars) / total_chars)
    # Check if non-printable characters exceed threshold
    if (total_chars - printable_chars) / total_chars > threshold:
        return True

    # Detect repeated corruption patterns (e.g., '������')
    if re.search(r"�{3,}", text):
        return True

    # If there's a mix of valid text (including Arabic) and not just junk, pass it
    if rtl_chars > 0:  
        return False  # Arabic is detected, so it's fine

    return False


# Helper function to check if the pdf has unicode text
def analyze_pdf(pdf_path):
    """
    Determines if a PDF file has readable text or corrupted text.
    Returns: boolean True if readable, False if corrupted
    """
    doc = fitz.open(pdf_path)
    has_text, has_images, corrupted_text = False, False, False

    for page in doc:
        text = page.get_text("text")
        if text.strip():
            has_text = True
            if is_text_corrupted(text):
                corrupted_text = True

        if len(page.get_images(full=True)) > 0:
            has_images = True

    doc.close()

    # Logic for determining readability:
    if corrupted_text:
        return False  # Corrupted text
    if has_text or has_images:
        return True  # Either readable text or images

    return False  # No readable text or images


def recreatePdfFunc(
    file: UploadFile = File(description="PDF file to be recreated"),
    returnPageImages: bool = False,
    returnPictureImages: bool = True,
    returnTableImages: bool = True
):
    pdf_bytes = file.file.read()

    # create a temp directory
    temp_dir = tempfile.mkdtemp()
    os.makedirs(temp_dir, exist_ok=True)

    logger.info(temp_dir)

    # create a temp file
    original_pdf_file_path = os.path.join(temp_dir, "original.pdf")
    with open(original_pdf_file_path, "wb") as f:
        f.write(pdf_bytes)

    # Checking for corrupted text
    isUncorruptedText = analyze_pdf(original_pdf_file_path)
    logger.debug(f"Is Uncorrupted Text: {isUncorruptedText}")

    if(isUncorruptedText == False):   
        logger.debug("PDF is corrupted, converting to images to retry")     
        workable_pdf_file_path = os.path.join(temp_dir, "workable.pdf")
        convert_pdf_to_image_pdf_fitz(original_pdf_file_path, workable_pdf_file_path)
        logger.debug("PDF converted to images")

    else:
        logger.debug("PDF is not corrupted, skipping conversion to images")     
        workable_pdf_file_path = original_pdf_file_path

    logger.debug('Started parsing PDF')
    conv_res = doc_converter.convert(workable_pdf_file_path)
    doc_filename = conv_res.input.file.stem
    output_dir = Path(temp_dir)

    page_image_names = [] 
    picture_image_names = []
    table_image_names = []

    # Save page images
    for page_no, page in conv_res.document.pages.items():
        page_no = page.page_no
        page_image_filename = output_dir / f"{doc_filename}-{page_no}.png"
        page_image_names.append(page_image_filename)
        with page_image_filename.open("wb") as fp:
            page.image.pil_image.save(fp, format="PNG")

    # Save images of figures and tables
    table_counter = 0
    picture_counter = 0
    for element, _level in conv_res.document.iterate_items():
        if isinstance(element, TableItem):
            table_counter += 1
            element_image_filename = (
                output_dir / f"{doc_filename}-table-{table_counter}.png"
            )
            table_image_names.append(element_image_filename)
            with element_image_filename.open("wb") as fp:
                element.get_image(conv_res.document).save(fp, "PNG")

        if isinstance(element, PictureItem):
            picture_counter += 1
            element_image_filename = (
                output_dir / f"{doc_filename}-picture-{picture_counter}.png"
            )
            picture_image_names.append(element_image_filename)
            with element_image_filename.open("wb") as fp:
                element.get_image(conv_res.document).save(fp, "PNG")

    # read every image from the arrays page_image_names, picture_image_names and table_image_names to base64 strings
    page_image_list = [] 
    picture_image_list = []
    table_image_list = []

    if returnPageImages:
        for page_image_name in page_image_names:
            with open(page_image_name, "rb") as img_file:
                encoded_string = base64.b64encode(img_file.read()).decode("utf-8")
                page_image_list.append(encoded_string)


    if returnPictureImages:
        for picture_image_name in picture_image_names:  
            with open(picture_image_name, "rb") as img_file:
                encoded_string = base64.b64encode(img_file.read()).decode("utf-8")
                picture_image_list.append(encoded_string)


    if returnTableImages:
        for table_image_name in table_image_names:
            with open(table_image_name, "rb") as img_file:
                encoded_string = base64.b64encode(img_file.read()).decode("utf-8")
                table_image_list.append(encoded_string)

    images = page_image_list + picture_image_list + table_image_list

    # create a temp.md file inside the temp directory
    temp_md_path = os.path.join(temp_dir, "markdown-with-images.md")
    temp_md_path = Path(temp_md_path)
    
    # Save markdown with embedded pictures
    conv_res.document.save_as_markdown(temp_md_path, image_mode=ImageRefMode.EMBEDDED)

    # # Save markdown with externally referenced pictures
    # conv_res.document.save_as_markdown(temp_md_path, image_mode=ImageRefMode.REFERENCED)

    logger.debug("=============================================")
    logger.debug("Markdown has been created")
    logger.debug(table_counter)
    logger.debug(picture_counter)
    logger.debug("=============================================")

    temp_md_path = str(temp_md_path)
    with open(temp_md_path, "r") as md_file:
         md_string = md_file.read()
    
    md_string = str(md_string)

    
    temp_final_pdf_path = os.path.join(temp_dir, "document.pdf")

    # tex_file_path = os.path.join(temp_dir, "document.tex")

    # latex_code = configs.MARKDOWN_TO_PDF_GENERATION_TEMPLATE

    # with open(tex_file_path, "w", encoding="utf-8") as tex_file:
    #     tex_file.write(latex_code)

    # try:
    #     # subprocess.run(["pdflatex", "--shell-escape", "-interaction=nonstopmode", "-output-directory", temp_dir, tex_file_path],
    #     #                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    #     subprocess.run(["pdflatex", "--shell-escape", "-output-directory", temp_dir, tex_file_path],
    #                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, cwd=temp_dir)
    # except subprocess.CalledProcessError as e:
    #     return {"error": "pdflatex compilation failed: " + str(e)}
    

    html_content = markdown.markdown(md_string)
    pdfkit.from_string(html_content, temp_final_pdf_path)
    
    with open(temp_final_pdf_path, "rb") as pdf_file:
        pdf_content = pdf_file.read()
    
    # get the pdf_content frorm  the  temp_final_pdf_path file and keep it as a base64 string
    pdf_content = base64.b64encode(pdf_content).decode("utf-8")

    return ResponseModel(
        images = images,
        # page_images=page_image_list,
        # picture_images=picture_image_list,
        # table_images=table_image_list,
        doc=pdf_content,
        markDownText=md_string
    )


    

    # return Response(content=pdf_content, media_type="application/pdf")