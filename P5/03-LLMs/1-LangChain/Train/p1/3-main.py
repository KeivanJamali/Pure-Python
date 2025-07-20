from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser, OutputFixingParser

load_dotenv()

class City(BaseModel):
    name: str
    population: int

class CityList(BaseModel):
    cities: list[City]

parser = PydanticOutputParser(pydantic_object=CityList)
prompt = ChatPromptTemplate([("system", "You are a helpful assistant that should help the user.\n {format_instructions}"),
                                        ("human", "Hello, how are you?"),
                                        ("ai", "I'm doing well, thanks!"),
                                        ("human", "That's good to hear."),
                                        ("ai", "OK"),
                                        MessagesPlaceholder("talk"),
                                        ("human", "{query}")],
                                        input_variables=["query", "talk"],
                                        partial_variables={"format_instructions": parser.get_format_instructions()},
                                        validate_template=True)

llm = ChatOpenAI(model="gpt-4.1-nano", temperature=0)
chain = prompt | llm
response = chain.invoke(input={"query":"name 4 cities and their populations and also tell me about them.",
                               "talk":[]})
print(response.content)
# a = 'The output should be formatted as a JSON instance that conforms to the JSON schema below.\n\nAs an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}\nthe object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.\n\nHere is the output schema:\n```\n{"$defs": {"City": {"properties": {"name": {"title": "Name", "type": "string"}, "population": {"title": "Population", "type": "integer"}}, "required": ["name", "population"], "title": "City", "type": "object"}}, "properties": {"cities": {"items": {"$ref": "#/$defs/City"}, "title": "Cities", "type": "array"}}, "required": ["cities"]}\n```'
# print(len(a))
