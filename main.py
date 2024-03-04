from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from crewai import Crew, Process
from agents import ApplicationTrackingAgents
from tasks import ApplicationTrackingTasks
from tools import ApplicationTrackingTools


app = FastAPI()


class CVData(BaseModel):
    cv_url: str
    criteria: str 

@app.get('/')
def index():
   return {"code": 200, "status": "Ok"}

@app.post("/screen")
def screen_cv(data: CVData):
  cv_url = data.cv_url
  criteria = data.criteria
  
  agents = ApplicationTrackingAgents()
  tasks = ApplicationTrackingTasks()
  tools = ApplicationTrackingTools()

  cv_content = tools.cv_loader(file_url=cv_url)
  screening_agent = agents.application_screening_expert()

  screening_task = tasks.screen(
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
@app.get("/write/{topic}")
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