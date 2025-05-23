from fastapi import APIRouter
from colearn_chat import colearnChat, ChatItem, ChatRequest, get_class_chedule_from_agent, GetClassScheduleRequest
router = APIRouter(prefix="/colearn-chat")
from logger import logger

@router.post("/faq")
def colearnFaqChat(req: ChatRequest) -> ChatItem:
    response_string = colearnChat(req)

    response =  ChatItem(
        role="assistant",
        content=response_string
    )

    logger.info(response)

    return response


@router.post("/get-class-schedule")
def get_class_schedule(req: GetClassScheduleRequest) -> str:
    response = get_class_chedule_from_agent(req)
    return response
