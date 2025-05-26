from pydantic import BaseModel
from typing import List

class ChatItem(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatItem]
