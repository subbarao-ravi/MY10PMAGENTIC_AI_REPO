from pathlib import Path
from langchain_core.documents import Document
from langchain_core.document_loaders import BaseLoader
from typing import Iterator

class SimpleTextLoader(BaseLoader):
    def __init__(self, base_dir : Path, extra_metadata : dict | None = {}, encoding : str ='utf-8'):
        self.base_dir = base_dir
        self.encoding = encoding
        self.extra_metadata = extra_metadata or {}

    def lazy_load(self) -> Iterator[Document]:
        for file in sorted(self.base_dir.glob("*.txt")):
            if not file.is_file():
                continue
            yield from self._load_text(file=file)
            
    def _load_text(self, file : Path):
        yield Document(
            page_content=(file.read_text(encoding=self.encoding)),
            metadata = {
                "source" : str(file),
                "type":"text",
                "fileName": file.name,
                ** self.extra_metadata
            }
        )
if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent / "LoaderDocs"
    loader = SimpleTextLoader(base_dir, {"department":"learning"})
    documents = loader.load()
    print(f"Loaded {len(documents)} documents")
    for document in documents:
        print('pagecontent ', document.page_content, 'metadata ',document.metadata)