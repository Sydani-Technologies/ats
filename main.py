from typing import Union
from fastapi import APIRouter, FastAPI
from pydantic import BaseModel
from crewai import Crew, Process
from agents import application_screening_expert
from tasks import cv_screen
from tools import cv_loader

prefix_router = APIRouter(prefix="/ai/api")


app = FastAPI()


class CVData(BaseModel):
    cv_url: str
    criteria: str 

@prefix_router.get("/")
def index():
   return {"code": 200, "status": "Ok"}

@prefix_router.post("/screen")
def screen_cv(data: CVData):
  cv_url = data.cv_url
  criteria = data.criteria
  
  # agents = ApplicationTrackingAgents()
  # tasks = ApplicationTrackingTasks()

  cv_content = cv_loader(file_url=cv_url)
  screening_agent = application_screening_expert()

  screening_task = cv_screen(
     agent=screening_agent, 
     cv_content=cv_content, 
     criteria=criteria
  )

  crew = Crew(
    agents=[screening_agent],
    tasks=[screening_task],
    process=Process.sequential  # Optional: Sequential task execution is default
  )

  result = crew.kickoff()
 
  return result

# Research endpoint -> Never mind this endpoint is just for testing---------
@prefix_router.get("/write/{topic}")
def task_agent(topic: str):
  # print(topic)
  from langchain_community.tools import DuckDuckGoSearchRun
  # from tools import ResearchTools
  from agents import researcher, writer
  from tasks import research_task, write_task

  search_tool = DuckDuckGoSearchRun()
  # tools_class = ResearchTools()
  tools = [search_tool]

  researcher = researcher(topic=topic, tools=tools)
  writer = writer(topic=topic, tools=tools)

  search_task = research_task(topic=topic, tools=tools, researcher=researcher)
  writing_task = write_task(topic=topic, tools=tools, writer=writer)
  
  crew = Crew(
    agents=[researcher, writer],
    tasks=[search_task, writing_task],
    process=Process.sequential  # Optional: Sequential task execution is default
  )

  result = crew.kickoff()
  return result

app.include_router(prefix_router)