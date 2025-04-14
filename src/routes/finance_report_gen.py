from fastapi import FastAPI, UploadFile, File, HTTPException, APIRouter
from fastapi.responses import JSONResponse, Response
import requests
import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.knowledge.document import DocumentKnowledgeBase
from agno.document.base import Document
from logger import logger
import base64
import tempfile
from configs.prompts.annual_report import description, instructions, query1, query2, query3

from utils.fileUtil import FileUtil
from configs.samples.annual_report import markdown_list

import io
from pypdf import PdfReader, PdfWriter
from utils.financial_report import convert_pdf_to_markdown, convert_single_pdf_chunk_to_markdown, decode_base64_to_markdown, split_pdf, generate_financial_analysis
from latex_render import convert_markdown_to_latex, latex_to_pdf
import configs

# Load environment variables
load_dotenv()

router = APIRouter(prefix="/annual-report")


# FastAPI route to receive the PDF file and generate a financial analysis
@router.post("/generate-financial-analysis")
async def generate_financial_analysis_route(file: UploadFile = File(...)):
    try:
        logger.info("Generating financial analysis markdown")
        markdownString = await generate_financial_analysis(file)
        logger.debug(markdownString)

        logger.info("Generating financial analysis latex")
        latex_code = convert_markdown_to_latex(markdownString)
        logger.debug(latex_code)

        logger.info("Generating financial analysis PDf")
        pdf_content = latex_to_pdf(latex_code)


        return Response(content=pdf_content, media_type="application/pdf")
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f'Invalid pdf file. {e}')