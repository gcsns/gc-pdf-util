from fastapi import APIRouter
from axa_travel_entitlements_chat_query import axaEntitlementsTravelChat, ChatItem, ChatRequest

router = APIRouter(prefix="/axa-hr")

@router.post("/travel-entitlements-chat")
def axaHrResponse(req: ChatRequest) -> ChatItem:
    response_string = axaEntitlementsTravelChat(req)

    response =  ChatItem(
        role="assistant",
        content=response_string
    )

    return response