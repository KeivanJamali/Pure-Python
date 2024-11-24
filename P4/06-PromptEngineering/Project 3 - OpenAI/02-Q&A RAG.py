from dotenv import load_dotenv

from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import os
from colorama import Fore

# Load env variables
load_dotenv()

# ============================Load The Model==============================
models = {"Google": ["gemma2-9b-it", "gemma-7b-it"],
          "Groq": ["llama3-groq-70b-8192-tool-use-preview", "llama3-groq-8b-8192-tool-use-preview"],
          "Meta": ["llama-3.1-70b-versatile", "llama-3.1-8b-instant", "llama-3.2-1b-preview", "llama-3.2-3b-preview", "llama-3.2-11b-vision-preview", "llama-3.2-90b-vision-preview", "llama-guard-3-8b", "llama3-70b-8192", "llama3-8b-8192"],
          "Mistral": ["mixtral-8x7b-32768"],
          "OpenAI": ["whisper-large-v3", "whisper-large-v3-turbo"]}
model_groq = ChatGroq(model=models["Meta"][0], temperature=0.7)


# ============================Prompt Template==============================
def prompt_generate():
    system_prompt_file_path = "D:/All Python/Pure-Python/P4/06-PromptEngineering/Project 2 - OpenAI/KeivanSystemPrompt.txt"
    system_prompt = SystemMessagePromptTemplate.from_template_file(system_prompt_file_path, input_variables={"context"})
    human_prompt = HumanMessagePromptTemplate.from_template(template="{question}")
    prompt = ChatPromptTemplate([system_prompt, human_prompt])
    return prompt

def load_document():
    """Load a file from path, split it into chunks, embed each chunk and load it into the vector store."""
    doc_path = "D:/All Python/Pure-Python/P4/06-PromptEngineering/Project 2 - OpenAI/KeivanJamali_doc"
    document = []
    for file_name in os.listdir(doc_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(doc_path, file_name)
            loader = TextLoader(file_path, encoding="utf-8")
            temp = loader.load()
            splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
            result = splitter.split_documents(temp)
            document += result
    return document

def load_embeddings(document):
    """Create a vectore store from a set of documents."""
    embeddings = HuggingFaceEmbeddings()
    db = Chroma.from_documents(document, embeddings)
    retriever = db.as_retriever()
    return retriever

def generate_response(retriever, query):
    """Generate a response using retriever and query."""
    chain = RetrievalQA.from_chain_type(llm=model_groq,
                                        chain_type="stuff",
                                        retriever=retriever,
                                        return_source_documents=True)
    return chain.invoke(query)

def query(query_, retriever):
    """Query the model and return the response"""
    response = generate_response(retriever, query_)
    return response

def start():
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
    documents = load_document()
    retriever = load_embeddings(documents)
    while True:
        user_input = input("Q: ")
        # Exit
        if user_input == "x":
            start()
        else:
            response = query(user_input, retriever)
            print(Fore.BLUE + f"A: " + response["result"] + Fore.RESET)
            print(Fore.WHITE + "\n-------------------------------------------------------")

if __name__ == "__main__":
    start()