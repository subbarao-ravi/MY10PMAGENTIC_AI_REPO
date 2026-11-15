from pathlib import Path
from langchain_core.documents import Document
from langchain_core.document_loaders import BaseLoader
from typing import Iterator
import csv

class CustomCSVLoader(BaseLoader):
    def __init__(self, base_dir : Path, encoding:str='utf-8'):
        self.base_dir = base_dir
        self.encoding = encoding

    def lazy_load(self) -> Iterator[Document]:
        for file in sorted(self.base_dir.glob("*.csv")):
            if not file.is_file():
                continue
            #with file.open(newline="", encoding=self.encoding) as f:
            yield from self._load_csv(file=file)
           

    def _load_csv(self, file : Path):
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
if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent / "LoaderDocs"
    loader = CustomCSVLoader(base_dir)
    documents = loader.load()
    print(f"Loaded {len(documents)} documents")
    for row, document in enumerate(documents,start=1):
        print('index:',row, 'text:',document.page_content)