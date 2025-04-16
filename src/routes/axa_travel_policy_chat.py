from fastapi import APIRouter
from axa_travel_policy_chat_query import axaTravelPolicyChat, ChatItem, ChatRequest

router = APIRouter(prefix="/axa-hr")

@router.post("/travel-policy-chat")
def axaHrResponse(req: ChatRequest) -> ChatItem:
    response_string = axaTravelPolicyChat(req)

    response =  ChatItem(
        role="assistant",
        content=response_string
    )

    return response