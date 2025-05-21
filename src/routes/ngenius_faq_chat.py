from fastapi import APIRouter
from ngenius_chat import ngeniusChat, ChatItem, ChatRequest
router = APIRouter(prefix="/ngenius-chat")

@router.post("/faq")
def ngeniusFaqChat(req: ChatRequest) -> ChatItem:
    response_string = ngeniusChat(req)

    response =  ChatItem(
        role="assistant",
        content=response_string
    )

    return response
