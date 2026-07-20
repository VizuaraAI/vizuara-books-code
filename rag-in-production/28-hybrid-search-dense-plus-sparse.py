"""
RAG in Production
Chapter 28: Hybrid Search: Dense plus Sparse
Section: Advanced RAG

Read this chapter: https://books.vizuara.ai/read/rag-in-production/hybrid-search-dense-plus-sparse

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not in the book; the reader supplies these) ---
# https://books.vizuara.ai/read/rag-in-production/hybrid-search-dense-plus-sparse
dense_ids = None  # TODO: doc ids ranked by the dense (vector) search
bm25_ids = None   # TODO: doc ids ranked by the BM25 (sparse) search

# --- block 1 ---
from rank_bm25 import BM25Okapi

corpus = [
    "Reset the router to clear E-4021, then power-cycle.",
    "E-4021 E-4021 diagnostics: E-4021 indicates a handshake failure.",
    "General network errors can interrupt your connection.",
]
tokenized = [doc.lower().split() for doc in corpus]   # split on whitespace
bm25 = BM25Okapi(tokenized)                            # builds IDF + length stats

query = "e-4021".split()
scores = bm25.get_scores(query)   # -> array like [~1.0, ~1.8, 0.0]

# --- block 2 ---
def rrf(ranked_lists, k=60):
    scores = {}
    for ranked in ranked_lists:                 # e.g. [dense_ids, bm25_ids]
        for rank, doc_id in enumerate(ranked, start=1):
            scores[doc_id] = scores.get(doc_id, 0) + 1 / (k + rank)
    return sorted(scores, key=scores.get, reverse=True)

fused = rrf([dense_ids, bm25_ids])   # -> ['A', 'C', 'B', 'D']
