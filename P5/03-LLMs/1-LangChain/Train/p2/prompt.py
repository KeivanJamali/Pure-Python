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
prompt_2 = ChatPromptTemplate([("system", """You sould check if data is related to the question or not.\n
                                             Your answer should only be a boolean value."""),
                               ("human", """who is keivan jamali?
                                            data: how funny was last night, I really enjoyed to be with keivan."""),
                               ("ai", "1"),
                               ("human", """who is keivan jamali?
                                            data: I think reading books is a good habit."""),
                               ("ai", "0"),
                               ("human", "{query}\n\n{context}")],
                               input_variables=["query", "context"],
                               metadata={"name": "check_retrieved_data"},
                               validate_template=True)
prompt_3 = ChatPromptTemplate([("system", """Your name is KPG. A person with a strong personality and charisma.
                                             If the user asks you a question or wanted to talk to you, you should answer it respectfully. Try to motivate the user to know about Keivan Jamali.
                                             Here is some data that may help you to answer the user. read the data carefully and use your brain to find some conceptual relations between the data and the question if you can.
                                             If the data is not related to the question, just say 'I don't know'.
                                             {data}"""),
                                MessagesPlaceholder("context"),
                               ("human", "{query}")],
                               input_variables=["query", "data", "context"],
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
prompt_5 = ChatPromptTemplate([("system", """1. Rewrite the question so it explicitly refers to the subject mentioned in [data] (e.g., use the person's name instead of pronouns).
                                             2. If the question contains vague or general words (like "resume," "bio," "work," or "things"), expand them into a few related terms or synonyms (e.g., "resume" → "resume / abilities / projects").
                                             3. Output only the rewritten question."""),
                               ("human", """Hey there! I’m Keivan Jamali, hailing from the timeless city of Yazd, Iran. Yazd’s ancient vibes are my roots, and right now, I’m diving deep into the world of Civil Engineering at Sharif University – yep, the top-notch place for engineering in Iran. I’ve got this thing for programming too, especially machine learning. I’m no Python wizard (yet!), but I get by, and I’ve dabbled in HTML and CSS for some design fun. This website? One of my brainchildren, crafted with a bit of WordPress magic.\n what can he do?"""),
                               ("ai", "What can Keivan Jamali do / what are his abilities / skills / projects?"),
                               ("human", "[data]:\n{history}\n\n\nquestion:\n{query}")],
                               input_variables=["query", "history"],
                               metadata={"name": "rewrite_query"},
                               validate_template=True)

prompt = [prompt_1, prompt_2, prompt_3, prompt_4, prompt_5]
