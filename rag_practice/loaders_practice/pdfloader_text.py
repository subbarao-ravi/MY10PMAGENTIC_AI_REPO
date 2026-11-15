from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

base_dir = Path(__file__).resolve().parent / "LoaderDocs"
pdf_dir = base_dir / "PDFDOCS"
pdf_dir.mkdir(exist_ok=True)

pdf_sub_dir = pdf_dir / "loadedPdfs"
pdf_sub_dir.mkdir(parents=True, exist_ok=True)

pdf_file_path = pdf_dir / "RAG_PyPDFLoader_1.pdf"
pdf_file_path = pdf_dir / "RAG_PyPDFLoader_1.pdf"
print('pdf_file_path ',pdf_file_path)

pdfLoader = PyPDFLoader(
    file_path=pdf_file_path
)

documents = pdfLoader.load()
for pageno, document in enumerate(documents, start=1):
    file_path = pdf_sub_dir / f"RAG_PyPDFLoader_{pageno}.txt"
    file_path.write_text(document.page_content, encoding='utf-8')
    print("--------------Created----------:", file_path)
    print(document.metadata)