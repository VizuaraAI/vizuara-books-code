"""
RAG in Production
Chapter 31: Building an Advanced RAG Pipeline
Section: Advanced RAG

Read this chapter: https://books.vizuara.ai/read/rag-in-production/building-an-advanced-rag-pipeline

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# `rrf` is defined in chapter 28 (Hybrid Search: Dense plus Sparse).
from context import rrf

# --- stubs (not in the book; the reader supplies these) ---
# https://books.vizuara.ai/read/rag-in-production/building-an-advanced-rag-pipeline
rewrite = None               # TODO: history-aware query rewriter - see chapter 27
expand_query = None          # TODO: multi-query rephrasings - see chapter 27
vector_search = None         # TODO: dense bi-encoder search - see chapters 19-20
bm25_search = None           # TODO: sparse keyword search - see chapter 28
dedupe = None                # TODO: de-duplicates fused candidates
cross_encoder_rerank = None  # TODO: cross-encoder re-ranking - see chapter 29
compress = None              # TODO: context compression - see chapter 30
generate = None              # TODO: your grounded LLM call - see chapter 23

# --- block 1 ---
def advanced_rag(query, chat_history=None, k=3, N=20):
    # QUERY-SIDE: rewrite for context, then fan out to several probes
    query = rewrite(query, chat_history)          # resolve "it"/"that", spell out terms
    subqueries = expand_query(query)              # multi-query: 3 rephrasings

    # RETRIEVAL-SIDE: hybrid (dense + BM25), fused, over-retrieved to N
    candidates = []
    for q in subqueries:
        dense  = vector_search(q, top=N)          # bi-encoder, semantic
        sparse = bm25_search(q, top=N)            # keyword, exact tokens
        candidates += rrf(dense, sparse)          # fuse on rank, k=60
    candidates = dedupe(candidates)               # union across subqueries

    # POST-RETRIEVAL: re-rank the shortlist, then compress to signal
    ranked  = cross_encoder_rerank(query, candidates)   # slow, sharp — on ~N items
    context = compress(ranked[:k])                # drop irrelevant sentences

    return generate(query, context)               # grounded answer + citations
