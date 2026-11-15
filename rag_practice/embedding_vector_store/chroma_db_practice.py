from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from pathlib import Path
import shutil
from dotenv import load_dotenv , find_dotenv
from rag_practice.loaders_practice.custom_text_loader import SimpleTextLoader
from rag_practice.splitters_practice.textsplitters import CustomRecursiveCharTextSplitter
from rag_practice.database_practice.chromadb import ChromaDB
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv(find_dotenv(), override=True)

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview",
    timeout=60,
    max_retries=2
)

base_dir = Path(__file__).resolve().parent.parent / "LoaderDocs"
print(f"basedir : {base_dir}")
textLoader = SimpleTextLoader(
    base_dir=base_dir
)

textDocuments = textLoader.load()
splitter = CustomRecursiveCharTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    documents=textDocuments
)

chunkList = splitter.getRecursiveChunks

persist_directory = Path(__file__).resolve().parent.parent / "VectorDB"
persist_directory.mkdir(exist_ok=True)
print('persist_directory ',persist_directory)

chromaDB = ChromaDB(
    documents=chunkList,
    persistance_directory=persist_directory,
    embeddings=embedding,
    collection_name="vectordb_practice"
)

chroma_store = chromaDB.retriveChromaStore()
vectorStoreRetriever = chromaDB.chromaRetriver(chroma_store, 4, "similarity")

query = "How do I reset my password"
# similarity_documents = vector_store.similarity_search(
#                     query=query,
#                     k=2
#                 )

similarity_documents = vectorStoreRetriever.invoke(query)

print(f"Loaded {len(similarity_documents)} search results ")
print("*******results with similarity search******")
for result , document in enumerate(similarity_documents, start=1):
    print(f"document {result}", f"answer : {document.page_content}")
    print()

print("--------------------------mmr results------------------------------------")

mmrRetriever = chromaDB.chromaRetriverWithMMR(chroma_store, 4, "mmr")

query = "How do I reset my password"

mmrRetriever_documents = mmrRetriever.invoke(query)

print(f"Loaded {len(mmrRetriever_documents)} mmr search results ")

for result , document in enumerate(mmrRetriever_documents, start=1):
    print(f"document {result}", f"answer : {document.page_content}")