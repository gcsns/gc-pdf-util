from agno.agent import Agent
from agno.vectordb.qdrant import Qdrant
from agno.knowledge.document import DocumentKnowledgeBase
from agno.tools.tavily import TavilyTools
from agno.document.base import Document
# from agno.memory.v2.db.sqlite import SqliteMemoryDb
# from agno.memory.v2.memory import Memory
from configs.prompts.ngenius.ngenius_knowledge_agent import ngeniusKnowledgeRole, ngeniusKnowledgeMdStrings, ngeniusKnowledgeMdStrings_small, ngeniusKnowledgeDescription, ngeniusKnowledgeInstructions
from configs.prompts.ngenius.ngenius_main_agent import ngeniusMainDescription, ngeniusMainDescriptionSmall, ngeniusMainInstructions, ngeniusMainInstructionsSmall, ngeniusMainRole, ngeniusMainRoleSmall

from pydantic import BaseModel
from typing import List
from fastapi import HTTPException, status
from agno.document.chunking.semantic import SemanticChunking

from agno.vectordb.lancedb import LanceDb
from agno.vectordb.search import SearchType
from agno.models.message import Message
from utils.embeddings import get_embeddings
from utils.agnoLlm import get_llm
from utils.findandparsejsonobject import findAndParseJsonObject
import configs, json
from logger import logger
import os


class ChatItem(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatItem]

HOME_DIR = os.path.expanduser("~")
LANCE_DB_PATH = os.path.join(HOME_DIR, ".cache", "lancedb")
os.makedirs(LANCE_DB_PATH, exist_ok=True)

if(configs.LOAD_NGENIUS == True):
    # Load documents from the data/docs directory
    small_documents = [Document(content=item) for item in ngeniusKnowledgeMdStrings_small]
    
    documents = [Document(content=item) for item in ngeniusKnowledgeMdStrings]

    embedder = get_embeddings(configs.DEFAULT_EMBEDDINGS_MODEL)

    # vector_db = Qdrant(
    #     collection="ngenius_big_1",
    #     url=configs.QDRANT_URL,
    #     api_key=configs.QDRANT_API_KEY,
    #     embedder=embedder
    # )

    vector_db=LanceDb(
        uri=LANCE_DB_PATH,
        table_name="ngenius_big_1",
        search_type=SearchType.hybrid,
        embedder=embedder
    )
    
    # vector_db_small = Qdrant(
    #     collection='ngenius_small_1',
    #     url=configs.QDRANT_URL,
    #     api_key=configs.QDRANT_API_KEY,
    #     embedder=embedder
    # )

    vector_db_small = LanceDb(
        uri=LANCE_DB_PATH,
        table_name="ngenius_small_1",
        search_type=SearchType.hybrid,
        embedder=embedder
    )

    # Create a knowledge base with the loaded documents
    knowledge_base = DocumentKnowledgeBase(
        documents=documents,
        vector_db=vector_db,
        chunking_strategy=SemanticChunking(similarity_threshold=0.5, chunk_size= 8000)
    )
    
    knowledge_base_small = DocumentKnowledgeBase(
        documents=small_documents,
        vector_db=vector_db_small,
        chunking_strategy=SemanticChunking(similarity_threshold=0.5, chunk_size= 8000)
    )
    
    logger.info("Ngenius Docs added to vectorDB!")


# memory_db = SqliteMemoryDb(table_name="memory", db_file="tmp/brain.db")
# memory = Memory(db=memory_db)


def ngeniusChat(req: ChatRequest) -> str:
    # Import the messages form the request
    formatted_messages = [Message(role=i.role, content=i.content) for i in req.messages]


    if(len(formatted_messages) == 0):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The 'messages' list cannot be empty."
        )
    
    knowledge_base.load(recreate=False)
    knowledge_base_small.load(recreate=False)


    ngenius_documentation_agent = Agent(
        name="N-Genius Documentation Agent",
        tools=[TavilyTools()], 
        show_tool_calls=False,
        instructions= ngeniusKnowledgeInstructions,
        model=get_llm(configs.NGENIUS_LLM_CHOICE, 1),        
    )


    small_kb_agent = Agent(
        name="Conversation Specialist",
        description=ngeniusMainDescriptionSmall,
        role=ngeniusMainRoleSmall,
        model=get_llm(configs.NGENIUS_LLM_CHOICE, 1),        
        instructions=ngeniusMainInstructionsSmall,
        search_knowledge=True,
        # memory=memory,
        # enable_agentic_memory=True,
        knowledge=knowledge_base_small,
        show_tool_calls=True
    )


    faq_agent = Agent(
        name="FAQ Agent",
        description=ngeniusMainDescription,
        role=ngeniusMainRole,
        model=get_llm("openai:gpt-4o", 0),        
        instructions=ngeniusMainInstructions,
        search_knowledge=True,
        knowledge=knowledge_base,
        # memory=memory,
        # enable_agentic_memory=True,
        # team=[ngenius_documentation_agent, small_kb_agent],
        show_tool_calls=False
    )
    
    classification_agent= Agent(
        name="Classification Agent",
        description="You're a classification Agent who classifies an input question to call the appropriate agent, and give a response to the user.",
        role="You take the user question, classify it, call the appropriate agent in the team to get the required information and then respond to the user.",
        model=get_llm("openai:gpt-4o", 0),        
        instructions=[
        "You are a highly skilled classification AI agent skilled in classifying user questions into specific categories.",
        """
        If the User responds with Yes or No or in small responses, then create a complete response on behalf of the user. For example, 
            Agent Question: Do you have User ID and Password?
            User: Yes

        In this case, you should rephrase customer response to Yes, I have USER ID and Password. If you do not understand what the Customer is saying Yes to, then please clarify""",
        """Carefully review the user request and determine if the user is asking a software code level, API level question or a less technical question. You can assess this by looking for common terms such as API, headers, auth, API Key, SDK etc, - terminologies and descriptions that are usually found in a developer documentation or a software integration guide.
            Classify your response as 
            -- Type 1) high complexity technical question
            -- Type 2) low complexity question
            -- Type 3) user says hi or hello and exchanging normal messages to initiate a conversation. 
        """,
        "If you classified the user question as Type 1, then pass the question to 'N-Genius Documentation Agent and present 'N-Genius Documentation Agent's response to the User.",
        "If the user question is classified as Type 2, then check with 'Conversation Specialist' and 'FAQ Agent' for response. Summarize the response from 'Conversation Specialist' and 'FAQ Agent' and present a unified response to the User. If 'Conversation Specialist' and 'FAQ Agent' do not offer any response, then go back to 'N-Genius Documentation Agent and get response from 'N-Genius Documentation Agent.",
        "For type 3 questions, respond back with simple professional responses as any professional customer service agent will do. E.g., Ask the customer - How are you today? How can I help you today?",
        """
        Please do NOT tell the User that you are fetching your response from another agent. DO NOT RESPOND LIKE THE EXAMPLE BELOW.
        **EXAMPLE**
        "It seems like you're asking a technical question related to obtaining an access token, which is typically a part of API integration or authentication processes. I'll transfer your question to the N-Genius Documentation Agent to provide you with the most accurate and detailed information."
        """,
        "If the data recieved about the user query contains code, ALWAYS SHWO THE CODE, do not omit it for the sake of brevity.",
        """Your responses to the user must grow gradually in complexity. Start by giving simple and concise answers, and if the user asks more, give lengthier and more detailed answers. """,
        """The first time a user asks a question, your response should not be more than 3 sentences, even if your team members give longer answers. Shorten them while retaining main points and keep the answer concise.""",
        """Early in the conversation, instruct your teammates to also give shorter and concise answers.""",
        """Later into the conversation, provide more detailed answers""",
        """When asking clarifying questions, ask them one at a time. Do not ask the user multiple questions in the same message.""",
        """
        When giving a final response to the User, please ensure:
            a. Do NOT dump a LOT of info on the Customer
            b. Go step by step in helping the customer come to the root cause of the problem
            c. Ask clarifying questions before giving the final answer. For example, if the user says that I am not able to log in, then ask FIRST if the user has signed up or is this a first time sign up / registration experience of the User. Clarify if the user has received User ID and Password etc.
            d. Please provide information to user in bite sizes. Ask each time if the user wants more details and then you can provide more details as required. Gradually increase the complexity for the User so that the User is not overwhelmed.
        """
    ],
        team=[ngenius_documentation_agent, small_kb_agent, faq_agent],
        # memory=memory,
        # enable_agentic_memory=True,
        show_tool_calls=False
    )

    user_message = formatted_messages[-1].content
    

    response_string = classification_agent.run(
        user_message, 
        user_id="session_id_2",
        markdown=True,
        stream=False
    )


    return response_string.content
