from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


prompt_to_en = ChatPromptTemplate([("system", "You should only write the translated text in English, and writing the name of the original language in the requested format."),
                                   ("user", "{query}")],
                                    input_variables=["query"],
                                    validate_template=True,
                                    metadata={"name": "translate_to_EN"})

prompt_to_something = ChatPromptTemplate([("system", "You should ONLY wtire the translation of the next into language of {language}. Nothing else."),
                                          ("user", "{query}")],
                                          input_variables=["query", "language"],
                                          validate_template=True,
                                          metadata={"name": "translate_to_something"})

prompt_to_choose = ChatPromptTemplate([("system", """You are a helpful AI agent responsible for deciding how to handle a user query.
Your task is to decide the most appropriate action based on the content of the query.

You have access to the following options:
1. "Answer it on your own" — Use only your own knowledge to answer.
2. "Search the web for getting the answer" — When the query is about recent or external information.
3. "Search the local docs to find the answer" — When the query is about internal knowledge related to Sharif University of Technology (e.g., professors, environmental data, research, departments, etc.).
"""),
                                        MessagesPlaceholder(variable_name="messages")],
                                        input_variables=["messages"],
                                        validate_template=True,
                                        metadata={"name": "decide_on_tools"})

prompt_answer = ChatPromptTemplate([("system", "You have to answer the query using the information here\n{information}"),
                                    MessagesPlaceholder(variable_name="messages")],
                                    input_variables=["information", "messages"],
                                    validate_template=True,
                                    metadata={"name": "decide_on_tools"})
