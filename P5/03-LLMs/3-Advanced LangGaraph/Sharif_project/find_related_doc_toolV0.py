import re
from typing import List
from schema import File
from difflib import SequenceMatcher

# Step 1: Define your known docs
docs_summary = [
    {"file_name": "Zahra Amini", "file_path": r"/mnt/Data1/Python_Projects/Datasets/Sharif_Data/Data/Zahra_Amini.md"},
    {"file_name": "Amirhosein Kermanshah", "file_path": r"/mnt/Data1/Python_Projects/Datasets/Sharif_Data/Data/Amirhossein_Kermanshah.md"},
    {"file_name": "Mohammad Sabouri", "file_path": r"/mnt/Data1/Python_Projects/Datasets/Sharif_Data/Data/Mohammad_Sabouri.md"},
    {"file_name": "Nader Tabatabaee", "file_path": r"/mnt/Data1/Python_Projects/Datasets/Sharif_Data/Data/Nader_Tabatabaee.md"},
    {"file_name": "Yousef Shafahi", "file_path": r"/mnt/Data1/Python_Projects/Datasets/Sharif_Data/Data/Yousef_Shafahi.md"},
]

def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower())

def is_similar(a: str, b: str, threshold=0.6) -> bool:
    return SequenceMatcher(None, a, b).ratio() >= threshold

def find_related_docs(queries: List[str]) -> List[File]:
    related_files = []

    for query in queries:
        norm_query = normalize(query)
        # print(norm_query)

        for doc in docs_summary:
            norm_filename = normalize(doc["file_name"])
            # print(norm_filename)
            # Try strict keyword match or soft fuzzy match
            if any(word in norm_filename for word in norm_query.split()) or is_similar(norm_query, norm_filename):
                related_files.append(File(file_name=doc["file_name"], file_path=doc["file_path"]))

    # Remove duplicates
    unique_files = {f.file_path: f for f in related_files}.values()
    unique_files = list(unique_files)
    if unique_files:
        return unique_files
    else:
        return [File(file_name="not_found", file_path="not_found")]

