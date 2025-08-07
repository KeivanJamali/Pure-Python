from dotenv import load_dotenv
load_dotenv()
from typing import List, Dict
from langchain_tavily import TavilySearch
from find_related_doc_tool import find_related_docs
from pathlib import Path

tavily_tool = TavilySearch(max_result=5)

def search_web(queries: List[str]) -> List[str]:
    """search for some queries"""
    return tavily_tool.batch([{"query": query} for query in queries])

def extract_related_files(queries: List[str]) -> List[Dict]:
    """Find the related documents about some queries and return them as list of doc_name, doc_path and doc_content."""
    docs = find_related_docs(queries=queries)
    extracted = []
    for doc in docs:
        doc = doc.model_dump()
        file_path = Path(doc["file_path"])
        try:
            content = file_path.read_text(encoding="utf-8")
        except:
            continue

        extracted.append({
            "file_name": doc["file_name"],
            # "file_path": doc["file_path"],
            "content": content
        })
    return extracted

# queries = ["prof.Amini", "environmental changes", "research labs in EE"]
# result = extract_related_files(queries)

# print(result)