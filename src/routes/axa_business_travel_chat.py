from fastapi import FastAPI, UploadFile, File, HTTPException, APIRouter
from fastapi.responses import JSONResponse
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
from configs.agentConfig.axa_business_travel_agent import description, instructions, mdString

from utils.fileUtil import FileUtil
# from configs.samples.annual_report import markdown_list

import io
from pypdf import PdfReader, PdfWriter

import configs
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/axa-hr")

from agno.models.message import Message

from axa_business_travel_chat_query import axaBusinessTravelChat, ChatItem, ChatRequest

@router.post("/ask-query")
def axaHrResponse(req: ChatRequest) -> ChatItem:
    response_string = axaBusinessTravelChat(req)

    response =  ChatItem(
        role="assistant",
        content=response_string
    )

    return response