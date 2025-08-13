from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState, StateGraph, START, END
from node import run_agent_reasoning, tool_node


def should_continue(state:MessagesState) -> str:
    if not state["messages"][LAST].tool_calls:
        return END
    return ACT

AGENT_REASON = "agent_reason"
ACT = "act"
LAST = -1

flow = StateGraph(MessagesState)
flow.add_node(AGENT_REASON, run_agent_reasoning)
flow.add_node(ACT, tool_node)

flow.add_edge(START, AGENT_REASON)
flow.add_conditional_edges(AGENT_REASON, should_continue, {END:END, ACT:ACT})
flow.add_edge(ACT, AGENT_REASON)

graph = flow.compile()
graph.get_graph().draw_mermaid_png(output_file_path="./pic.png")

if __name__ == "__main__":
    print("React with langgraph")
    res = graph.invoke({"messages": [HumanMessage(content="What is the weather in Tokyo? List it and then triple it.")]})
    print(res["messages"][LAST].content)