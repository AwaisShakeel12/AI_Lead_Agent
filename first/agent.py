from google.adk.agents import Agent 
from dotenv import load_dotenv
from .tool_prompts import prompt, prompt2, csv_tool,start_async_timer



CSV_FILE_PATH = r'E:\Gen_AI2\ADK2\first\lead.csv'


model_gemini = "gemini-1.5-flash"

csv_agent = Agent(
    model=model_gemini, 
    name="csv_agent",
    description="A helpful Ai Agent for Colleting data.",
    instruction=prompt,
    tools=[csv_tool]
  
)

follow_up_agent = Agent(
     model=model_gemini, 
    name="follow_up_agent",
    description="Sends a follow-up message if user say no",
    instruction=prompt2,
    tools=[csv_tool, start_async_timer]
)


root_agent = Agent(
    name="first", 
    model=model_gemini, 
    description="Route the question to either csv_agent or follow_up_agent",
    instruction="""
    first give user greeting if you dont before
    handel simple query like hii messags. if question is like this not rout to other agent answer by yourself.
    and ask question can we collect some information from you.
    You should rout the question between the sub agents (csv_agent or follow_up_agent)
    
    
    You are AS-AI, a friendly assistant helping us collect basic user information for our records. Please follow these guidelines to ensure a smooth and respectful experience:
    
    - If the user says **No**
      you shoud route to the follow_up_agent.
      
      
    -if user say yes you can collect data   
    you should rout to csv_agent

    """,
    sub_agents=[csv_agent, follow_up_agent]
)


agent = root_agent


