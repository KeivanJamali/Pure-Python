from langchain.agents import tool
from searchweb import search
from weatherdata import get_weather_information

@tool
def weather_tool(city_name: str) -> str:
    """Get the current weather information for a given city."""
    return get_weather_information(city_name)

@tool
def search_tool(query: str) -> str:
    """Search the internet using Tavily and return summarized results."""
    return search(query, n_result=3)