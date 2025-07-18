import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

if __name__ == "__main__":
    print("ingesting...")
    loader = TextLoader(r"/mnt/Data1/Python_Projects/Pure-Python/P5/LLMs/1-LangChain/Part4/medium.txt")
    document = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=30)
    text = text_splitter.split_documents(document)
    embeddings = OpenAIEmbeddings(openai_api_type=os.environ.get("OPENAI_API_KEY"),
                                  model="text-embedding-3-small")
    PineconeVectorStore.from_documents(text,
                                       embeddings,
                                       index_name=os.environ["INDEX_NAME"])
    