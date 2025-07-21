from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel

class detect_language(BaseModel):
    query: str
    language: str

parser = PydanticOutputParser(pydantic_object=detect_language)
prompt_1 = ChatPromptTemplate([("system", "You are an expert English translator. You can translate any language to English.\n You should tanslate all the sentences to English and tell the language of the origin.\n{format_instructions}"),
                               ("human", "سلام. حال شما چطوره؟"),
                               ("ai", "{{'query': 'Hello. How are you?', 'language': 'Persian'}}"),
                               ("human", "The weather is very good today."),
                               ("ai", "{{'query': 'The weather is very good today.', 'language': 'English'}}"),
                               ("human", "{input}")],
                               input_variables=["input"],
                               partial_variables={"format_instructions": parser.get_format_instructions()},
                               metadata={"name": "translate_to_english"},
                               validate_template=True)
prompt_2 = ChatPromptTemplate([("system", """You sould check if data is related to the question or not.\nYour answer should only be a boolean value."""),
                               ("human", """who is keivan jamali?\ndata: how funny was last night, I really enjoyed to be with keivan."""),
                               ("ai", "1"),
                               ("human", """who is keivan jamali?\ndata: I think reading books is a good habit."""),
                               ("ai", "0"),
                               ("human", "{query}\n\n{context}")],
                               input_variables=["query", "context"],
                               metadata={"name": "check_retrieved_data"},
                               validate_template=True)
prompt_3 = ChatPromptTemplate([("system", """Your name is KPG. A person with a strong personality and charisma.
You have a tools. search_query tool will give you access to data only about Keivan Jamali. 
Instructions:
1. If the user asks about Keivan Jamali, use yout tool and search about that question in the search_query tool. If the returned data were not useful, say simply 'I don't know the answer to your question. sorry :('.
3. Try to motivate the user to know about Keivan Jamali."""),
                               ("human", "{query}")],
                               input_variables=["query"],
                               metadata={"name": "answer_question"},
                               validate_template=True)
prompt_4 = ChatPromptTemplate([("system", "You are an expert English translator. You can translate English to any language."),
                               ("human", "Hello, how are you? -> Persian"),
                               ("ai", "سلام. حال شما چطور است؟"),
                               ("human", "It is so hot. -> English"),
                               ("ai", "It is so hot."),
                               ("human", "{query} -> {language}")],
                               input_variables=["query", "language"],
                               metadata={"name": "translate_to_language"},
                               validate_template=True)


prompt = [prompt_1, prompt_2, prompt_3, prompt_4]
