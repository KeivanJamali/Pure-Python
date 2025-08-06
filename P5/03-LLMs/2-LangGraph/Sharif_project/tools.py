from typing import List
from langchain_core.tools import StructuredTool
from schemas import Search_Docs

def search_deep(query : str, **kwargs):
    """Find related documents."""
    pass


tools = [StructuredTool.from_function(search_deep, name="search_queries")]