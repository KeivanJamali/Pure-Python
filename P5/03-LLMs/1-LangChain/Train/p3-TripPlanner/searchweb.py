from dotenv import load_dotenv
load_dotenv()
import os
from langchain_tavily import TavilySearch


def search(query:str, n_result:int):
    tavily_tool = TavilySearch(max_results=n_result,
                               topic="general",
                               # include_answer=False,
                               # include_raw_content=False,
                               # include_images=False,
                               # include_image_descriptions=False,
                               # search_depth="basic",
                               # time_range="day",
                               # include_domains=None,
                               # exclude_domains=None
                               )
    result_tavily = tavily_tool.invoke(query)
    result = [result_tavily["results"][i]["content"] for i in range(n_result)]
    result_str = ""
    for i in range(len(result)):
        result_str += f"Website_{i+1}_result:\n{result[i]}\n\n"
    return result_str[:-1]
