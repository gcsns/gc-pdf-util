from agno.agent import Agent
from agno.vectordb.qdrant import Qdrant
from agno.knowledge.document import DocumentKnowledgeBase
from agno.document.base import Document
from configs.prompts.colearn.colearn_knowledge_agent import colearnKnowledgeRole, colearnKnowledgeMdStrings
from configs.prompts.colearn.colearn_main_agent import colearnMainDescription, colearnMainInstructions, colearnMainRole

from pydantic import BaseModel
from typing import List
from fastapi import HTTPException, status

from agno.models.message import Message
from utils.embeddings import get_embeddings
from utils.agnoLlm import get_llm
import configs
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

    knowledge_agent = Agent(
        name="CoLearn Knowledge Agent",
        role=colearnKnowledgeRole,
        model=get_llm(configs.COLEARN_LLM_CHOICE),
        knowledge=knowledge_base,
        search_knowledge=True,
        show_tool_calls=False,
    )

    agentTeam = Agent(
        name="Alex",
        role=colearnMainRole,
        description=colearnMainDescription, 
        instructions=colearnMainInstructions, 
        add_messages=formatted_messages, 
        show_tool_calls=False,
        team=[knowledge_agent],
        model=get_llm(configs.COLEARN_LLM_CHOICE),
        search_knowledge=False,
    )

    user_message = formatted_messages[-1].content
    

    response_string = agentTeam.run(
        user_message, 
        markdown=True,
        stream=False
    )

    

    return response_string.content

