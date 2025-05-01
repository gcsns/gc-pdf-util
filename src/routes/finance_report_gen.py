from fastapi import HTTPException, APIRouter
from fastapi.responses import JSONResponse
from logger import logger
import base64
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from pydantic import BaseModel

from utils.financial_report import generate_financial_analysis

router = APIRouter(prefix="/annual-report")
    
class MdRequest(BaseModel):
    mdStrings: List[str]

class MdResponse(BaseModel):
    mdString: str

# FastAPI route to receive the PDF file and generate a financial analysis section -> similar to 10-k filings analyzer
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
        raise HTTPException(status_code=400, detail=f'Error in generating the markdown content.')


# FastAPI route to receive the PDF file and generate an about section for the company and the leadership
@router.post("/generate-about-section")
def generate_about_section_route(mdRequest: MdRequest):
    try:
        logger.info("Generating about section markdown")
        markdownString = generate_about_section(mdRequest.mdStrings)
        response_bytes = markdownString.encode("utf-8")
        base64_bytes = base64.b64encode(response_bytes)
        base64_md_string = base64_bytes.decode("utf-8")
        resp = MdResponse(mdString = base64_md_string)
        json_compatible_item_data = jsonable_encoder(resp)
        logger.info("response generated")
        return JSONResponse(content = json_compatible_item_data)
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f'Error in generating the markdown content.')



# FastAPI route to receive the PDF file and generate an about section for the company and the leadership
@router.post("/generate-products-section")
def generate_products_section_route(mdRequest: MdRequest):
    try:
        logger.info("Generating products section markdown")
        markdownString = generate_products_section(mdRequest.mdStrings)
        response_bytes = markdownString.encode("utf-8")
        base64_bytes = base64.b64encode(response_bytes)
        base64_md_string = base64_bytes.decode("utf-8")
        resp = MdResponse(mdString = base64_md_string)
        json_compatible_item_data = jsonable_encoder(resp)
        logger.info("response generated")
        return JSONResponse(content = json_compatible_item_data)
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f'Error in generating the markdown content.')
    
# FastAPI route to receive the PDF file and generate an about section for the company and the leadership
@router.post("/generate-full-markdown")
def generate_full_markdown_route(mdRequest: MdRequest):
    try:
        fullMarkdownString = generate_financial_analysis(mdRequest.mdStrings)
        response_bytes = fullMarkdownString.encode("utf-8")
        base64_bytes = base64.b64encode(response_bytes)
        base64_md_string = base64_bytes.decode("utf-8")
        resp = MdResponse(mdString = base64_md_string)
        json_compatible_item_data = jsonable_encoder(resp)
        logger.info("response generated")
        return JSONResponse(content = json_compatible_item_data)
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f'Error in generating the markdown content.')
    
