from dotenv import load_dotenv
from crewai import Agent

# from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from langchain_google_genai import GoogleGenerativeAI
import os


load_dotenv()

google_api_key = os.environ.get('GOOGLE_API_KEY')

# GoogleGemini = GoogleGenerativeAI(model="gemini-pro", google_api_key=google_api_key)
OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

class ApplicationTrackingAgents:
  def __init__(self):
    self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
    # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
    # self.Ollama = Ollama(model="openhermes")

  def application_screening_expert(self):
    return Agent(
      role='Application Screening Expert',
      goal="Efficiently screen job applicants' CVs",
      verbose=True,
      memory=True,
      backstory="""Armed with expertise in candidate evaluation, you meticulously assess job applicants' CVs, ensuring only the most qualified individuals proceed in the hiring process.""",
      allow_delegation=True,
      llm=self.OpenAIGPT35
    )
  
# class ResearchAgents:
#   def __init__(self, topic, tools):
#     self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
#     self.topic = topic
#     self.tools = tools

#   # Creating a senior researcher agent with memory and verbose mode
  

def researcher(topic, tools):
  
  return Agent(
    role='Senior Researcher',
    goal=f'Uncover groundbreaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory="""Driven by curiosity, you're at the forefront of
    innovation, eager to explore and share knowledge that could change
    the world.""",
    tools=tools,
    allow_delegation=True,
    llm=OpenAIGPT35
  )

# Creating a writer agent with custom tools and delegation capability
def writer(topic, tools):

  return Agent(
    role='Writer',
    goal=f'Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory="""With a flair for simplifying complex topics, you craft
    engaging narratives that captivate and educate, bringing new
    discoveries to light in an accessible manner.""",
    tools=tools,
    allow_delegation=False,
    llm=OpenAIGPT35
  )
