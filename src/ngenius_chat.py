from agno.agent import Agent
from agno.vectordb.qdrant import Qdrant
from agno.knowledge.document import DocumentKnowledgeBase
from agno.tools.tavily import TavilyTools
from agno.document.base import Document
from configs.prompts.ngenius.ngenius_knowledge_agent import ngeniusKnowledgeRole, ngeniusKnowledgeMdStrings, ngeniusKnowledgeDescription, ngeniusKnowledgeInstructions
from configs.prompts.ngenius.ngenius_main_agent import ngeniusMainDescription, ngeniusMainInstructions, ngeniusMainRole

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

if(configs.LOAD_NGENIUS == True):
    # Load documents from the data/docs directory
    documents = [Document(content=item) for item in ngeniusKnowledgeMdStrings]

    embedder = get_embeddings(configs.DEFAULT_EMBEDDINGS_MODEL)

    vector_db = Qdrant(
        collection=configs.QDRANT_NGENIUS_COLLECTION_NAME,
        url=configs.QDRANT_URL,
        api_key=configs.QDRANT_API_KEY,
        embedder=embedder
    )

    # Create a knowledge base with the loaded documents
    knowledge_base = DocumentKnowledgeBase(
        documents=documents,
        vector_db=vector_db,
    )
    logger.info("Ngenius Docs added to vectorDB!")

def ngeniusChat(req: ChatRequest) -> str:
    # Import the messages form the request
    formatted_messages = [Message(role=i.role, content=i.content) for i in req.messages]


    if(len(formatted_messages) == 0):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The 'messages' list cannot be empty."
        )
    
    knowledge_base.load(recreate=False)

    # maker_agent = Agent(
    #     name="Query Maker Agent",
    #     role=ngeniusKnowledgeRole,
    #     model=get_llm(configs.NGENIUS_LLM_CHOICE),
    #     description=ngeniusKnowledgeDescription,
    #     instructions=ngeniusKnowledgeInstructions,
    #     show_tool_calls=True,
    # )

    ngenius_documentation_agent = Agent(
        name="NGenius Documentation Agent",
        tools=[TavilyTools()], 
        show_tool_calls=True,
        instructions= ngeniusKnowledgeInstructions,
        model=get_llm(configs.NGENIUS_LLM_CHOICE, 1),        
    )


    # query_handler_agent = Agent(
    #     name="Query Handler Agent",
    #     role=ngeniusMainRole,
    #     model=get_llm(configs.NGENIUS_LLM_CHOICE),
    #     description=ngeniusMainDescription,
    #     instructions=ngeniusMainInstructions,  
    #     search_knowledge=True,
    #     knowledge=knowledge_base,
    #     team=[maker_agent],
    #     show_tool_calls=True
    # )

    query_handler_agent = Agent(
        name="Query Handler Agent",
        description=ngeniusMainDescription,
        role=ngeniusMainRole,
        model=get_llm(configs.NGENIUS_LLM_CHOICE, 1),        
        instructions=ngeniusMainInstructions,
        search_knowledge=True,
        knowledge=knowledge_base,
        team=[ngenius_documentation_agent],
        show_tool_calls=True
    )



    # testTavilyAgent = Agent(
    #     name="NGenius AI Agent",
    #     tools=[TavilyTools()], 
    #     show_tool_calls=True,
    #     instructions= ["Always include examples", "When referring to documentation, include the relevant section or direct link if available"],
    #     # instructions=[
    #     #     "Fetch information only from the official NGENIUS documentation - https://docs.ngenius-payments.com/reference/set-up-n-genius uning 'TavilyTools'.",
    #     #     "Focus on answering questions related to troubleshooting, setup, and integration of NGENIUS.",
    #     #     "Always provide accurate and concise responses based on official documentation.",
    #     #     "If multiple solutions exist, list them in order of most commonly effective to least.",
    #     #     "Do not provide information about licensing, billing, or sales unless explicitly available on the NGENIUS documentation.",
    #     #     "When referring to documentation, include the relevant section or direct link if available.",
    #     #     "Clarify ambiguous user questions by asking follow-up questions before providing an answer.",
    #     #     "Respond in a professional and helpful tone suitable for technical support.",
    #     #     "Avoid speculation—only respond based on verifiable content from the NGENIUS site.",
    #     #     "If no relevant information is found, acknowledge the limitation and suggest contacting NGENIUS support directly."
    #     # ],
    #     model=get_llm(configs.NGENIUS_LLM_CHOICE, 1),
    #     # description="Fetches relevant information from the NGENIUS website to assist with troubleshooting and integration-related questions. The agent provides accurate, real-time responses by referencing official documentation, support articles, and other web resources.",
    #     # role="Act as a support assistant for NGENIUS by retrieving information from its official documentation. Answer user queries related to troubleshooting, setup, and integration by referencing up-to-date documentation and support content. Ensure responses are accurate, context-aware, and aligned with the platform's best practices."
        
    # )


    user_message = formatted_messages[-1].content
    

    response_string = query_handler_agent.run(
        user_message, 
        markdown=True,
        stream=False
    )


    return response_string.content
    # json_response = findAndParseJsonObject(response_string.content)
    
    # return json.dumps(json_response)
    # return json_response.message

