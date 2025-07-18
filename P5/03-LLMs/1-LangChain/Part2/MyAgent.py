from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from agents.agent1 import lookup
from tools.tools import load_scrape
from output_parser import summary_parser
load_dotenv()

def program(name: str) -> str:
    link = lookup(name=name)
    print(link)
    data = load_scrape(url=link)

    summary_template = """
    given the information {information} about a person, I want you to create:
    1. a short summary.
    2. two interesting facts about him.
    \n{formated_instructions}
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], 
                                             template=summary_template,
                                             partial_variables={"formated_instructions":summary_parser.get_format_instructions()})

    # llm = ChatOpenAI(temperature=0, 
                    #  model="gpt-4.1-nano", 
                    #  openai_proxy="http://127.0.0.1:10808")
    llm = ChatOllama(model="deepseek-r1")
    chain = summary_prompt_template | llm | summary_parser

    res = chain.invoke(input={"information": data})

    print(res)
    return res

program("Keivan Jamali engineer")
