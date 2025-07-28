from dotenv import load_dotenv
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode
from react import llm, tools
from langchain_core.messages import SystemMessage

load_dotenv()

SYSTEM_MESSAGE = """
You are a helpful assistant that can use the following tools to answer questions.
"""

def run_agent_reasoning(state:MessagesState) -> MessagesState:
    """
    Runs the agent reasoning with the provided state.

    Args:
        state (MessagesState): The current state of the messages.

    Returns:
        MessagesState: The updated state after running the agent reasoning.
    """
    sys_msg = SystemMessage(content=SYSTEM_MESSAGE)
    response = llm.invoke([sys_msg] + state["messages"])
    return {"messages": state["messages"] + [response]}

tool_node = ToolNode(tools)
