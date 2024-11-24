from dotenv import load_dotenv

from langchain_community.chat_models import ChatOpenAI
from langchain_community.document_loaders import WebBaseLoader
from langchain.prompts import PromptTemplate
# from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

from langchain_ollama import ChatOllama
# from langchain_ollama import OllamaEmbeddings

from langchain_groq import ChatGroq

from langchain_huggingface import HuggingFaceEmbeddings

import os
from colorama import Fore

# Load env variables
load_dotenv()

# ============================API KEY==============================
# open_ai_api_path = "D:\\All Python\\GPTAPI.txt"
# with open(open_ai_api_path, "r") as file:
#     open_ai_api = file.read().strip()

# groq_api_path = "D:\\All Python\\GroqAPI.txt"
# with open(groq_api_path, "r") as file:
#     groq_api = file.read().strip()

# ============================Load The Model==============================
# model_gpt = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, max_tokens=10)
model_oll = ChatOllama(model="llama3.2:1b-instruct-q8_0", temperature=0.7)
models = {"Google": ["gemma2-9b-it", "gemma-7b-it"],
          "Groq": ["llama3-groq-70b-8192-tool-use-preview", "llama3-groq-8b-8192-tool-use-preview"],
          "Meta": ["llama-3.1-70b-versatile", "llama-3.1-8b-instant", "llama-3.2-1b-preview", "llama-3.2-3b-preview", "llama-3.2-11b-vision-preview", "llama-3.2-90b-vision-preview", "llama-guard-3-8b", "llama3-70b-8192", "llama3-8b-8192"],
          "Mistral": ["mixtral-8x7b-32768"],
          "OpenAI": ["whisper-large-v3", "whisper-large-v3-turbo"]}
model_groq = ChatGroq(model=models["Meta"][0], temperature=0.7)


# ============================Load The Document============================
loader = WebBaseLoader("https://keivanjamali.com/")
document = loader.load()

# ============================Prompt Template==============================
template = "You are a friendly helpful assistant. Your personality is like Steve Harvey. You will answer the {question} based on your knowledge based on {context}"
# template = """/
# You are a customer support specialist /
# question: {question}. You assist users with general inqueries based on {context} /
# and technical issues. /
# """

prompt = PromptTemplate(template=template, input_variables=["question", "context"])

# ========Retriever Load embeddings and create a vector store==============
# embeddings = OpenAIEmbeddings()
# embeddings = OllamaEmbeddings(model="llama3.2:1b-instruct-q8_0")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2",
                                   model_kwargs = {'device': 'cpu'},
                                   encode_kwargs = {'normalize_embeddings': False})
vector_store = FAISS.from_documents(documents=document, embedding=embeddings)

# ========Defind a function that generate the response==============
def generate(query):
    chain_kwargs = {"prompt": prompt}
    chain = RetrievalQA.from_chain_type(llm=model_groq,
                                        chain_type="stuff",
                                        retriever=vector_store.as_retriever(search_kwargs={"k": 1}), 
                                        chain_type_kwargs=chain_kwargs)
    response = chain.invoke(query)
    return response


def start():
    # print("OPENAI API KEY", os.getenv("OPENAI_API_KEY"))
    # print("documents", document)
    instructions = ("Type your question and press ENTER. Type 'x' to go back to the MAIN menu.\n")
    print(Fore.BLUE+"\n\x1B[3m" + instructions + "\x1B[0m" + Fore.RESET)

    print("MENU")
    print("====")
    print("[1]- Ask a question")
    print("[2]- Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        ask()
    elif choice == "2":
        print("Goodbye.")
        exit()
    else:
        print("Invalid choice.")
        start()


def ask():
    while True:
        user_input = input("Q: ")
        # Exit
        if user_input == "x":
            start()
        else:
            response = generate(user_input)
            print(Fore.BLUE + f"A: " + response["result"] + Fore.RESET)
            print(Fore.WHITE + "\n-------------------------------------------------------")

if __name__ == "__main__":
    start()