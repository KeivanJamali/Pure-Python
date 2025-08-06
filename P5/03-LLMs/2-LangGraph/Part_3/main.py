from dotenv import load_dotenv
load_dotenv()

from typing import List
from langchain_core.messages import BaseMessage, ToolMessage
from langgraph.graph import END, MessageGraph
from chain import revisor, first_responder
from tool_exxecutor import execute_tools

max_iteration = 2
builder = MessageGraph()
builder.add_node("draft", first_responder)
builder.set_entry_point("draft")
builder.add_node("execute_tools", execute_tools)
builder.add_node("revisor", revisor)
builder.add_edge("draft", "execute_tools")
builder.add_edge("execute_tools", "revisor")

def event_loop(state: List[BaseMessage]) -> str:
    count_tool_visit = sum(isinstance(item, ToolMessage) for item in state)
    if count_tool_visit < max_iteration:
        return "continue"
    else:
        return "done"

builder.add_conditional_edges("revisor", event_loop, {"continue": "execute_tools",
                                                      "done": END})
graph = builder.compile()
graph.get_graph().draw_mermaid_png(output_file_path="/mnt/Data1/Python_Projects/Pure-Python/P5/03-LLMs/2-LangGraph/Part_3/flow.png")

if __name__ == "__main__":
    print("Hello reflexion agent")
    res = graph.invoke("Write about usecase of LLMs in Transportation engineering field.")
    print(res[-1].tool_calls[0]["args"]["answer"])