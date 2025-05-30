from fastapi import APIRouter
from colearn_chat import colearnChat, ChatItem, ChatRequest, GetClassScheduleRequest
router = APIRouter(prefix="/colearn-chat")
from logger import logger
import time
@router.post("/faq")
def colearnFaqChat(req: ChatRequest) -> ChatItem:
    start_time = time.time()
    response_string = colearnChat(req)

    response =  ChatItem(
        role="assistant",
        content=response_string
    )

    logger.info(response)
    end_time = time.time()
    logger.info(f"Time taken: {end_time - start_time} seconds")
    return response

