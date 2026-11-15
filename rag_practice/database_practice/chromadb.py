from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_core.vectorstores import VectorStoreRetriever
from pathlib import Path
import shutil


class ChromaDB:
    def __init__(self, documents : list[Document], embeddings : Embeddings, collection_name : str, persistance_directory:str):
        self.documents = documents
        self.embeddings = embeddings
        self.collection_name = collection_name
        self.persistance_directory = persistance_directory

    
    def retriveChromaStore(self):
        if self.persistance_directory.exists(): #and any(Path(self.persistance_directory).iterdir()):
            shutil.rmtree(
                self.persistance_directory,
                ignore_errors=True
            )
            # chroma_store = Chroma(
            #     collection_name=self.collection_name,
            #     persist_directory=self.persistance_directory,
            #     embedding_function=self.embeddings
            # )
            # print("Existing vector store loaded successfully.")
            # print(f'persisted at {self.persistance_directory}')
        # else :
            chroma_store = Chroma.from_documents(
                    documents=self.documents,
                    embedding=self.embeddings,
                    collection_name=self.collection_name,
                    persist_directory=self.persistance_directory,
                    collection_configuration={
                         # HNSW stands for Hierarchical Navigable Small World. 
                         # It’s the algorithm Chroma uses to find the nearest vectors quickly, 
                         # uses ANN stands for Approximate nearest neighbour
                         # without comparing your query against every stored vector.
                            "hnsw":{
                                "space":"cosine" #cosine distance
                            }
                    }
            )
            print('vector strore created successfully')
            print(f'stroed chunks : {len(self.documents)}')
            print(f'persisted at {self.persistance_directory}')
        return chroma_store

    def chromaRetriver(self , store : Chroma, k:int, search_type : str = "similarity") -> VectorStoreRetriever:
        return store.as_retriever(
            search_type = search_type,
            search_kwargs={
                "k":k
            }
        )

     # mmr stands for maximum mariginal relevance. 
     # a retrival strategy that balances two goals: 
        # 1. returning chunks that are relavant to the query
        # 2. returning chunks that are different from each other
    def chromaRetriverWithMMR(self , store : Chroma, k:int, search_type : str = "mmr") -> VectorStoreRetriever:
        return store.as_retriever(
            search_type = search_type,
            search_kwargs={
                "k":k, #final number of results
                "fetch_k":8, #candidate pool size
                "lambda_mult":0.7 #relevance vs diversity
            }
        )

