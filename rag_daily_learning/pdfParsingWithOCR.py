# ============================================================
# Complex PDF Parser for RAG
# Text + Tables + Images + OCR + LangChain Documents
# ============================================================
import os
import json
#import fitz  # PyMuPDF
import pymupdf
import pdfplumber
import pandas as pd
from PIL import Image
from pathlib import Path
from langchain_core.documents import Document
import pytesseract

print("Tesseract version:", pytesseract.get_tesseract_version())

ROOT_DIR = Path(__file__).resolve().parent
print('ROOT_DIR ',ROOT_DIR)

PDF_PATH = ROOT_DIR / "complex_rag_parsing_sample_with_image.pdf";
print('PDF_PATH ',PDF_PATH)

OUTPUT_PATH = ROOT_DIR/ "DATA" / "parsed_complex_pdf_output"
print('OUTPUT_PATH ',OUTPUT_PATH)

OUTPUT_DIR = Path(OUTPUT_PATH)

IMAGE_DIR = OUTPUT_DIR / "extracted_images"
PAGE_IMAGE_DIR = OUTPUT_DIR / "page_images"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
IMAGE_DIR.mkdir(parents=True, exist_ok=True)
PAGE_IMAGE_DIR.mkdir(parents=True, exist_ok=True)

print("PDF exists:", os.path.exists(PDF_PATH))

# ============================================================
# 2. Helper: Safe OCR
# OCR stands for Optical Character Recognition. In Python, OCR is the process of extracting text from images, scanned documents, screenshots, or PDFs.
# Common OCR Libraries in Python
# - pytesseract (wrapper for Tesseract-OCR)
# - easyocr
# - paddleocr
# ============================================================

def run_ocr_on_image(image_path):
    """
    Runs OCR on image using pytesseract.
    If tesseract is not installed in system, it will return empty text.
    """
    try:
        import pytesseract
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        return f"[OCR_SKIPPED_OR_FAILED: {str(e)}]"

# ============================================================
# 3. Extract Text + Images using PyMuPDF
# ============================================================
def extract_text_and_images(pdf_path):
    #doc = fitz.open(pdf_path)
    doc = pymupdf.open(pdf_path)

    page_records = []
    image_records = []

    for page_index in range(len(doc)):
        page = doc[page_index]
        page_number = page_index + 1

        # Extract normal selectable text
        text = page.get_text("text")

        # Extract page metadata-like info
        page_info = {
            "page_number": page_number,
            "text": text.strip(),
            "image_count": len(page.get_images(full=True)),
            "width": page.rect.width,
            "height": page.rect.height,
        }

        page_records.append(page_info)

        # Render full page as image for OCR
        #pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        pix = page.get_pixmap(matrix=pymupdf.Matrix(2, 2))
        page_image_path = PAGE_IMAGE_DIR / f"page_{page_number:03d}.png"
        pix.save(str(page_image_path))

        # OCR full page image
        ocr_text = run_ocr_on_image(page_image_path)
        page_info["ocr_text"] = ocr_text
        page_info["page_image_path"] = str(page_image_path)

        # Extract embedded images
        images = page.get_images(full=True)

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)

            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            image_path = IMAGE_DIR / f"page_{page_number:03d}_image_{img_index + 1}.{image_ext}"

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            image_ocr_text = run_ocr_on_image(image_path)

            image_records.append({
                "page_number": page_number,
                "image_index": img_index + 1,
                "image_path": str(image_path),
                "image_ext": image_ext,
                "image_ocr_text": image_ocr_text
            })

    doc.close()

    return page_records, image_records


page_records, image_records = extract_text_and_images(PDF_PATH)

print("Total pages parsed:", len(page_records))
print("Total images extracted:", len(image_records))

# ============================================================
# 4. Extract Tables using pdfplumber
# ============================================================

def extract_tables(pdf_path):
    table_records = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_index, page in enumerate(pdf.pages):
            page_number = page_index + 1

            try:
                tables = page.extract_tables()
            except Exception as e:
                tables = []
                print(f"Table extraction failed on page {page_number}: {e}")

            for table_index, table in enumerate(tables):
                if not table:
                    continue

                # Clean table rows
                cleaned_table = []
                for row in table:
                    cleaned_row = [
                        cell.strip() if isinstance(cell, str) else cell
                        for cell in row
                    ]
                    cleaned_table.append(cleaned_row)

                # Convert to DataFrame safely
                try:
                    df = pd.DataFrame(cleaned_table[1:], columns=cleaned_table[0])
                except Exception:
                    df = pd.DataFrame(cleaned_table)

                table_records.append({
                    "page_number": page_number,
                    "table_index": table_index + 1,
                    "raw_table": cleaned_table,
                    "markdown": df.to_markdown(index=False),
                    "csv": df.to_csv(index=False)
                })

    return table_records


table_records = extract_tables(PDF_PATH)

print("Total tables extracted:", len(table_records))

for table in table_records[:3]:
    print("\nPage:", table["page_number"], "Table:", table["table_index"])
    print(table["markdown"][:1000])


# ============================================================
# 5. Create LangChain Documents
# ============================================================

langchain_docs = []

# 5.1 Page text documents
for page in page_records:
    page_number = page["page_number"]

    combined_text = f"""
PAGE {page_number}

SELECTABLE TEXT:
{page["text"]}

OCR TEXT:
{page["ocr_text"]}
""".strip()

    doc = Document(
        page_content=combined_text,
        metadata={
            "source": PDF_PATH,
            "page_number": page_number,
            "content_type": "page_text_plus_ocr",
            "image_count": page["image_count"],
            "page_image_path": page["page_image_path"],
        }
    )

    langchain_docs.append(doc)

# 5.2 Table documents
for table in table_records:
    page_number = table["page_number"]

    table_text = f"""
TABLE FOUND ON PAGE {page_number}
TABLE INDEX: {table["table_index"]}

TABLE MARKDOWN:
{table["markdown"]}
""".strip()

    doc = Document(
        page_content=table_text,
        metadata={
            "source": PDF_PATH,
            "page_number": page_number,
            "content_type": "table",
            "table_index": table["table_index"],
        }
    )

    langchain_docs.append(doc)

# 5.3 Image OCR documents

for image in image_records:
    page_number = image["page_number"]

    image_text = f"""
IMAGE FOUND ON PAGE {page_number}
IMAGE INDEX: {image["image_index"]}
IMAGE PATH: {image["image_path"]}

IMAGE OCR TEXT:
{image["image_ocr_text"]}
""".strip()

    doc = Document(
        page_content=image_text,
        metadata={
            "source": PDF_PATH,
            "page_number": page_number,
            "content_type": "image",
            "image_index": image["image_index"],
            "image_path": image["image_path"],
            "image_ext": image["image_ext"],
        }
    )

    langchain_docs.append(doc)

print("Total LangChain Documents created:", len(langchain_docs))

# ============================================================
# 6. Save Parsed Output
# ============================================================

# Save page records
with open(OUTPUT_DIR / "page_records.json", "w", encoding="utf-8") as f:
    json.dump(page_records, f, indent=2, ensure_ascii=False)

# Save image records
with open(OUTPUT_DIR / "image_records.json", "w", encoding="utf-8") as f:
    json.dump(image_records, f, indent=2, ensure_ascii=False)

# Save table records
with open(OUTPUT_DIR / "table_records.json", "w", encoding="utf-8") as f:
    json.dump(table_records, f, indent=2, ensure_ascii=False)

# Save all LangChain document content as markdown
with open(OUTPUT_DIR / "rag_ready_documents.md", "w", encoding="utf-8") as f:
    for i, doc in enumerate(langchain_docs):
        f.write(f"\n\n# Document {i + 1}\n")
        f.write(f"\nMetadata:\n```json\n{json.dumps(doc.metadata, indent=2, default=str)}\n```\n")
        f.write("\nContent:\n")
        f.write(doc.page_content)
        f.write("\n\n---\n")

# Save table markdown separately
with open(OUTPUT_DIR / "extracted_tables.md", "w", encoding="utf-8") as f:
    for table in table_records:
        f.write(f"\n\n## Page {table['page_number']} - Table {table['table_index']}\n\n")
        f.write(table["markdown"])
        f.write("\n\n---\n")

print("\nSaved outputs in:", OUTPUT_DIR)

# ============================================================
# 7. Preview Parsed Output
# ============================================================

print("\n================ PAGE TEXT PREVIEW ================\n")
print(langchain_docs[0].page_content[:1500])

print("\n================ TABLE PREVIEW ================\n")
table_docs = [doc for doc in langchain_docs if doc.metadata["content_type"] == "table"]

if table_docs:
    print(table_docs[0].page_content[:1500])
else:
    print("No table docs found.")

print("\n================ IMAGE OCR PREVIEW ================\n")
image_docs = [doc for doc in langchain_docs if doc.metadata["content_type"] == "image"]

if image_docs:
    print(image_docs[0].page_content[:1500])
else:
    print("No image docs found.")