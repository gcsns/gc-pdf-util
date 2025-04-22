from fastapi import HTTPException
import requests
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

# from configs.samples.annual_report import markdown_list

import io
from pypdf import PdfReader, PdfWriter

import configs



# Endpoint to convert PDF to markdown (this is an external service)
convert_to_markdown_endpoint = configs.GC_AI_PARSERS_BASE_URL + '/api/pdf/convert-to-markdown'

# Function to convert PDF to markdown using the external API
def convert_pdf_to_markdown(file_buffer, file_name):
    headers = {
        "Authorization": f"Bearer {configs.GC_AI_API_KEY}",
    }

    form_data = {
        "file": (file_name, file_buffer, "application/pdf")
    }

    try:
        response = requests.post(convert_to_markdown_endpoint, files=form_data, headers=headers)
        response.raise_for_status()
        return response.json()  # Assume this returns the markdown
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error converting PDF: {e}")


# Convert a single chunk via API
def convert_single_pdf_chunk_to_markdown(chunk_buffer, file_name, chunk_index):
    headers = {
        "Authorization": f"Bearer {configs.GC_AI_API_KEY}",
    }

    files = {
        "file": (f"{file_name}_part{chunk_index}.pdf", chunk_buffer, "application/pdf")
    }

    try:
        response = requests.post(convert_to_markdown_endpoint, files=files, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error converting PDF chunk {chunk_index}: {e}")


# Function to decode the base64 string to markdown text
def decode_base64_to_markdown(base64_string):
    try:
        decoded_bytes = base64.b64decode(base64_string)
        return decoded_bytes.decode("utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error decoding base64: {e}")


# Split PDF into chunks
def split_pdf(file_buffer, chunk_size=configs.DEFAULT_PDF_CHUNK_SIZE):
    file_buffer.seek(0)
    reader = PdfReader(file_buffer)
    total_pages = len(reader.pages)
    chunks = []

    for start in range(0, total_pages, chunk_size):
        writer = PdfWriter()
        for i in range(start, min(start + chunk_size, total_pages)):
            writer.add_page(reader.pages[i])

        output_buffer = io.BytesIO()
        writer.write(output_buffer)
        output_buffer.seek(0)
        chunks.append(output_buffer)

    return chunks


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
            raise HTTPException(status_code=400, detail=f'{e}')
