from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel


prompt_1 = ChatPromptTemplate([("system", """You are a helpful assistant which have access to search tool and get weather info tool.
You can help people to decide where to go and give them a travel plan."""),
                               ("human", "{query}")],
                               input_variables=["query"],
                               metadata={"name": "Travel Planner"},
                               validate_template=True)


prompt = [prompt_1]