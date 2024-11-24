import bs4
from dotenv import load_dotenv
from langchain import hub
from operator import itemgetter
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from utils import format_qa_pair, format_qa_pairs
from colorama import Fore
from Models_name import groq_models

load_dotenv()

llm = ChatGroq(model=groq_models["Meta"][1], temperature=0.7)

loader = WebBaseLoader("http")