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
from configs.prompts.annual_report_financial_analysis_section import financial_analysis_section_description, financial_analysis_section_instructions, financial_analysis_section_queries
from configs.prompts.annual_report_about_section import about_section_description, about_section_instructions, about_section_queries
from configs.prompts.annual_report_products_section import products_and_services_section_description, products_and_services_section_instructions, products_and_services_section_queries
from typing import List
import re

# Function to decode the base64 string to markdown text
def decode_base64_to_markdown(base64_string):
    try:
        decoded_bytes = base64.b64decode(base64_string)
        return decoded_bytes.decode("utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error decoding base64")

def remove_markdown_blocks(text: str) -> str:
    """
    Removes LLM-style markdown code block delimiters (e.g., markdown``` and ```) from the input text.

    Args:
        text (str): The input string containing markdown-style block delimiters.

    Returns:
        str: Text with the markdown code block delimiters removed.
    """
    # Remove 'markdown```' lines and lines with just '```'
    cleaned_text = re.sub(r'^markdown```\s*\n?|^```\s*\n?', '', text, flags=re.MULTILINE)
    return cleaned_text

def generate_financial_analysis(mdStrings: List[str]):
    mdStringResponse = generate_markdown_from_agent(mdStrings, financial_analysis_section_description, financial_analysis_section_instructions, financial_analysis_section_queries)
    return mdStringResponse


def generate_about_section(mdStrings: List[str]):
    mdStringResponse = generate_markdown_from_agent(mdStrings, about_section_description, about_section_instructions, about_section_queries)
    return mdStringResponse

def generate_products_section(mdStrings: List[str]):
    mdStringResponse = generate_markdown_from_agent(mdStrings, products_and_services_section_description, products_and_services_section_instructions, products_and_services_section_queries)
    return mdStringResponse




def generate_markdown_from_agent(mdStrings: List[str], description: str, instructions: List[str], queries: List[str]):
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
        
