from dotenv import load_dotenv
load_dotenv()

from prompts import prompt
from memory import Memory
from retrieval import search_query
from langchain.chat_models import init_chat_model
import json


log_folder = r"/mnt/Data1/Python_Projects/Pure-Python/P5/03-LLMs/1-LangChain/Train/p1-staticWebAssistant/log"
llm = init_chat_model(model="gpt-4.1-nano", model_provider="OpenAI")

def run_agent(user_id: str, query: str):
    memory = Memory(user_id=user_id, log_folder_path=log_folder)

    # Agent 1
    chain_1 = prompt[0] | llm
    res_1 = chain_1.invoke(input={"input": query})
    res_1 = json.loads(res_1.content)
    eng_query = res_1["query"]
    language = res_1["language"]

    # # Agent 2
    history, history_doc = memory.get_relevant_history(limit=6)
    if not len(history) == 0:
        chain_2 = prompt[1] | llm
        res_2 = chain_2.invoke(input={"query": eng_query,
                                      "history": history_doc})
        history_query = res_2.content
        print(f"[INFO] Question summary is: {history_query}")
    else:
        history_query = ""

    # # Agent 3
    retrieved_data = search_query(query=history_query)

    # Agent 4
    chain_4 = prompt[3] | llm
    res_4 = chain_4.invoke(input={"query": eng_query, 
                                  "data": retrieved_data,
                                  "context": history})
    res_4 = res_4.content
    

    # Update memory
    memory.update_memory(query=query, response=res_4)

    # Agent 5
    chain_5 = prompt[4] | llm
    res_5 = chain_5.invoke(input={"query": res_4, "language": language})
    res_5 = res_5.content

    return res_5

# while True:
    # query = input("=>")
    # print(run_agent(user_id=1, query=query))
    