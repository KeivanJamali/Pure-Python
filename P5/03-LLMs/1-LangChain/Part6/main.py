from dotenv import load_dotenv
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_experimental.tools import PythonREPLTool
from langchain_experimental.agents import create_csv_agent

load_dotenv()

def main():
    print("start")
    instructions = """You are an agent designed to write and execute python code to answer questions.
    You have access to a python REPL, which you can use to execute python code.
    If you get an error, debug your code and try again.
    Only use the output of yout code to answer the question.
    You might know the answer without running any code, but you should still run the code to get the answer.
    If it does not seem like you can write code to answer the question, just return "I don't know" as the answer."""

    base_prompt = hub.pull("langchain-ai/react-agent-template")
    prompt = base_prompt.partial(instructions=instructions)

    tools = [PythonREPLTool()]
    agent = create_react_agent(
        prompt=prompt,
        llm=ChatOpenAI(temperature=0, model="gpt-4.1-nano"),
        tools=tools,
    )

    agent_executor = AgentExecutor(agent=agent, 
                                   tools=tools, 
                                   verbose=True,
                                   handle_parsing_errors=True)
    agent_executor.invoke({
        "input": """generate and save in current working directory 15 QRcodes
                        that point to www.udemy.com/course/langchain, you have qrcode package installed already"""
    })

    csv_agent = create_csv_agent(
        llm = ChatOpenAI(temperature=0, model="gpt-4.1-nano"),
        path="something.csv",
        verbose=True
    )
    csv_agent.invoke(
        input={"input": "how many columns is in the csv file?"}
    )

if __name__ == "__main__":
    main()