from dotenv import load_dotenv
load_dotenv()
from typing import List, Dict
from langchain_tavily import TavilySearch
from find_related_doc_toolV1 import retriever_maker
from pathlib import Path

tavily_tool = TavilySearch(max_result=5)

def search_web(queries: List[str]) -> List[str]:
    """search for some queries"""
    return tavily_tool.batch([{"query": query} for query in queries])

def extract_related_files(queries: List[str]) -> str:
    """Find the related documents about some queries and return them as list of doc_name, doc_path and doc_content."""
    retriever = retriever_maker()
    print(f"[INFO] Retriver is ready now !!!")
    file_paths = []
    related_docs = []
    i = 0
    for query in queries:
        i += 1
        print("[INFO] Search for the doc...")
        res = retriever.invoke(query)
        file_paths.append(res[0].metadata["file_path"])
        print(f"[INFO] Found {i}")
    
    for path in file_paths:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            related_docs.append(content)

    return "\n\n".join(related_docs)

# queries = ["prof.Amini"]
# result = extract_related_files(queries)

# print(result)