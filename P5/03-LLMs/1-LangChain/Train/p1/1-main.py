from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

template = """You are a helpful assistant that generate python codes ONLY. No explaning or describing.\n{query}\n"""
prompt = PromptTemplate(template=template,
                        input_variables=["query"],
                        input_types={"query": str},
                        partial_variables={"garb": " and no garb"},
                        metadata={"name": "ptyhon_code_gen",
                                  "description": "Generate python code from query",
                                  "version": "0.0.1",
                                  "priority": "high"},
                        validate_template=True)

llm = ChatOpenAI(model="gpt-4.1-nano", temperature=0)
# print(prompt.format(query="how to import csv using pandas?"))
chain = prompt | llm
response = chain.invoke(input={"query":"how to read xcel files?"})
print(response.content)