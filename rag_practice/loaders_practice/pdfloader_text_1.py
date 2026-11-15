from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

base_dir = Path(__file__).resolve().parent / "LoaderDocs"
pdf_dir = base_dir / "PDFDOCS"
pdf_dir.mkdir(exist_ok=True)

pdf_sub_dir = pdf_dir / "loadedPdfs"
pdf_sub_dir.mkdir(parents=True, exist_ok=True)

pdf_file_path = pdf_dir / "RAG_PyPDFLoader_1.pdf"
print('pdf_file_path ',pdf_file_path)

delimiter = "\n----- PAGE BREAK -----\n"
pdfLoader = PyPDFLoader(
    file_path=pdf_file_path,
    mode='single',
    pages_delimiter=delimiter
)

documents = pdfLoader.load()
document = documents[0]

pages = document.page_content.split(delimiter)
for pageno, text in enumerate(pages, start=1):
    file_path = pdf_sub_dir / f"RAG_PyPDFLoader_TEXT_{pageno}.txt"
    file_path.write_text(text, encoding='utf-8')
    print("--------------Created----------:", file_path)