from dotenv import load_dotenv
load_dotenv()

from graph import graph
from chain import chain_translate_en, chain_translate_something

def run_agent(query: str, id_: str):
    config = {"configurable": {"thread_id": id_}}

    # Agent 1
    print(f"[INFO] Agent 1 started...")
    res = chain_translate_en.invoke(query)
    query_en = res.query
    language = res.language
    print(f"[INFO] Agent 1 finished (Detected language: {language}).\n")

    # Agent 2
    print(f"[INFO] Agent 2 started...")
    res = graph.invoke({"messages": query_en}, config=config)
    res = res["messages"][-1].content
    print(f"[INFO] Agent 2 finished.\n")

    # Agent 3
    print(f"[INFO] Agent 3 started...")
    res = chain_translate_something.invoke({"query": res, "language": language})
    final_answer = res.content
    print(f"[INFO] Agent 3 finished.\n")

    return final_answer

query1 = "Who is Amini (probalby at sharif university)?"
# query1 = "what was my last question?"
# query2 = "what about now? what was my last question?"
# query = "Who is Amini?"
# query = "میدونی امینی کی هست؟ شنیدم تو دانشگاه شریف هست."
print(run_agent(query=query1, id_="4"))
# print(run_agent(query=query2, id_="1"))

