"""
AI Context Engineering
Chapter 15: Vector Search and Retrieval
Section: Write and Select: RAG

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/vector-search-and-retrieval

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def normalize(M):
    # unit-length each row so cosine == dot product later
    return M / np.linalg.norm(M, axis=1, keepdims=True)

# --- ingestion (done once) ---
# corpus_vecs: (N, d) matrix of chunk embeddings from your embed model
corpus_vecs = normalize(corpus_vecs)          # (N, d), each row ‖·‖ = 1

def retrieve(query_vec, corpus_vecs, chunks, k=3):
    q = query_vec / np.linalg.norm(query_vec)  # (d,) unit-length query
    scores = corpus_vecs @ q                    # (N,) cosine of query vs every chunk
    top = np.argsort(scores)[::-1][:k]          # indices of the k highest scores
    return [(chunks[i], float(scores[i])) for i in top]
