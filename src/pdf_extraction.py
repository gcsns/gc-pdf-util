
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

import shutil

doc_converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
)


def recreatePdfFunc(
    file: UploadFile = File(description="PDF file to be recreated"),
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


    # create a temp.md file inside the temp directory
    temp_md_path = os.path.join(temp_dir, "markdown-with-images.md")
    temp_md_path = Path(temp_md_path)
    
    # # Save markdown with embedded pictures
    # conv_res.document.save_as_markdown(temp_md_path, image_mode=ImageRefMode.EMBEDDED)

    # Save markdown with externally referenced pictures
    conv_res.document.save_as_markdown(temp_md_path, image_mode=ImageRefMode.REFERENCED)

    logger.debug("=============================================")
    logger.debug("Markdown has been created")
    logger.debug(table_counter)
    logger.debug(picture_counter)
    logger.debug("=============================================")

    temp_md_path = str(temp_md_path)
    with open(temp_md_path, "r") as md_file:
         md_string = md_file.read()
    
    md_string = str(md_string)

    tex_file_path = os.path.join(temp_dir, "document.tex")
    temp_final_pdf_path = os.path.join(temp_dir, "document.pdf")

    latex_code = configs.MARKDOWN_TO_PDF_GENERATION_TEMPLATE

    with open(tex_file_path, "w", encoding="utf-8") as tex_file:
        tex_file.write(latex_code)

    try:
        # subprocess.run(["pdflatex", "--shell-escape", "-interaction=nonstopmode", "-output-directory", temp_dir, tex_file_path],
        #                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        subprocess.run(["pdflatex", "--shell-escape", "-output-directory", temp_dir, tex_file_path],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, cwd=temp_dir)
    except subprocess.CalledProcessError as e:
        return {"error": "pdflatex compilation failed: " + str(e)}
    

    # temp_html_path = str(temp_html_path)
    # pdfkit.from_file(temp_html_path, temp_final_pdf_path)
    
    # # Create a temporary ZIP file
    # with tempfile.NamedTemporaryFile(delete=False, suffix=".zip") as temp_zip:
    #     zip_path = temp_zip.name

    # shutil.make_archive(zip_path.replace(".zip", ""), 'zip', temp_dir)

    # return FileResponse(zip_path, filename="files.zip", media_type="application/zip")
    
    with open(temp_final_pdf_path, "rb") as pdf_file:
            pdf_content = pdf_file.read()

    return Response(content=pdf_content, media_type="application/pdf")