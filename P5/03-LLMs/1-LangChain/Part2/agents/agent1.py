from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from tools.tools import load_search


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0,
                     model_name="gpt-4.1-nano",
                     openai_proxy="http://127.0.0.1:10808")
    template = """Given the full name {name_of_person} I want you to get it me a link which has the person information.
                    Your answer should contain only a URL"""
    prompt_template = PromptTemplate(template=template,
                                     input_variables=["name_of_person"])
    tools_for_agent = [Tool(name="Crawl google 3 website page",
                            func=load_search,
                            description="Useful for when you need to get related website URL to some data")]
    
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm,
                               tools=tools_for_agent,
                               prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent,
                                   tools=tools_for_agent,
                                   verbose=True)
    
    result = agent_executor.invoke(input={
        "input": prompt_template.format_prompt(name_of_person=name)
    })
    result_url = result["output"]
    return result_url 