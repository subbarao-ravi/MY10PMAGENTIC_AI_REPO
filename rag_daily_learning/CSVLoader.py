from langchain_community.document_loaders import CSVLoader
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
print('ROOT_DIR ',ROOT_DIR)

PDF_PATH = ROOT_DIR / "DOCS" / "sample_data.csv";
print('PDF_PATH ',PDF_PATH)

myloader = CSVLoader(PDF_PATH)
mydocs=myloader.load()

print('metadata ',mydocs[0].metadata)
print('pagecontent ', mydocs[0].page_content)