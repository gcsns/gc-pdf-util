from fastapi import HTTPException, APIRouter
from fastapi.responses import JSONResponse
import requests
import os
from dotenv import load_dotenv
from logger import logger
import base64
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from configs.samples.annual_report import markdown_list
from pydantic import BaseModel

from utils.financial_report import generate_financial_analysis

# Load environment variables
load_dotenv()

router = APIRouter(prefix="/annual-report")
    
class MdRequest(BaseModel):
    mdStrings: List[str]

class MdResponse(BaseModel):
    mdString: str

# FastAPI route to receive the PDF file and generate a financial analysis
@router.post("/generate-financial-analysis")
def generate_financial_analysis_route(mdRequest: MdRequest):
    try:
        logger.info("Generating financial analysis markdown")
        markdownString = generate_financial_analysis(mdRequest.mdStrings)
        response_bytes = markdownString.encode("utf-8")
        base64_bytes = base64.b64encode(response_bytes)
        base64_md_string = base64_bytes.decode("utf-8")
        resp = MdResponse(mdString = base64_md_string)
        json_compatible_item_data = jsonable_encoder(resp)
        logger.info("response generated")
        return JSONResponse(content = json_compatible_item_data)
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f'Error in generating the markdown content. {e}')
    