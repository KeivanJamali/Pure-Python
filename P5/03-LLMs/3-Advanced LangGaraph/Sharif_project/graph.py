from dotenv import load_dotenv
load_dotenv()

from typing import List
from langgraph.graph import START, END, StateGraph
from langgraph.prebuilt import ToolNode
from langchain_core.tools import StructuredTool
from chain import chain_decide_on_tool, chain_to_answer
from schema import SearchLocalDocs, SearchTheWeb, State
from tools import extract_related_files, search_web
from langchain_core.messages import BaseMessage, AIMessage
from langgraph.checkpoint.memory import InMemorySaver

def should_use_tool(state: List[BaseMessage]):
    last_msg = state["messages"][-1]
    if isinstance(last_msg, AIMessage) and last_msg.tool_calls:
        return "go_to_tools"
    return "pass"

def deciding(state: List[BaseMessage]):
    return {"messages" : chain_decide_on_tool.invoke({"messages": state["messages"]})}

def final_answering(state: List[BaseMessage]):
    return {"messages" : chain_to_answer.invoke({"messages": state["messages"], "information": state["messages"][-1].content})}

tool_node = ToolNode([StructuredTool.from_function(extract_related_files, name=SearchLocalDocs.__name__),
                      StructuredTool.from_function(search_web, name=SearchTheWeb.__name__)])

builder = StateGraph(State)
builder.add_node("initial", deciding)
builder.add_node("tools", tool_node)
builder.add_node("final", final_answering)

builder.add_edge(START, "initial")
builder.add_conditional_edges("initial", should_use_tool, {"go_to_tools": "tools", "pass": END})
builder.add_edge("tools", "final")
builder.add_edge("final", END)

memory = InMemorySaver()
graph = builder.compile(checkpointer=memory)
graph.get_graph().draw_mermaid_png(output_file_path="./pic.png")

