"""
RAG in Production
Chapter 29: Re-ranking with Cross-Encoders
Section: Advanced RAG

Read this chapter: https://books.vizuara.ai/read/rag-in-production/reranking-with-cross-encoders

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from sentence_transformers import CrossEncoder

# loaded once at startup, not per request
reranker = CrossEncoder("BAAI/bge-reranker-base")

def retrieve_and_rerank(query, index, n=20, k=3):
    # STAGE 1 — over-retrieve: fast bi-encoder shortlist, high recall
    shortlist = index.search(query, top_k=n)          # N candidate chunks

    # STAGE 2 — re-rank: score every (query, chunk) pair jointly
    pairs  = [(query, c.text) for c in shortlist]
    scores = reranker.predict(pairs)                  # one batched forward pass

    ranked = sorted(zip(shortlist, scores),
                    key=lambda cs: cs[1], reverse=True)
    return [c for c, _ in ranked[:k]]                 # keep the sharp top-k
