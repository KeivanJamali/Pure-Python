from dotenv import load_dotenv
load_dotenv()

from prompts import prompt
from memory import Memory
from retrieval import search_query
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
import json


log_folder = r"/mnt/Data1/Python_Projects/Pure-Python/P5/03-LLMs/1-LangChain/Train/p2-MyWebsiteAsistant/log"
llm = init_chat_model(model="gpt-4.1-nano", model_provider="OpenAI")
llm_with_search_tool = create_react_agent(model=llm,
                                          tools=[search_query])
memory_l = MemorySaver()

def run_agent(user_id: str, query: str):
    memory = Memory(user_id=user_id, log_folder_path=log_folder)
    config = {"configurable": {"thread_id": user_id}}

    # Agent 1
    chain_1 = prompt[0] | llm
    res_1 = chain_1.invoke(input={"input": query})
    res_1 = json.loads(res_1.content)
    eng_query = res_1["query"]
    language = res_1["language"]

    # Agent 3
    chain_3 = prompt[2] | llm_with_search_tool
    res_3 = chain_3.invoke(input={"query": eng_query}, config=config)
    for message in res_3["messages"]:
        message.pretty_print()
    res_3 = res_3["messages"][-1]
    res_3 = res_3.content
    

    # Update memory
    memory.update_memory(query=eng_query, response=res_3)

    # Agent 4
    chain_4 = prompt[3] | llm
    res_4 = chain_4.invoke(input={"query": res_3, "language": language})
    res_4 = res_4.content
    return res_4

# while True:
    # query = input("=>")
    # run_agent(user_id=1, query=query)
    