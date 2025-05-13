from agno.agent import Agent
from agno.vectordb.qdrant import Qdrant
from agno.knowledge.document import DocumentKnowledgeBase
from agno.document.base import Document
from configs.prompts.colearn.colearn_knowledge_agent import colearnKnowledgeRole, colearnKnowledgeMdStrings, colearnKnowledgeDescription, colearnKnowledgeInstructions
from configs.prompts.colearn.colearn_main_agent import colearnMainDescription, colearnMainInstructions, colearnMainRole

from pydantic import BaseModel
from typing import List
from fastapi import HTTPException, status

from agno.models.message import Message
from utils.embeddings import get_embeddings
from utils.agnoLlm import get_llm
from utils.findandparsejsonobject import findAndParseJsonObject
import configs, json
from logger import logger

class ChatItem(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatItem]

if(configs.LOAD_COLEARN == True):
    # Load documents from the data/docs directory
    documents = [Document(content=item) for item in colearnKnowledgeMdStrings]

    embedder = get_embeddings(configs.DEFAULT_EMBEDDINGS_MODEL)

    vector_db = Qdrant(
        collection=configs.QDRANT_COLEARN_COLLECTION_NAME,
        url=configs.QDRANT_URL,
        api_key=configs.QDRANT_API_KEY,
        embedder=embedder
    )

    # Create a knowledge base with the loaded documents
    knowledge_base = DocumentKnowledgeBase(
        documents=documents,
        vector_db=vector_db,
    )
    logger.info("Colearn Docs added to vectorDB!")

def colearnChat(req: ChatRequest) -> str:
    # Import the messages form the request
    formatted_messages = [Message(role=i.role, content=i.content) for i in req.messages]


    if(len(formatted_messages) == 0):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The 'messages' list cannot be empty."
        )
    
    knowledge_base.load(recreate=False)

    maker_agent = Agent(
        name="Query Maker Agent",
        role=colearnKnowledgeRole,
        model=get_llm(configs.COLEARN_LLM_CHOICE),
        description=colearnKnowledgeDescription,
        instructions=colearnKnowledgeInstructions,
        show_tool_calls=True,
    )

    query_handler_agent = Agent(
        name="Query Handler Agent",
        role=colearnMainRole,
        model=get_llm(configs.COLEARN_LLM_CHOICE),
        description=colearnMainDescription,
        instructions=colearnMainInstructions,  
        search_knowledge=True,
        knowledge=knowledge_base,
        team=[maker_agent],
        show_tool_calls=True
    )

    user_message = formatted_messages[-1].content
    

    response_string = query_handler_agent.run(
        user_message, 
        markdown=True,
        stream=False
    )
    json_response = findAndParseJsonObject(response_string.content)
    
    return json.dumps(json_response)
    # return json_response.message

