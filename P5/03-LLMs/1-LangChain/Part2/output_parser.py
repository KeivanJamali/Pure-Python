from typing import List, Dict, Any
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class Summary(BaseModel):
    summary: str = Field(description="summary")
    facts: List[str] = Field(description="Interesting facts about them")

    def to_dict(self) -> Dict[str, Any]:
        return {"summary": self.summary, "facts":self.facts}
    
summary_parser = PydanticOutputParser(pydantic_object=Summary)