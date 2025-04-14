from typing import Annotated
from fastapi import APIRouter, File, Form, UploadFile, HTTPException
from fastapi.responses import FileResponse, Response
from pydantic import BaseModel
import base64

from utils.fileUtil import FileUtil
from utils.pdftoimage import from_pdf_to_image_bytes
from utils.pdf_util import PdfUtil
from configs.latex.markdown_to_pdf import MARKDOWN_TO_PDF_GENERATION_TEMPLATE
from logger import logger

import subprocess
import tempfile
import os

def latex_to_pdf(latex_code: str): 
    """
    Compiles LaTeX code into a PDF and returns it as a PDF response.
    
    Args:
        latex_code (str): The LaTeX code to compile.
    
    Returns:
        Response: A FastAPI Response with the generated PDF.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        # tex_file_path = "-"
        tex_file_path = os.path.join(temp_dir, "document.tex")
        pdf_file_path = os.path.join(temp_dir, "document.pdf")
        
        # Write the LaTeX code to a .tex file
        with open(tex_file_path, "w", encoding="utf-8") as tex_file:
            tex_file.write(latex_code)
        
        # Run pdflatex to generate the PDF
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-output-directory", temp_dir, "-shell-escape", tex_file_path],
            cwd=temp_dir,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False
        )

        # Print the output and error to help with debugging
        logger.debug(result.stdout.decode())
        logger.debug(result.stderr.decode())

        if result.returncode != 0:
            return {"error": "pdflatex compilation failed", "stderr": result.stderr.decode()}

        # Check if PDF exists
        if not os.path.exists(pdf_file_path):
            return {"error": "PDF file was not generated."}
        
        # Read the generated PDF into a BytesIO buffer
        with open(pdf_file_path, "rb") as pdf_file:
            pdf_content = pdf_file.read()
        
        return pdf_content

def convert_markdown_to_latex(mdString: str) -> str:
    latex_code = MARKDOWN_TO_PDF_GENERATION_TEMPLATE.replace('<mdString>', mdString)
    return latex_code
