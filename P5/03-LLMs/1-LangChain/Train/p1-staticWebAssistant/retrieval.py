from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from prompts import prompt

embedding = OpenAIEmbeddings(model="text-embedding-3-small")
db = PineconeVectorStore(index_name="kpg", embedding=embedding)
retriever = db.as_retriever(search_type="mmr",
                            search_kwargs={"k": 5,
                                           "score_threshold": 0.75,
                                           "lambda_mult": 0.5})
llm = ChatOpenAI(model="gpt-4.1-nano", temperature=0)

def search_query(query: str) -> str:
    """Find and return information ONLY about **Keivan Jamali** nothing else.
    query: Only English string."""
    docs = retriever.invoke(query)
    chain = prompt[2] | llm

    relevance_docs = ""
    i = 1
    for idx, doc in enumerate(docs):
        doc_txt = doc.page_content
        binary_score = chain.invoke({"query": query, "context": doc_txt})
        binary_score = binary_score.content
        print(f"Keivan Document {idx + 1} relevance score: {binary_score}")
        if binary_score == "1" or binary_score.lower() == "true" or binary_score.lower() == "yes":
            relevance_docs += f"data_{i}: {doc_txt}\n\n"
            i += 1

    return relevance_docs
