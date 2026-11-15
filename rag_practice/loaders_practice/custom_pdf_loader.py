from pathlib import Path
from langchain_core.documents import Document
from langchain_core.document_loaders import BaseLoader
from typing import Iterator
from pypdf import PdfReader, PdfWriter

class CustomPDFLoader(BaseLoader):
    def __init__(self, base_dir : Path, encoding : str="utf-8"):
        self.base_dir = base_dir
        self.encoding = encoding

    def lazy_load(self) -> Iterator[Document]:
        for file in sorted(self.base_dir.glob("*.pdf")):
            if not file.is_file():
                continue
            yield from self._load_pdf(file=file)

            
    def _load_pdf(self, file : Path):
        reader = PdfReader(file)
        pdf_metadata = {k.lstrip("/"): v for k, v in (reader.metadata or {}).items()}
        for pageno, page in enumerate(reader.pages):
            yield Document(
                page_content=page.extract_text(),
                metadata={
                    "source":str(file),
                    "page":pageno,
                    **pdf_metadata
                }
            )

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent / "LoaderDocs"
    print('base_dir ',base_dir)
    loader = CustomPDFLoader(base_dir)
    documents = loader.load()
    print(f"Loaded {len(documents)} documents")