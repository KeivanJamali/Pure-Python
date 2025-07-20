from dotenv import load_dotenv
load_dotenv()

from prompt import prompt
from memory import Memory
from retrieval import search_query
from langchain_openai import ChatOpenAI
import json


log_folder = r"/mnt/Data1/Python_Projects/Pure-Python/P5/03-LLMs/1-LangChain/Train/p2/log"

def run_agent(user_id: str, query: str):
    llm = ChatOpenAI(model="gpt-4.1-nano", temperature=0)
    memory = Memory(user_id=user_id, log_folder_path=log_folder)

    # Agent 1
    chain_1 = prompt[0] | llm
    res_1 = chain_1.invoke(input={"input": query})
    res_1 = json.loads(res_1.content)
    eng_query = res_1["query"]
    language = res_1["language"]

    # Agent 5
    history, history_doc = memory.get_relevant_history(limit=6)
    if not len(history) == 0:
        chain_5 = prompt[4] | llm
        res_5 = chain_5.invoke(input={"query": eng_query,
                                      "history": history_doc})
        history_query = res_5.content
        print(f"[INFO] Question summary is: {history_query}")
    else:
        history_query = ""

    # Agent 2
    retrieved_data = search_query(query=history_query)

    # Agent 3
    chain_3 = prompt[2] | llm
    res_3 = chain_3.invoke(input={"query": eng_query, 
                                  "data": retrieved_data,
                                  "context": history})
    res_3 = res_3.content

    # Update memory
    memory.update_memory(query=eng_query, response=res_3)

    # Agent 4
    chain_4 = prompt[3] | llm
    res_4 = chain_4.invoke(input={"query": res_3, "language": language})
    res_4 = res_4.content

    return res_4

