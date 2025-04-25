from fastapi import HTTPException
import os
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.knowledge.document import DocumentKnowledgeBase
from agno.document.base import Document
from logger import logger
import base64
import tempfile
from configs.prompts.annual_report import description, instructions, query1, query2, query3
from typing import List

# Function to decode the base64 string to markdown text
def decode_base64_to_markdown(base64_string):
    try:
        decoded_bytes = base64.b64decode(base64_string)
        return decoded_bytes.decode("utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error decoding base64")

def generate_financial_analysis(mdStrings: List[str]):
    with tempfile.TemporaryDirectory() as temp_dir:
        logger.info("Temp Directory" + str(temp_dir))
        try:
            markdown_string_list = [decode_base64_to_markdown(md) for md in mdStrings]

            # setting the markdowns to the sample
            documents = []

            for mdString in markdown_string_list:
                documents.append(Document(content=mdString))

            lance_path = os.path.join(temp_dir, "lancedb")

            # Create a knowledge base with the loaded documents
            knowledge_base = DocumentKnowledgeBase(
                documents=documents,
                vector_db=LanceDb(
                    uri=lance_path,
                    table_name="statement",
                    search_type=SearchType.hybrid,
                    embedder=OpenAIEmbedder(id="text-embedding-ada-002"),
                ),
            )

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
            queries = [query1, query2, query3]
            for query in queries:
                response = agent.run(
                    query
                )
                responseMdString += response.content
                responseMdString += "\n"
                logger.info("Chunk Complete")

            return responseMdString

        except Exception as e:
            raise HTTPException(status_code=400, detail=f'Error in generating markdown string')
