from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

@tool
def triple(num: float) -> float:
    """Triples the input number.

    Args:
        num (float): The number to triple.

    Returns:
        float: The tripled value.
    """
    return float(num) * 3

@tool
def search_tool(query: str) -> str:
    """Searches the web for the given query using Tavily.

    Args:
        query (str): The search query.

    Returns:
        str: The search results.
    """
    search = TavilySearch(max_results=1)
    results = search.invoke(query)
    return results

tools = [triple, search_tool]

llm = ChatOpenAI(model="gpt-4.1-nano",
                 temperature=0)
llm = llm.bind_tools(tools)
