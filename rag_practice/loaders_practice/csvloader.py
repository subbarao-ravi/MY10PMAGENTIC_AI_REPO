from langchain_core.documents import Document
from langchain_community.document_loaders import CSVLoader
from pathlib import Path

base_dir = Path(__file__).resolve().parent / "LoaderDocs"
csv_path = base_dir / "sample_data.csv"

csvLoader = CSVLoader(
    file_path=csv_path,
    encoding='utf-8'
)

documents = csvLoader.load()
for row, document in enumerate(documents , start=1):
    print(row,'--', document.page_content,'--', document.metadata)