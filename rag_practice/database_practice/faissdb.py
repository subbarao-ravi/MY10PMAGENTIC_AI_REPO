from langchain_core.embeddings import Embeddings
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
import faiss

class FAISS_DB:
    def __init__(self, embeddings : Embeddings, documents : list[Document], 
                 search_type : str, search_kwargs={"k":1}, dimension : int = 3072):
        self.embeddings = embeddings
        self.documents = documents
        self.search_type = search_type
        self.search_kwargs = search_kwargs
        self.dimension = dimension

    '''FAISS Inmemorydocstore but automatic setup we no need to specify dimension it will take care off this internally'''
    @property
    def getVectorStoreRetriver(self):
        vector_store = FAISS.from_documents(
            documents=self.documents,
            embedding=self.embeddings
        )
        vectorStoreRetriver = vector_store.as_retriever(
            search_type =   self.search_type,
            search_kwargs = self.search_kwargs
        )
        return vectorStoreRetriver

    '''FAISS Inmemorydocstore with manual setup by passing dimensions explicitly with constructor approach'''
    @property
    def getManualSetupRetriver(self):
        index = faiss.IndexFlatL2(self.dimension)
        vector_Store = FAISS(
            embedding_function=self.embeddings,
            index=index,
            docstore= InMemoryDocstore(),
            index_to_docstore_id={}
        )
        docStoreIds = vector_Store.add_documents(self.documents)
        print("inmemory docstoreIds ",docStoreIds)

        vectorStoreRetriver = vector_Store.as_retriever(
            search_type =   self.search_type,
            search_kwargs = self.search_kwargs
        )
        return vectorStoreRetriver

    def getFaissLocalPersistant():
        pass
        