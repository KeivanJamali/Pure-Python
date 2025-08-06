from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel

class detect_language(BaseModel):
    query: str
    language: str

parser = PydanticOutputParser(pydantic_object=detect_language)
prompt_1 = ChatPromptTemplate([("system", "You are an expert English translator. You can translate any language to English.\n You should tanslate all the sentences to English and tell the language of the origin.\n\n{format_instructions}"),
                               ("human", "سلام. حال شما چطوره؟"),
                               ("ai", "{{'query': 'Hello. How are you?', 'language': 'Persian'}}"),
                               ("human", "The weather is very good today."),
                               ("ai", "{{'query': 'The weather is very good today.', 'language': 'English'}}"),
                               ("human", "{input}")],
                               input_variables=["input"],
                               partial_variables={"format_instructions": parser.get_format_instructions()},
                               metadata={"name": "translate_to_english"},
                               validate_template=True)

prompt_2 = ChatPromptTemplate([("system", "You are an expert English translator. You can translate English to any language."),
                               ("human", "Hello, how are you? -> Persian"),
                               ("ai", "سلام. حال شما چطور است؟"),
                               ("human", "It is so hot. -> English"),
                               ("ai", "It is so hot."),
                               ("human", "{query} -> {language}")],
                               input_variables=["query", "language"],
                               metadata={"name": "translate_to_language"},
                               validate_template=True)


prompt_3 = ChatPromptTemplate([("system", "")])