from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from tools import search_tool, weather_tool
from memory import Memory
from prompts import prompt
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver


log_folder = r"/mnt/Data1/Python_Projects/Pure-Python/P5/03-LLMs/1-LangChain/Train/p3-TripPlanner/log"
memory_l = MemorySaver()

def run_agent(user_id: str, query: str):
    memory = Memory(user_id=user_id, log_folder_path=log_folder)
    llm = init_chat_model(model="gpt-4.1-nano", model_provider="OpenAI")
    llm_with_tools = create_react_agent(model=llm, tools=[search_tool, weather_tool],
                                        checkpointer=memory_l)
    config = {"configurable": {"thread_id": user_id}}
    chain = prompt[0] | llm_with_tools
    res = chain.invoke(input={"query": query}, config=config)
    
    content = res["messages"][-1]
    
    # Update memory
    memory.update_memory(query=query, response=content.content)

    return content.content

    
