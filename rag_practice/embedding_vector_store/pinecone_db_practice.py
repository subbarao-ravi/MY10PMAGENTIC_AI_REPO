from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv,find_dotenv
import os
from pathlib import Path
from uuid import uuid4
from rag_practice.database_practice.pineconedb import PineCone_DB
import hashlib

load_dotenv(find_dotenv())

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview"
)

dimension = len(embeddings.embed_query("Hello"))
pinecone_api_key = os.getenv("PINECONE-API-KEY")

if not pinecone_api_key:
    raise ValueError("PINECONE_API_KEY is missing")

pineCone_DB = PineCone_DB(
                dimension=dimension,
                embeddings=embeddings
            )

index = pineCone_DB.getPineConeIndex(pinecone_api_key)
print(type(index))

vector_store = pineCone_DB.pineConeVectorStore(index=index)

# 8. Create documents
# ---------------------------------------------------

documents = [
    Document(
        page_content=(
            "I had chocolate chip pancakes and "
            "scrambled eggs for breakfast this morning."
        ),
        metadata={"source": "tweet"},
    ),
    Document(
        page_content=(
            "The weather forecast for tomorrow is cloudy "
            "and overcast, with a high of 62 degrees."
        ),
        metadata={"source": "news"},
    ),
    Document(
        page_content=(
            "Building an exciting new project with "
            "LangChain - come check it out!"
        ),
        metadata={"source": "tweet"},
    ),
    Document(
        page_content=(
            "Robbers broke into the city bank and "
            "stole $1 million in cash."
        ),
        metadata={"source": "news"},
    ),
    Document(
        page_content=(
            "LangGraph is the best framework for building "
            "stateful, agentic applications!"
        ),
        metadata={"source": "tweet"},
    ),
]

def make_id(doc) -> str:
    source = doc.metadata.get("source", "")
    text = source + "\n" + doc.page_content
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
# always gives same id with same content if executes multiple times
ids = [make_id(doc) for doc in documents] #[str(uuid4()) for _ in documents]#
print("ids ",ids)
inserted_ids = vector_store.add_documents(documents=documents, ids=ids)
print("inserted_ids ",inserted_ids)

results = vector_store.similarity_search(
    query=(
        "Langchain provides abstractions "
        "for working with LLMs"
    ),
    k=4,
    filter={
        "source" : "tweet"
    }
)

for result in results:
    print(result.page_content)
    print(result.metadata)


retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={
        "k": 1,
        "score_threshold": 0.4,
        "filter": {
            "source": "news"
        }
    }
)

retrieved_docs = retriever.invoke(
    "Stealing money from a bank is a crime"
)

print("retrieved_docs ",retrieved_docs)

retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={
        "k": 4,
        "score_threshold": 0.4,
        "filter": {"source": "tweet"},
    },
)

docs = retriever.invoke("LangChain provides abstractions for working with LLMs")
print(docs)