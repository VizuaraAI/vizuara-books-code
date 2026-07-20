"""
RAG in Production - shared context

Definitions that a later chapter uses but that the book introduces in an
EARLIER chapter. Every function below is copied verbatim from the chapter
named in its comment, so that later chapter files can simply do:

    from context import cosine, rrf

Nothing here is invented; if a name a chapter needs is not defined anywhere
in the book, that chapter file declares it as an explicit stub instead.
"""

import numpy as np


# --- from Chapter 17: Similarity Metrics: Cosine, Dot, Euclidean ---
# https://books.vizuara.ai/read/rag-in-production/similarity-metrics-cosine-dot-euclidean
def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# --- from Chapter 28: Hybrid Search: Dense plus Sparse ---
# https://books.vizuara.ai/read/rag-in-production/hybrid-search-dense-plus-sparse
def rrf(ranked_lists, k=60):
    scores = {}
    for ranked in ranked_lists:                 # e.g. [dense_ids, bm25_ids]
        for rank, doc_id in enumerate(ranked, start=1):
            scores[doc_id] = scores.get(doc_id, 0) + 1 / (k + rank)
    return sorted(scores, key=scores.get, reverse=True)
