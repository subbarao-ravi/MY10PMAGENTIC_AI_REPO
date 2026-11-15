from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
import faiss #Facebook AI Similarity Search
from langchain_community.docstore.in_memory import InMemoryDocstore
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
from langchain_core.documents import Document
from pathlib import Path
from dotenv import load_dotenv , find_dotenv
from rag_practice.loaders_practice.custom_text_loader import SimpleTextLoader
from rag_practice.splitters_practice.textsplitters import CustomRecursiveCharTextSplitter
from rag_practice.database_practice.faissdb import FAISS_DB

load_dotenv(find_dotenv(), override=True)

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

base_dir = Path(__file__).resolve().parent.parent / "LoaderDocs"
print('base_dir', base_dir)

textLoader = SimpleTextLoader(base_dir=base_dir)
documents = textLoader.load()

splitter = CustomRecursiveCharTextSplitter(
                    chunk_size=550,
                    chunk_overlap=50,
                    documents=documents
            )

recursiveChunks = splitter.getRecursiveChunks
print(f"total chunks  {len(recursiveChunks)}")

for index , document in enumerate(recursiveChunks, start=  1):
      print(f"chunk: {index}", f" content={document.page_content}", f"length={len(document.page_content)}")


faissdb = FAISS_DB(
    search_type="similarity",
    documents=recursiveChunks,
    embeddings=embeddings,
    search_kwargs={"k":1}
)

asretriver = faissdb.getVectorStoreRetriver

query = input("enter user query ")
retrivedDocs = asretriver.invoke(input=query)
print(f"Retrived {len(retrivedDocs)} documents ")

for docno, document in enumerate(retrivedDocs, start = 1):
    print('doc no ',docno, 'content ', document.page_content)

if __name__ == "__main__":
        documents=["Washington is the capital of USA",
           "Donald Trump is a president of USA",
           "Narendra Modi is a prime minister of India."]

        query = "who is the prime minister of India"

        doccontent = [Document(page_content=t) for t in documents]

        embedding_docs = embeddings.embed_documents(documents)
        embedded_query = embeddings.embed_query(query)
        print(len(embedded_query))


        ndArray = cosine_similarity([embedded_query], embedding_docs)
        print('cosine_similarity', ndArray)

        ndArray = euclidean_distances([embedded_query], embedding_docs)
        print('euclidean_distances ',ndArray)

        index = faiss.IndexFlatL2(3072)

        faissdb = FAISS_DB(
                search_type="similarity",
                documents=doccontent,
                embeddings=embeddings,
                search_kwargs={"k":1}
        )

        vectorStoreRetriver = faissdb.getManualSetupRetriver

        # docstore_Id = vector_Store.index_to_docstore_id[0]
        # print('docstore_Id ',docstore_Id)
        # print('---',vector_Store.index_to_docstore_id)
        # print('====',vector_Store.docstore.search(docstore_Id))
        documents = vectorStoreRetriver.invoke(input=query)
        print(documents)




