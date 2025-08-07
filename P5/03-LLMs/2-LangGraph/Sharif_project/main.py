from dotenv import load_dotenv
load_dotenv()

from graph import graph
from chain import chain_translate_en, chain_translate_something

def run_agent(query: str, id_: str):
    config = {"configurable": {"thread_id": id_}}

    # Agent 1
    res = chain_translate_en.invoke(query)
    query_en = res.tool_calls[0]["args"]["query"]
    language = res.tool_calls[0]["args"]["language"]

    # Agent 2
    res = graph.invoke({"messages": query_en}, config=config)
    res = res["messages"][-1].content

    # Agent 3
    res = chain_translate_something.invoke({"query": res, "language": language})
    final_answer = res.content

    return final_answer


query = "Who is Amini (probalby at sharif university)?"
query = "Who is Amini?"
query = "میدونی امینی کی هست؟ شنیدم تو دانشگاه شریف هست."
print(run_agent(query=query, id_="1"))