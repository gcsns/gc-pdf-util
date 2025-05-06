from agno.agent import Agent
from agno.models.azure import AzureOpenAI
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.knowledge.document import DocumentKnowledgeBase
from agno.document.base import Document
from logger import logger
import re
from fastapi import HTTPException
from agno.models.message import Message
from typing import List
import os

def remove_markdown_blocks(text: str) -> str:
    # Remove 'markdown```' lines and lines with just '```'
    cleaned_text = re.sub(r'^markdown```\s*\n?|^```\s*\n?', '', text, flags=re.MULTILINE)
    return cleaned_text


def generate_markdown_content_from_agent(knowledge_base: DocumentKnowledgeBase, description: str, instructions: List[str], queries: List[str]) -> str:
    try:
        # Load the knowledge base
        knowledge_base.load(recreate=False)

        model = AzureOpenAI(
            id=os.getenv("AZURE_OPENAI_MODEL_NAME"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        )

        # Create an agent with the knowledge base
        agent = Agent(
            model=model,
            description=description,
            instructions=instructions,
            knowledge=knowledge_base
        )

        responseMdString = ""
        logger.info("Generating section content...")
        for query in queries:
            response = agent.run(
                query
            )
            responseMdString += response.content
            responseMdString += "\n"
            logger.info("Chunk Complete")

        responseMdString = remove_markdown_blocks(responseMdString)

        return responseMdString

    except Exception as e:
        raise HTTPException(status_code=400, detail=f'Error in generating markdown string')
        
def generate_chat_message_from_agent(knowledge_base: DocumentKnowledgeBase, description: str, instructions: List[str], chatHistory: List[Message]) -> str:
    try:
        # Load the knowledge base
        knowledge_base.load(recreate=False)

        model = AzureOpenAI(
            id=os.getenv("AZURE_OPENAI_MODEL_NAME"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        )

        # Create an agent with the knowledge base
        agent = Agent(
            model=model,
            description=description,
            instructions=instructions,
            knowledge=knowledge_base,
            add_messages=chatHistory
        )

        user_message = chatHistory[-1].content

        response_string = agent.run(
            user_message, 
            markdown=True,
            stream=False
        )

        responseMdString = remove_markdown_blocks(response_string.content)

        return responseMdString

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail=f'Error in generating markdown string')
     