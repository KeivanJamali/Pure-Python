import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

def ingest_docs():
    raw_document = []
    doc_path = r"/mnt/Data1/Python_Projects/Pure-Python/P5/03-LLMs/1-LangChain/Train/p2/Docs"
    for file_name in os.listdir(doc_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(doc_path, file_name)
            loader = TextLoader(file_path, encoding="utf-8")
            docs = loader.load()
            raw_document += docs
    print(f"[INFO] loaded {len(raw_document)} documents")
    text_splitter = RecursiveCharacterTextSplitter(separators=["---"], chunk_size=500, chunk_overlap=100)
    documents = text_splitter.split_documents(raw_document)
    print(f"[INFO] we are going to add {len(documents)} to Pinecone")
    PineconeVectorStore.from_documents(documents=documents,
                                       embedding=embeddings,
                                       index_name="kpg")
    print(f"[INFO] Everything is done. Good job.")



if __name__ == "__main__":
    ingest_docs()

