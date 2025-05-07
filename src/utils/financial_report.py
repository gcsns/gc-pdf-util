from fastapi import HTTPException
import os
from agno.embedder.openai import OpenAIEmbedder
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.knowledge.document import DocumentKnowledgeBase
from agno.document.base import Document
from logger import logger
import base64
import tempfile
from configs.prompts.annual_report.annual_report_financial_analysis_section import financial_analysis_section_description, financial_analysis_section_instructions, financial_analysis_section_queries
from configs.prompts.annual_report.annual_report_about_section import about_section_description, about_section_instructions, about_section_queries
from configs.prompts.annual_report.annual_report_products_section import products_and_services_section_description, products_and_services_section_instructions, products_and_services_section_queries
from typing import List
import configs
from utils.agnoAgent import generate_markdown_content_from_agent

# Function to decode the base64 string to markdown text
def decode_base64_to_markdown(base64_string):
    try:
        decoded_bytes = base64.b64decode(base64_string)
        return decoded_bytes.decode("utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error decoding base64")

from utils.embeddings import get_embeddings
def generate_financial_analysis(mdStrings: List[str]):
    with tempfile.TemporaryDirectory() as temp_dir:
        logger.info("Temp Directory" + str(temp_dir))
        lance_path = os.path.join(temp_dir, "lancedb")
        markdown_string_list = [decode_base64_to_markdown(md) for md in mdStrings]
        documents = []
        model_choice = configs.DEFAULT_EMBEDDINGS_MODEL
        embedder = get_embeddings(model_choice)
        for mdString in markdown_string_list:
            documents.append(Document(content=mdString))
        knowledge_base = DocumentKnowledgeBase(
            documents=documents,
            vector_db=LanceDb(
                uri=lance_path,
                table_name="statement",
                search_type=SearchType.hybrid,
                embedder=embedder,
            ),
        )

    logger.info("Generating about section markdown")
    aboutSectionMdString = generate_markdown_content_from_agent(knowledge_base, about_section_description, about_section_instructions, about_section_queries)
    logger.info("Generating products section markdown")
    ProductSectionMdString = generate_markdown_content_from_agent(knowledge_base, products_and_services_section_description, products_and_services_section_instructions, products_and_services_section_queries)
    logger.info("Generating financial analysis section markdown")
    financialAnalysisMdString = generate_markdown_content_from_agent(knowledge_base, financial_analysis_section_description, financial_analysis_section_instructions, financial_analysis_section_queries)
    

    fullMarkdownString = ""
    fullMarkdownString += "\n# About Section \n"
    fullMarkdownString += aboutSectionMdString
    fullMarkdownString += "\n"
    fullMarkdownString += "\n# Products and Services Section \n"
    fullMarkdownString += ProductSectionMdString
    fullMarkdownString += "\n"
    fullMarkdownString += "\n# Financial Insights section Section \n"
    fullMarkdownString += financialAnalysisMdString
    
    return fullMarkdownString