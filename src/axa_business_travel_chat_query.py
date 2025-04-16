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

from agno.models.message import Message


class ChatItem(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatItem]

def axaBusinessTravelChat(req: ChatRequest) -> str:
    with tempfile.TemporaryDirectory() as temp_dir:
        # Import the messages form the request
        formatted_messages = [Message(role=i.role, content=i.content) for i in req.messages]
        
        # Load documents from the data/docs directory
        documents = [Document(content=mdString)]

        lance_path = os.path.join(temp_dir, "lancedb")

        # Create a knowledge base with the loaded documents
        knowledge_base = DocumentKnowledgeBase(
            documents=documents,
            vector_db=LanceDb(
                    uri=lance_path,
                    table_name="statement",
                    search_type=SearchType.hybrid,
                    embedder=OpenAIEmbedder(id="text-embedding-ada-002"),
                ),
        )

        # Load the knowledge base
        knowledge_base.load(recreate=False)


        # Create an agent with the knowledge base
        agent = Agent(
            model=OpenAIChat(id="gpt-4o"),
            description=description,
            instructions=instructions,
            knowledge=knowledge_base,
            add_messages = formatted_messages
        )

        user_message = formatted_messages[-1].content
        
        response_string = agent.run(
            user_message, 
            markdown=True,
            stream=False
        )

        return response_string.content