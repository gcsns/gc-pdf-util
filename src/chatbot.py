from fastapi import FastAPI
from starlette.responses import StreamingResponse
import asyncio
from fastapi import FastAPI, status
from fastapi.responses import StreamingResponse
import mindsdb_sdk
import time
from fastapi import FastAPI, HTTPException, status
# from fastapi.responses import StreamingResponse
from starlette.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import mindsdb_sdk
from typing import AsyncGenerator
import json
import sys
import json
from pydantic import BaseModel
from typing import List, Optional
from logger import logger
import configs

import time

# server_local = mindsdb_sdk.connect(configs.MINDS_DB_API_ENDPOINT)
# agent = server_local.agents.get(configs.MINDS_DB_MODEL_NAME)

class QuestionData(BaseModel):
    role: Optional[str] = None
    question: str
    answer: Optional[str] = None

def generate_chunks(messages: List[QuestionData]):
    serialized_messages = [message.model_dump() for message in messages]
    for chunk in agent.completion_stream(serialized_messages):
        res = json.dumps(chunk)
        yield res + '$$'
        sys.stdout.flush()


def stream_response(messages: List[QuestionData]):
    return StreamingResponse(generate_chunks(messages), media_type="text/event-stream")
