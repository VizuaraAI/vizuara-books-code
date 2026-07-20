"""
AI Agents Bootcamp
Chapter 28: Embeddings and Vector Search
Section: Retrieval: RAG and Agentic RAG

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/embeddings-and-vector-search

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    dot = a @ b                          # sum of element-wise products
    return dot / (np.linalg.norm(a) * np.linalg.norm(b))
