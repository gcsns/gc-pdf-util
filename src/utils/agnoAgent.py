from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.knowledge.document import DocumentKnowledgeBase
from agno.document.base import Document
from logger import logger
import re
from fastapi import HTTPException
from typing import List

def remove_markdown_blocks(text: str) -> str:
    # Remove 'markdown```' lines and lines with just '```'
    cleaned_text = re.sub(r'^markdown```\s*\n?|^```\s*\n?', '', text, flags=re.MULTILINE)
    return cleaned_text


def generate_markdown_from_agent(knowledge_base: DocumentKnowledgeBase, description: str, instructions: List[str], queries: List[str]):
    try:
        # Load the knowledge base
        knowledge_base.load(recreate=False)

        # Create an agent with the knowledge base
        agent = Agent(
            model=OpenAIChat(id="gpt-4o"),
            description=description,
            instructions=instructions,
            knowledge=knowledge_base,
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
        