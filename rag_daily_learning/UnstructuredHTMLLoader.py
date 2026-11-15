from langchain_community.document_loaders import UnstructuredHTMLLoader
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
print('ROOT_DIR ',ROOT_DIR)

PDF_PATH = ROOT_DIR / "DOCS" / "sample_page.html";
print('PDF_PATH ',PDF_PATH)

myloader = UnstructuredHTMLLoader(PDF_PATH)
mydocs=myloader.load()

print('metadata ',mydocs[0].metadata)
print('pagecontent ', mydocs[0].page_content)