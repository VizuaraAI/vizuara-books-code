"""
RAG in Production
Chapter 7: Loading Documents: PDF, HTML, and Beyond
Section: Data Ingestion

Read this chapter: https://books.vizuara.ai/read/rag-in-production/loading-documents-pdf-html-and-beyond

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import fitz  # PyMuPDF

def load_pdf(path):
    doc = fitz.open(path)
    pages = []
    for i, page in enumerate(doc):
        text = page.get_text("text")          # layout-ordered text
        pages.append({
            "page_content": text,
            "metadata": {"source": path, "page": i + 1},
        })
    return pages

# --- block 2 ---
from bs4 import BeautifulSoup

def load_html(html, source):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "header", "footer", "aside"]):
        tag.decompose()                       # remove junk subtrees
    text = soup.get_text(separator="\n", strip=True)
    return {"page_content": text, "metadata": {"source": source}}

# --- block 3 ---
from docx import Document as Docx

def load_docx(path):
    d = Docx(path)
    parts = [p.text for p in d.paragraphs if p.text.strip()]
    for table in d.tables:                     # tables live separately!
        for row in table.rows:
            parts.append(" | ".join(c.text for c in row.cells))
    return {"page_content": "\n".join(parts),
            "metadata": {"source": path}}

# --- block 4 ---
import pytesseract
from PIL import Image

def load_scan(path):
    text = pytesseract.image_to_string(Image.open(path))
    return {"page_content": text,
            "metadata": {"source": path, "extractor": "ocr"}}
