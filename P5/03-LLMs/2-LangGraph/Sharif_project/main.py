from dotenv import load_dotenv
load_dotenv()

from typing import List, Annotated
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage, ToolMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from chain import translator_en, translator_back, answering
from tools import tools

class State(TypedDict):
    messages: Annotated[list, add_messages]

def continue_func(state: List[BaseMessage]):
    count_tool_visit = sum(isinstance(item, ToolMessage) for item in state)
    if count_tool_visit > 0:
        return "finish"
    else:
        return "continue"

tool_executer = ToolNode(tools)

builder = StateGraph(State)
builder.add_node("en_translation", translator_en)
builder.add_node("back_translation", translator_back)
builder.add_node("answering", answering)
builder.add_node("tool_executer", tool_executer)
builder.add_edge(START, "en_translation")
builder.add_edge("en_translation", "answering")
builder.add_conditional_edges("answering", continue_func, {"finish":"back_translation",
                                                           "continue":"tool_executer"})
builder.add_edge("tool_executer", "answering")
builder.add_edge("back_translation", END)

memory = InMemorySaver()
graph = builder.compile(checkpointer=memory)

graph.get_graph().draw_mermaid_png(output_file_path="./pic.png")


def run_agent(query:str, id:str):
    config = {"configurable": {"thread_id": id}}
    # res = graph.invoke({"messages": [{"role": "user", "content": query}]},
                        # config=config)
    res = graph.stream({"messages": [{"role": "user", "content": query}]},
                        config=config)
    for event in res:
        event["en_translation"]["messages"].pretty_print()
    
    