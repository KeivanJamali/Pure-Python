from typing import List, Annotated
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field


class TranslationOutput(BaseModel):
    """Translate the text into English and specify what language it was before."""
    query: str = Field(description="The translated text in English.")
    language: str = Field(description="The original language name.")


class SearchTheWeb(BaseModel):
    queries: List[str] = Field(description="1 to 3 search queries for the web.")


class File(BaseModel):
    file_name: str = Field(description="Name of the file, e.g., 'professors_data.pdf'")
    file_path: str = Field(description="Absolute path to the file on disk.")


class SearchLocalDocs(BaseModel):
    queries: List[str] = Field(description="1 to 5 search queries for finding the related docs.")


class State(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]
