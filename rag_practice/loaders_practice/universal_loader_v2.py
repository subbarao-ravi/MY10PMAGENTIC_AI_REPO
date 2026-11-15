from collections.abc import Callable
from langchain_core.documents import Document
from pathlib import Path
from typing import Iterator
from langchain_core.document_loaders import BaseLoader
import csv
from pypdf import PdfReader

class UniversalLoader(BaseLoader):
    def __init__(self, base_dir : Path, recursive : bool=False, extra_metadata : dict | None = {}, encoding:str='utf-8'):
        self.base_dir = base_dir
        self.encoding = encoding
        self.recursive = recursive
        self.extra_metadata = extra_metadata
        self.handlers = {
            ".csv" : self._load_csv,
            ".txt" : self._load_txt,
            ".pdf" : self._load_pdf
        }

    def lazy_load(self) -> Iterator[Document]:
        if self.base_dir:
            if not self.base_dir.is_dir():
                raise FileNotFoundError(f"directory not found: {self.base_dir}")

            pattern = self.base_dir.rglob("*.*") if self.recursive else self.base_dir.glob("*.*")
            print('pattern ', pattern)
            for file in sorted(pattern):
                if not file.is_file():
                    continue

                handler = self.handlers.get(file.suffix.lower())
                print('file suffix ',file.suffix, 'hanlder ',handler)
                if handler is None:
                    continue
                yield from handler(file)

    def _load_csv(self, file : Path) -> Iterator[Document]:
            with open(file, newline="", encoding=self.encoding) as f:
                for index , row in enumerate(csv.DictReader(f)):
                    text = "\n".join (f"{key}: {value}" for key, value in row.items())
                    yield Document(
                        page_content= text,
                        metadata={
                            "source":str(file),
                            "fileName":file.name,
                            "row":index
                        }
                    )

    def _load_pdf(self, file : Path) -> Iterator[Document]:
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

    
    def _load_txt(self, file : Path) -> Iterator[Document]:
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
    loader = UniversalLoader(base_dir=base_dir)
    documents = loader.load()
    print(f"Loaded {len(documents)} documents")