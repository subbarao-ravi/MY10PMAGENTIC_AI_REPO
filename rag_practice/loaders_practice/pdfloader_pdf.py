from langchain_core.documents import Document
from pathlib import Path
from pypdf import PdfReader, PdfWriter

base_dir = Path(__file__).resolve().parent / "LoaderDocs"
pdf_dir = base_dir / "PDFDOCS"
pdf_dir.mkdir(exist_ok=True)

pdf_sub_dir = pdf_dir / "loadedPdfs"
pdf_sub_dir.mkdir(parents=True, exist_ok=True)

pdf_file_path = pdf_dir / "RAG_PyPDFLoader_1.pdf"
print('pdf_file_path ',pdf_file_path)


reader = PdfReader(pdf_file_path)

for pageno, page in enumerate(reader.pages, start=1):
    writer = PdfWriter()
    writer.add_page(page)
    writer.add_metadata(reader.metadata)
    file_path = pdf_sub_dir / f"RAG_PyPDFLoader_{pageno}.pdf"
    with open(file_path, 'wb') as f:
        writer.write(f)
        print("--------------Created----------:", file_path)