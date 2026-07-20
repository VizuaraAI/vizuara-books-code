"""
LLM Production & Deployment
Chapter 25: Chunking Strategies Compared
Section: RAG in Production

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/chunking-strategies

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def fixed_chunks(tokens, chunk_size=40, overlap=10):
    step = chunk_size - overlap          # how far the window advances
    chunks = []
    for start in range(0, len(tokens), step):
        chunks.append(tokens[start : start + chunk_size])
    return chunks

# --- block 2 ---
import re

def structural_chunks(markdown):
    # split right before every line that starts with one or more '#'
    parts = re.split(r"\n(?=#{1,6}\s)", markdown)
    return [p.strip() for p in parts if p.strip()]
