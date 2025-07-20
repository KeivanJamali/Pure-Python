from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
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
template = """You are a helpful assistant that should help the user.\n{output}\nuser:{query}\n"""
prompt = PromptTemplate(template=template,
                        input_variables=["query"],
                        input_types={"query": str},
                        partial_variables={"output": parser.get_format_instructions()},
                        metadata={"name": "city_json_gen",
                                  "description": "Generate city name and poplulation in json",
                                  "version": "0.0.1",
                                  "priority": "high"},
                        validate_template=True)

template = "Check if the the result is a valid json, if not fix it for me."
fix_prompt = PromptTemplate(template=template,
                            input_variables=[],
                            validate_template=True)

llm = ChatOpenAI(model="gpt-4.1-nano", temperature=0)
output_parser = OutputFixingParser.from_llm(llm=llm, parser=parser, max_retries=1, prompt=fix_prompt)
chain = prompt | llm | output_parser
response = chain.invoke(input={"query":"Generate a list of 5 cities and their populations"})
print(response)
# a = 'The output should be formatted as a JSON instance that conforms to the JSON schema below.\n\nAs an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}\nthe object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.\n\nHere is the output schema:\n```\n{"$defs": {"City": {"properties": {"name": {"title": "Name", "type": "string"}, "population": {"title": "Population", "type": "integer"}}, "required": ["name", "population"], "title": "City", "type": "object"}}, "properties": {"cities": {"items": {"$ref": "#/$defs/City"}, "title": "Cities", "type": "array"}}, "required": ["cities"]}\n```'
# print(len(a))
