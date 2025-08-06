from typing import Sequence, List
from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph
from chains import generate_chain, reflection_chain

def generation_node(state: Sequence[BaseMessage]):
    return generate_chain.invoke({"messages": state})

def reflection_node(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    res = reflection_chain.invoke({"messages": messages})
    return [HumanMessage(content=res.content)]

builder = MessageGraph()
builder.add_node("generation", generation_node)
builder.add_node("reflection", reflection_node)
builder.set_entry_point("generation")

def should_continue(state: Sequence[BaseMessage]):
    if len(state) > 6:
        return "finish"
    else:
        return "continue"
    
builder.add_conditional_edges("generation", should_continue, {"finish":END, "continue":"reflection"})
builder.add_edge("reflection", "generation")

graph = builder.compile()
# graph.get_graph().draw_mermaid_png(output_file_path=r"/mnt/Data1/Python_Projects/Pure-Python/P5/03-LLMs/2-LangGraph/Part_2/flow.png")
# graph.get_graph().print_ascii()

if __name__ == "__main__":
    print("Hello langgraph")
    inputs = HumanMessage(content=
                          """Make this tweet better:
                          @langChainAI
                          -newly tool calling feature is seriously underrated.
                          after a long wait, it's here- making the implementation of agents across different nodels with function calling - super easy.
                          mode a video covering their newest blog post.""")
    graph.invoke(inputs)