from fastapi import APIRouter
from chat_request import ChatRequest, ChatItem
from enbd_chat import product_query

router = APIRouter(prefix="/enbd-chat")


@router.post("/product-query")
def product_query_end_point(req: ChatRequest) -> ChatItem:
    return product_query(req)
