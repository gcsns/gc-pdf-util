import os
from agno.embedder.azure_openai import AzureOpenAIEmbedder
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.knowledge.document import DocumentKnowledgeBase
from agno.document.base import Document
import tempfile
from configs.prompts.axa_travel_chat.axa_travel_entitlements_agent import travelEntitlementsDescription, travelEntitlementsInstructions, travelEntitlementsMdStrings
from configs.prompts.axa_travel_chat.axa_travel_policy_agent import travelPolicyDescription, travelPolicyInstructions, travelPolicyMdStrings

from pydantic import BaseModel
from typing import List
from fastapi import HTTPException, status

from agno.models.message import Message
from utils.agnoAgent import generate_chat_message_from_agent
from utils.embeddings import get_embeddings
import configs

class ChatItem(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatItem]

def axaEntitlementsTravelChat(req: ChatRequest) -> str:
    with tempfile.TemporaryDirectory() as temp_dir:
        # Import the messages form the request
        formatted_messages = [Message(role=i.role, content=i.content) for i in req.messages]


        if(len(formatted_messages) == 0):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The 'messages' list cannot be empty."
            )
        

        # Load documents from the data/docs directory
        documents = [Document(content=item) for item in travelEntitlementsMdStrings]

        lance_path = os.path.join(temp_dir, "lancedb")

        model_choice = configs.DEFAULT_EMBEDDINGS_MODEL
        embedder = get_embeddings(model_choice)

        # Create a knowledge base with the loaded documents
        knowledge_base = DocumentKnowledgeBase(
            documents=documents,
            vector_db=LanceDb(
                    uri=lance_path,
                    table_name="statement",
                    search_type=SearchType.hybrid,
                    embedder=embedder,
                ),
        )

        response_string = generate_chat_message_from_agent(knowledge_base, travelEntitlementsDescription, travelEntitlementsInstructions, formatted_messages)

        return response_string



def axaTravelPolicyChat(req: ChatRequest) -> str:
    with tempfile.TemporaryDirectory() as temp_dir:
        # Import the messages form the request
        formatted_messages = [Message(role=i.role, content=i.content) for i in req.messages]

        if(len(formatted_messages) == 0):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The 'messages' list cannot be empty."
            )


        # Load documents from the data/docs directory
        documents = [Document(content=item) for item in travelPolicyMdStrings]

        lance_path = os.path.join(temp_dir, "lancedb")

        model_choice = configs.DEFAULT_EMBEDDINGS_MODEL
        embedder = get_embeddings(model_choice)
        
        # Create a knowledge base with the loaded documents
        knowledge_base = DocumentKnowledgeBase(
            documents=documents,
            vector_db=LanceDb(
                    uri=lance_path,
                    table_name="statement",
                    search_type=SearchType.hybrid,
                    embedder=embedder,
                ),
        )
        response_string = generate_chat_message_from_agent(knowledge_base, travelPolicyDescription, travelPolicyInstructions, formatted_messages)
        return response_string