import os
from agno.agent import Agent
from agno.models.azure import AzureOpenAI
from agno.embedder.azure_openai import AzureOpenAIEmbedder
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.knowledge.document import DocumentKnowledgeBase
from agno.document.base import Document
import tempfile
from configs.agentConfig.axa_travel_entitlements_agent import description, instructions, mdStrings
from pydantic import BaseModel
from typing import List
from fastapi import HTTPException, status

from agno.models.message import Message


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
        documents = [Document(content=item) for item in mdStrings]

        lance_path = os.path.join(temp_dir, "lancedb")

        # Create a knowledge base with the loaded documents
        knowledge_base = DocumentKnowledgeBase(
            documents=documents,
            vector_db=LanceDb(
                    uri=lance_path,
                    table_name="statement",
                    search_type=SearchType.hybrid,
                    embedder=AzureOpenAIEmbedder(id="text-embedding-ada-002"),
                ),
        )

        # Load the knowledge base
        knowledge_base.load(recreate=False)

        azure_model = AzureOpenAI(
            id=os.getenv("AZURE_OPENAI_MODEL_NAME"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        )

        # Create an agent with the knowledge base
        agent = Agent(
            model=azure_model,
            description=description,
            instructions=instructions,
            knowledge=knowledge_base,
            add_messages = formatted_messages
        )

        user_message = formatted_messages[-1].content
        
        response_string = agent.run(
            user_message, 
            markdown=True,
            stream=False
        )

        return response_string.content