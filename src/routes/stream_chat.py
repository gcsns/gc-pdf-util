from fastapi import UploadFile, File, HTTPException, APIRouter
import os
import uuid
from logger import logger
from pydantic import BaseModel
from typing import List, Optional
from chatbot import stream_response, QuestionData


router = APIRouter(prefix="/stream_chat")

class ChatRequest(BaseModel):
    messages: List[QuestionData]

@router.post("/query-agent")
async def talkToChatbot(request: ChatRequest):
    try:
        messages = request.messages
        response = stream_response(messages)
        return response

    except Exception as e:
        logger.info(f'Error in streaming chat messages{e}')
        raise HTTPException(status_code=500, detail=str(e))