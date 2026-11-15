from langchain_core.embeddings import Embeddings
import time
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone , ServerlessSpec
from pinecone.db_data.index import Index


class PineCone_DB:
    def __init__(self, dimension : int, embeddings:Embeddings, index_name="langchain-rag-index"):
        self.dimension = dimension
        self.embeddings = embeddings
        self.index_name = index_name


    def getPineConeIndex(self, pinecone_key) -> Index:
        pc = Pinecone(api_key=pinecone_key, additional_headers={"X-Pinecone-Api-Version": "2026-04"},)
        #pc.delete_index(self.index_name)
        if not pc.has_index(self.index_name):
                print("Going to create index ")
                pc.create_index(
                        name=self.index_name,
                        dimension=self.dimension,
                        metric="cosine",
                        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
                )

                #waiting for index readiness if index not created
                while True:
                    description = pc.describe_index(self.index_name)
                    print("description ",description)
                    if description.status["ready"]:
                            break
                    time.sleep(2)
        # connect to index
        index = pc.Index(self.index_name)
        print("Index connected:", self.index_name)
        return index

    def pineConeVectorStore(self, index):
         vector_store = PineconeVectorStore(
                    index=index,
                    embedding=self.embeddings,
                    namespace="pineconepractice"
                )
         return vector_store