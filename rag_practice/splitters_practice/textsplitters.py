from pathlib import Path
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)
from langchain_core.documents import Document
from rag_practice.loaders_practice.custom_text_loader import SimpleTextLoader


class CustomCharacterTextSplitter:
    def __init__(self, chunk_size:int, chunk_overlap:int, documents : list[Document], separator:str="\n\n"):
        self.separator = separator
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.documents = documents

    @property
    def getChunks(self) -> list[Document]:
        splitter = CharacterTextSplitter(
                separator = self.separator,
                chunk_size= self.chunk_size,
                chunk_overlap = self.chunk_overlap,
                strip_whitespace=True
        )
        docChunks = splitter.split_documents(documents=self.documents)
        return docChunks


class CustomRecursiveCharTextSplitter:
    def __init__(self, chunk_size:int, chunk_overlap:int, documents : list[Document], 
                 separators:list[str] = ["\n\n", "\n", " ", ""]):
        self.separators = separators
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.documents = documents


    @property
    def getRecursiveChunks(self) -> list[Document]:
            splitter = RecursiveCharacterTextSplitter(
                    separators = self.separators,
                    chunk_size= self.chunk_size,
                    chunk_overlap = self.chunk_overlap
            )
            recursiveChunks = splitter.split_documents(documents=self.documents)
            return recursiveChunks

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent / "LoaderDocs"
    textLoader = SimpleTextLoader(base_dir=base_dir)
    documents = textLoader.load()
    print(f"Loaded {len(documents)} documents ")

    splitter = CharacterTextSplitter(
        separator = "\n\n",
        chunk_size=20,
        chunk_overlap = 10,
        strip_whitespace=True
    )

    docChunks = splitter.split_documents(documents=documents)
    print(f"created {len(docChunks)} chunks ")
    for index , document in enumerate(docChunks, start=1):
        print('chunk ', index, 'content ',document.page_content)

