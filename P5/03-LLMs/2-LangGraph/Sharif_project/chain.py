from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from prompts import *
from tools import tools

from dotenv import load_dotenv
load_dotenv()
llm = init_chat_model(model="openai:gpt-4.1-nano", temperature=0)
# llm_with_tools = llm.bind_tools(tools)

# chain1
def translator_en(state):
    chain = prompt_1 | llm
    return {"messages": chain.invoke(state["messages"])}

# chain2
def translator_back(state):
    chain = prompt_2 | llm
    return {"messages": chain.invoke(state["messages"])}

# chain3
def answering(state):
    chain = prompt_3 | llm.bind_tools(tools)
    return {"messages": chain.invoke(state["messages"])}