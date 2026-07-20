"""
RAG in Production
Chapter 17: Similarity Metrics: Cosine, Dot, Euclidean
Section: Embeddings & Indexing

Read this chapter: https://books.vizuara.ai/read/rag-in-production/similarity-metrics-cosine-dot-euclidean

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def l2_normalize(v):
    return v / np.linalg.norm(v)

# After normalizing, cosine == plain dot product:
qn = l2_normalize(np.array([1.0, 0.0]))
cn = l2_normalize(np.array([10.0, 0.0]))
np.dot(qn, cn)          # 1.0  — same as cosine(q, c2)
