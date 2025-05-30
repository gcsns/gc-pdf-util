from agno.agent import Agent
from agno.models.message import Message
from utils.common import convert_md_to_wa
from logger import logger

# from azure-ai-inference import OpenAIChat

import configs
from utils.agnoLlm import get_llm
from chat_request import ChatRequest, ChatItem
from configs.prompts.enbd_chat.enbd_chat_product_query_system_message import (
    ENBD_CHAT_PRODUCT_QUERY_SYSTEM_MESSAGE,
)


def product_query(req: ChatRequest) -> str:
    formatted_messages = [
        Message(role=i.role, content=i.content, type="text") for i in req.messages
    ]
    product_query_agent = Agent(
        name="Prodcut Query Agent",
        system_message=ENBD_CHAT_PRODUCT_QUERY_SYSTEM_MESSAGE,
        model=get_llm(configs.ENBD_CHAT_PRODUCT_QUERY_LLM),
    )
    response = product_query_agent.run(messages=formatted_messages, markdown=False, stream=False)
    try:
        wa_content = convert_md_to_wa(response.content)
        if response.content != wa_content:
            logger.debug(f"converted md tags from message: {response.content}\n to wa tags to message: {wa_content}")
    except Exception as e:
        logger.warning(f"error in convert_md_to_wa {e}")

    return ChatItem(role="assistant", content=response.content)
