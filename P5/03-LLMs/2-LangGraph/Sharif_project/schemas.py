from typing import List
from pydantic import BaseModel, Field

class Search_Docs(BaseModel):
    """Search text files for query."""
    answer: str = Field(description="Answer to the question.")
    search_queries: List[str] = Field(description="All the related documents to the question")