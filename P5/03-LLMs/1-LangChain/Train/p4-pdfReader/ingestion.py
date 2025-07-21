from dotenv import load_dotenv
load_dotenv()

from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_openai import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path
import faiss


file_path = Path(r"/mnt/Data1/Python_Projects/Pure-Python/P5/03-LLMs/1-LangChain/Train/p4-pdfReader/files")

loader = PyPDFLoader(file_path=file_path/"Molnar-interpretable-machine-learning_compressed.pdf")
document = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = splitter.split_documents(document)

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))
vector_store = FAISS(embedding_function=embeddings,
                     index=index,
                     docstore=InMemoryDocstore(),
                     index_to_docstore_id={})

vector_store.add_documents(docs)
retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 1})

query = "What is PDP?"
result = retriever.invoke(query)
for r in result:
    print(r.page_content)