from typing import Annotated
from fastapi import APIRouter, File, Form, UploadFile, HTTPException
from fastapi.responses import FileResponse, Response
from pydantic import BaseModel
import base64

from utils.fileUtil import FileUtil
from utils.pdftoimage import from_pdf_to_image_bytes
from utils.pdf_util import PdfUtil
from logger import logger

import subprocess
import tempfile
import os

router = APIRouter(prefix="/pdf")

from pdf_extraction import recreatePdfFunc
from latex_render import latex_to_pdf

@router.post("/render-latex-pdf")
def latex_to_pdf_route(latex_code: str = Form(...)):  # Accepts form data
    """
    Compiles LaTeX code into a PDF and returns it as a PDF response.
    
    Args:
        latex_code (str): The LaTeX code to compile.
    
    Returns:
        Response: A FastAPI Response with the generated PDF.
    """
    pdf_content = latex_to_pdf(latex_code)
    
    # Return the PDF as a response
    return Response(content=pdf_content, media_type="application/pdf")

@router.post("/recreate-pdf")
def recreatePdf(
    file: UploadFile = File(description="PDF file to be recreated"),
):
    """
    Takes a PDf as input, extracts information from it into a markdown file, converts the markdown file into a PDF with readable text using latex and returns it.
    
    Args:
        file (File): The PDF file to be recreated.
    
    Returns:
        Response: A FastAPI Response with the generated PDF.
    """
    resp = recreatePdfFunc(file)
    return resp