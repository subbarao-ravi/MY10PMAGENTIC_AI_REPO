from langchain_core.documents import Document
from pathlib import Path
from typing import Iterator
from langchain_core.document_loaders import BaseLoader
from rag_practice.loaders_practice.custom_text_loader import SimpleTextLoader
from rag_practice.loaders_practice.custom_csv_loader import CustomCSVLoader
from rag_practice.loaders_practice.custom_pdf_loader import CustomPDFLoader


class UniversalLoader(BaseLoader):
    def __init__(self, base_dir : Path, recursive : bool=False, extra_metadata : dict | None = {}, encoding:str='utf-8'):
        self.base_dir = base_dir
        self.encoding = encoding
        self.recursive = recursive
        self.extra_metadata = extra_metadata
        textLoader = SimpleTextLoader(base_dir=base_dir)
        csvLoader = CustomCSVLoader(base_dir=base_dir)
        pdfLoader = CustomPDFLoader(base_dir=base_dir)
        self.handlers = {
            ".txt" : textLoader._load_txt,
            ".csv" : csvLoader._load_csv,
            ".pdf" : pdfLoader._load_pdf
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

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent / "LoaderDocs"
    loader = UniversalLoader(base_dir=base_dir)
    documents = loader.load()
    print(f"Loaded {len(documents)} documents")