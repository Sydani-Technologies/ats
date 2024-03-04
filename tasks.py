from crewai import Task
from textwrap import dedent

# class ApplicationTrackingTasks():
#   def __init__(self):
#     pass

def cv_screen(agent, cv_content, criteria):
  return Task(
    description=dedent(f""" 
      Screen the content of this applicant's CV: {cv_content} 
      Determine if they meet this requirements: {criteria} 
      Return a python dict with the following structure: 
      "name": "applicant_name", "email": "applicant_email", "status": "qualified" or "unqualified". 
      
      Only assign the status "qualified" if the applicant's CV meets the requirements; otherwise, assign "unqualified".
      Return only the python dict not str
    """),
    expected_output="A python dict with name, email, and status",
    agent=agent,
  )
  
# research tasks
# class ResearchTasks:
#   def __init__(self, topic, tools, researcher, writer):
#     self.topic = topic
#     self.tools = tools
#     self.researcher = researcher
#     self.writer = writer

def research_task(topic, tools, researcher): 
  return Task(
    description=f"""Identify the next big trend in {topic}.
    Focus on identifying pros and cons and the overall narrative.
    Your final report should clearly articulate the key points,
    its market opportunities, and potential risks.""",
    expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
    tools=tools,
    agent=researcher,
  )

def write_task(topic, tools, writer):
  return Task(
    description=f"""Compose an insightful article on {topic}.
    Focus on the latest trends and how it's impacting the industry.
    This article should be easy to understand, engaging, and positive.""",
    expected_output=f'A 4 paragraph article on {topic} advancements fromated as markdown.',
    tools=tools,
    agent=writer,
    async_execution=False,
    output_file=f"{topic}-blog-post.md"  # Example of output customization
  )

  