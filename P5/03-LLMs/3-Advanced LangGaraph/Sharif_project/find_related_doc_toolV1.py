from langchain_core.documents import Document
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

# Step 1: Define your known docs
docs_summary = [
    {"file_name": "Zahra Amini", "file_path": r"/mnt/Data1/Python_Projects/Datasets/Sharif_Data/Data/Zahra_Amini.md"},
    {"file_name": "Amirhosein Kermanshah", "file_path": r"/mnt/Data1/Python_Projects/Datasets/Sharif_Data/Data/Amirhossein_Kermanshah.md"},
    {"file_name": "Mohammad Sabouri", "file_path": r"/mnt/Data1/Python_Projects/Datasets/Sharif_Data/Data/Mohammad_Sabouri.md"},
    {"file_name": "Nader Tabatabaee", "file_path": r"/mnt/Data1/Python_Projects/Datasets/Sharif_Data/Data/Nader_Tabatabaee.md"},
    {"file_name": "Yousef Shafahi", "file_path": r"/mnt/Data1/Python_Projects/Datasets/Sharif_Data/Data/Yousef_Shafahi.md"}]

def ingest_documents(docs):
    docs_to_store = []

    for doc_info in docs_summary:
        file_path = doc_info["file_path"]
        file_name = doc_info["file_name"]

        # Create a minimal "representative" text for vector search
        # Could be file name, keywords, or a short summary you generate later
        text_repr = f"Profile of {file_name}, professor at Sharif University."

        # Store only the metadata we want
        metadata = {
            "file_path": file_path,
            "file_name": file_name,
            "keywords": ["professor", "Sharif University"]  # You can expand this
        }

        docs_to_store.append(Document(page_content=text_repr, metadata=metadata))

    vector_store = PineconeVectorStore.from_documents(
        docs_to_store,
        embedding=OpenAIEmbeddings(),
        index_name="sharifd"
    )
    print(f"[INFO] Data stored.")

def retriever_maker():
    retriever = PineconeVectorStore(index_name="sharifd", embedding=OpenAIEmbeddings()).as_retriever(search_kwargs={"k": 1})
    return retriever

# ingest_documents(docs_summary)


