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

@router.post("/render-latex-pdf")
def latex_to_pdf(latex_code: str = Form(...)):  # Accepts form data
    """
    Compiles LaTeX code into a PDF and returns it as a PDF response.
    
    Args:
        latex_code (str): The LaTeX code to compile.
    
    Returns:
        Response: A FastAPI Response with the generated PDF.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        tex_file_path = os.path.join(temp_dir, "document.tex")
        pdf_file_path = os.path.join(temp_dir, "document.pdf")
        
        # Write the LaTeX code to a .tex file
        with open(tex_file_path, "w", encoding="utf-8") as tex_file:
            tex_file.write(latex_code)
        
        # Run pdflatex to generate the PDF
        try:
            subprocess.run(["pdflatex", "-interaction=nonstopmode", "-output-directory", temp_dir, tex_file_path],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        except subprocess.CalledProcessError:
            return {"error": "pdflatex compilation failed"}
        
        # Check if PDF exists
        if not os.path.exists(pdf_file_path):
            return {"error": "PDF file was not generated."}
        
        # Read the generated PDF into a BytesIO buffer
        with open(pdf_file_path, "rb") as pdf_file:
            pdf_content = pdf_file.read()
        
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