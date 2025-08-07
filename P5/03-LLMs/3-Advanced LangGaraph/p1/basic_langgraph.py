from dotenv import load_dotenv
load_dotenv()
from typing import List, Annotated
from typing_extensions import TypedDict
from langgraph.graph import START, END, MessageGraph, StateGraph
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage, ToolMessage, AIMessage
from langchain_core.tools import StructuredTool
from langgraph.prebuilt import ToolNode
from pydantic import BaseModel, Field
from langchain_tavily import TavilySearch

class State(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]

class Extract_Math(BaseModel):
    math: str = Field(description="Only the math problem that should be solved.")

class Search_Query(BaseModel):
    search_queries: List[str] = Field(description="1 to 3 queries to be searched if you like as a list of str.")

def calculator(math: str) -> str:
    """Calculate the query if it is a math problem."""
    return str(eval(math))

def search_web(search_queries: List[str]) -> List[str]:
    """search for some queries"""
    return tavily_search.batch([{"query": query} for query in search_queries])

def should_go_to_tool(state: List[BaseMessage]):
    last_msg = state["messages"][-1]
    if isinstance(last_msg, AIMessage) and last_msg.tool_calls:
        return "go_to_tools"
    return "pass"

def thinking_node(state: List[BaseMessage]):
    return {"messages" : llm_chain_thinker.invoke({"messages": state["messages"]})}

def talking_node(state: List[BaseMessage]):
    return {"messages" : llm_chain_talker.invoke({"messages": state["messages"]})}

tavily_search = TavilySearch(max_result=5)

prompt_thinker = ChatPromptTemplate([("system", """You are a helpfull assistant.
                              Get the user query and then decide on one of these: 'answering on your own', 'using the calculator tool to get the answer', 'use the search tool to connect to internet and search for the answer'"""),
                             MessagesPlaceholder(variable_name="messages")],
                             input_variable=["messages"],
                             validate_template=True,
                             meta_data={"name":"thinker to find the next node."})

prompt_talker = ChatPromptTemplate([("system", "You will recieve a question and the result of tool usage. Answer the question using the information in the tools."),
                             MessagesPlaceholder(variable_name="messages")],
                             input_variable=["messages"],
                             validate_template=True,
                             meta_data={"name":"Write the answer using tool's data"})

llm = init_chat_model(model="openai:gpt-4.1-nano", temperature=0)
llm_chain_thinker = prompt_thinker | llm.bind_tools([Extract_Math, Search_Query])
llm_chain_talker = prompt_talker | llm
toolnode = ToolNode([StructuredTool.from_function(calculator, name=Extract_Math.__name__),
                     StructuredTool.from_function(search_web, name=Search_Query.__name__)])

builder = StateGraph(State)

builder.add_node("thinking", thinking_node)
builder.add_node("tools", toolnode)
builder.add_node("talker", talking_node)

builder.add_edge(START, "thinking")
builder.add_conditional_edges("thinking", should_go_to_tool, {"go_to_tools": "tools",
                                                              "pass": END})
builder.add_edge("tools", "talker")
builder.add_edge("talker", END)

memory = InMemorySaver()
graph = builder.compile(checkpointer=memory)
graph.get_graph().draw_mermaid_png(output_file_path="./pic.png")
config = {"configurable": {"thread_id": 1}}

res1 = graph.invoke({"messages": "what is the answer to 5 * 5 * 5 - 5?"}, config=config)
res2 = graph.invoke({"messages": "What was the last message I sent?"}, config=config)
res3 = graph.invoke({"messages": "Can you tell me a bit about Keivan Jamali, some civil engineer guy, studied at Sharif University?"}, config=config)


print(res1["messages"][-1].content)
print(res2["messages"][-1].content)
print(res3["messages"][-1].content)