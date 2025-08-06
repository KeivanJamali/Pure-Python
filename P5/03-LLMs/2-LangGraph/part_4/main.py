from dotenv import load_dotenv
load_dotenv()
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from langgraph.graph import START, END, StateGraph

# defined a special dictionary
class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

llm = init_chat_model(model="openai:gpt-4.1-nano")
def chat_bot(state: State):
    return {"message": llm.invoke(state["messages"])}
graph_builder.add_node("chat", chat_bot)

graph_builder.add_edge(START, "chat")
graph_builder.add_edge("chat", END)

graph = graph_builder.compile()

from IPython.display import Image, display

display(Image(graph.get_graph().draw_mermaid_png()))
