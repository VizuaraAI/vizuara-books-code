"""
LLM Production & Deployment
Chapter 24: Data Ingestion & Chunking
Section: RAG in Production

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/data-ingestion-and-chunking

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def chunk_fixed(text, size=200, overlap=0):
    words = text.split()
    chunks, start = [], 0
    step = size - overlap                 # how far the window advances
    while start < len(words):
        chunk = words[start : start + size]
        chunks.append(" ".join(chunk))
        start += step
    return chunks
