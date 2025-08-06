from dotenv import load_dotenv
load_dotenv()
from langgraph.graph import START, END, StateGraph
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from langchain_core.tools import StructuredTool
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.prebuilt import ToolNode


def calculator(query: str) -> str:
    """Calculate the query if it is a math problem."""
    return str(eval(query))

class State(TypedDict):
    math: Annotated[list, add_messages]

prompt = ChatPromptTemplate([("system", "Get the user query and extract the final formula that it is trying to find the answer of."),
                             ("user", "what is 2 + 5 * 7? please help me with this."),
                             ("assistant", "2 + 5 * 7")])

llm = init_chat_model(model="openai:gpt-4.1-nano")

builder = StateGraph(State)
builder.add_node("thinking", llm)
builder.add_node("tools", ToolNode([StructuredTool.from_function(calculator, name="calculator")]))
builder.add_edge(START, "thinking")
builder.add_edge("thinking", "tools")
builder.add_edge("tools", END)

memory = InMemorySaver()

graph = builder.compile(checkpointer=memory)

graph.get_graph().draw_mermaid_png(output_file_path="./pic.png")
config = {"configurable": {"thread_id": id}}

res = graph.invoke({"what is the answer to 5 * 5 * 5 - 5?"}, config=config)

print(res["messages"])