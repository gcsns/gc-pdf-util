from agno.agent import Agent
from agno.vectordb.qdrant import Qdrant
from agno.knowledge.document import DocumentKnowledgeBase
from agno.document.base import Document
from configs.prompts.colearn.colearn_knowledge_agent import colearnKnowledgeRole, colearnKnowledgeMdStrings, colearnKnowledgeDescription, colearnKnowledgeInstructions
from configs.prompts.colearn.colearn_main_agent import colearnMainDescription, colearnMainInstructions, colearnMainRole

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

class GetClassScheduleRequest(BaseModel):
    message: str

if(configs.LOAD_COLEARN == True):
    # Load documents from the data/docs directory
    documents = [Document(content=item) for item in colearnKnowledgeMdStrings]

    embedder = get_embeddings(configs.DEFAULT_EMBEDDINGS_MODEL)

    vector_db = Qdrant(
        collection=configs.QDRANT_COLEARN_COLLECTION_NAME,
        url=configs.QDRANT_URL,
        api_key=configs.QDRANT_API_KEY,
        embedder=embedder
    )

    # Create a knowledge base with the loaded documents
    knowledge_base = DocumentKnowledgeBase(
        documents=documents,
        vector_db=vector_db,
    )
    logger.info("Colearn Docs added to vectorDB!")











def colearnChat(req: ChatRequest) -> str:
    # Import the messages form the request
    formatted_messages = [Message(role=i.role, content=i.content) for i in req.messages]


    if(len(formatted_messages) == 0):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The 'messages' list cannot be empty."
        )
    
    knowledge_base.load(recreate=False)

    maker_agent = Agent(
        name="Query Maker Agent",
        role=colearnKnowledgeRole,
        model=get_llm(configs.COLEARN_LLM_CHOICE),
        description=colearnKnowledgeDescription,
        instructions=colearnKnowledgeInstructions,
        show_tool_calls=True,
    )

    class_schedule_agent = Agent(
        name="Class Schedule Agent",
        role="Can get the class schedule.",
        model=get_llm(configs.COLEARN_LLM_CHOICE),
        description="Retrieves the class schedule.",
        instructions=["Do not process response, give it as you receive from get_class_schedule.", "YOU MUST RETURN THE JSON AS IS TO THE USER"],
        tools=[get_class_schedule], 
        show_tool_calls=True, 
        markdown=False, 
    )

    query_handler_agent = Agent(
        name="Query Handler Agent",
        role=colearnMainRole,
        model=get_llm(configs.COLEARN_LLM_CHOICE),
        description=colearnMainDescription,
        instructions=colearnMainInstructions,  
        search_knowledge=True,
        knowledge=knowledge_base,
        team=[maker_agent, class_schedule_agent],
        show_tool_calls=True
    )

    


    user_message = formatted_messages[-1].content
    

    response_string = query_handler_agent.run(
        user_message, 
        markdown=True,
        stream=False
    )
    json_response = findAndParseJsonObject(response_string.content)
    
    return json.dumps(json_response)
    # return json_response.message


import requests, httpx


def get_class_schedule(kelas: int, sem: int= 2, year: int= 2025, curriculum: str = "Kurikulum Merdeka", subject: str = "Kimia") -> str:
    """Use this function to get schedule.

    Args:
        num_stories (int): Number of stories to return. Defaults to 10.
        `kelas` (int): Specifies the class or grade level. Example: `kelas=12` for grade 12. 
        `sem` (int): Indicates the semester. Example: `sem=2` for the second semester.
        `year` (int): The academic year for which the schedule is being fetched. Example: `year=2025`.
        `curriculum` (str): Specifies the curriculum type. Example: `curriculum=Kurikulum Merdeka`.
        `subject` (str): The subject for which the schedule is being requested. Example: `subject=Kimia`.

    Returns:
        str: JSON string of following format
        { 
            schedule: [{
                "days": "Senin",
                "time": "17:15 - 18:15",
                "teacher": "Kak Windi",
                "seatsLeft": 70,
                "classStarted": true,
                "subject": "Kimia Merdeka - Kelas 12 SMT 2",
                "course_id": "e265144e-b747-4bb1-aab1-377e7ad96828"
            }]
        }
    """

    logger.debug("Getting class schedule for {} {} {} {} {}".format(kelas, sem, year, curriculum, subject))
    url = "https://e2oc2ege54.execute-api.ap-southeast-1.amazonaws.com/slotschedule?kelas={}&sem={}&year={}&curriculum={}&subject={}".format(kelas, sem, year, curriculum, subject)


    response = requests.request("GET", url, headers={}, data={})

    logger.debug("Class schedule for {} {} {} {} {}".format(kelas, sem, year, curriculum, subject))
    logger.debug(response.json())

    return json.dumps({
        "schedule": response.json()
    })


def get_class_chedule_from_agent(req: GetClassScheduleRequest) -> str:
    userMessage = req.message
    response_string = agent.run(userMessage, stream=False)
    return response_string.content








