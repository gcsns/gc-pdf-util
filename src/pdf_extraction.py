
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import FigureElement, InputFormat, Table
from docling_core.types.doc import ImageRefMode, PictureItem, TableItem
from pathlib import Path

import tempfile
import os
import markdown
import pdfkit
import sys
from fastapi import APIRouter, File, Form, UploadFile, HTTPException
from fastapi.responses import FileResponse, Response
import subprocess
import configs

from logger import logger

IMAGE_RESOLUTION_SCALE = 2.0
pipeline_options = PdfPipelineOptions()
pipeline_options.images_scale = IMAGE_RESOLUTION_SCALE
pipeline_options.generate_page_images = True
pipeline_options.generate_picture_images = True

import base64

import shutil
import zipfile

doc_converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
)
from pydantic import BaseModel
from typing import List



# define the structure of a ressponse model that has the page images, picture images, table images, pdf, all as base64 strings
class ResponseModel(BaseModel):
    # page_images: List[str]
    # picture_images: List[str]
    # table_images: List[str]
    images : List[str]
    doc: str
    markDownText: str


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
    temp_file_path = os.path.join(temp_dir, "temp.pdf")
    with open(temp_file_path, "wb") as f:
        f.write(pdf_bytes)

    
    conv_res = doc_converter.convert(temp_file_path)
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