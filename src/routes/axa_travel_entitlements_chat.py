from fastapi import APIRouter
from axa_travel_chat import axaEntitlementsTravelChat, axaTravelPolicyChat, ChatItem, ChatRequest
router = APIRouter(prefix="/axa-hr")

@router.post("/travel-entitlements-chat")
def axaHrEntitlementsResponse(req: ChatRequest) -> ChatItem:
    response_string = axaEntitlementsTravelChat(req)

    response =  ChatItem(
        role="assistant",
        content=response_string
    )

    return response

@router.post("/travel-policy-chat")
def axaHrPolicyResponse(req: ChatRequest) -> ChatItem:
    response_string = axaTravelPolicyChat(req)

    response =  ChatItem(
        role="assistant",
        content=response_string
    )

    return response