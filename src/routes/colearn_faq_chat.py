from fastapi import APIRouter
from colearn_chat import colearnChat, ChatItem, ChatRequest
router = APIRouter(prefix="/colearn-chat")

@router.post("/faq")
def colearnFaqChat(req: ChatRequest) -> ChatItem:
    response_string = colearnChat(req)

    response =  ChatItem(
        role="assistant",
        content=response_string
    )

    return response
