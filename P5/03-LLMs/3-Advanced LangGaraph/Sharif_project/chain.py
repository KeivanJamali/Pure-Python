from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model
from prompts import *
from schema import TranslationOutput, SearchLocalDocs, SearchTheWeb


llm = init_chat_model(model="gpt-4.1-nano", temperature=0)
# chain_translate_en = prompt_to_en | llm.bind_tools([TranslationOutput], tool_choice=TranslationOutput.__name__)
chain_translate_en = prompt_to_en | llm.with_structured_output(TranslationOutput)
chain_translate_something = prompt_to_something | llm
chain_decide_on_tool = prompt_to_choose | llm.bind_tools([SearchLocalDocs, SearchTheWeb])
chain_to_answer = prompt_answer | llm


# res = chain_translate_en.invoke("سلام. خوبی؟")
# print(res.tool_calls[0]["args"]["query"])
# print(res.tool_calls[0]["args"]["language"])
# print()

# res = chain_translate_something.invoke({"query": "Hi. How are you?", "language": "Persian"})
# print(res.content)