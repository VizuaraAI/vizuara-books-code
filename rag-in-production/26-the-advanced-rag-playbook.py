"""
RAG in Production
Chapter 26: The Advanced RAG Playbook
Section: Advanced RAG

Read this chapter: https://books.vizuara.ai/read/rag-in-production/the-advanced-rag-playbook

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not in the book; the reader supplies these) ---
# This chapter is the playbook overview: each name below is a stage that a
# LATER chapter builds. See https://books.vizuara.ai/read/rag-in-production/the-advanced-rag-playbook
expand_query = None            # TODO: multi-query rephrasings - see chapter 27
vector_search = None           # TODO: dense bi-encoder search - see chapters 19-20
bm25_search = None             # TODO: sparse keyword search - see chapter 28
reciprocal_rank_fusion = None  # TODO: RRF fusion - see chapter 28
cross_encoder_rerank = None    # TODO: cross-encoder re-ranking - see chapter 29
dedupe = None                  # TODO: de-duplicates fused candidates
compress = None                # TODO: context compression - see chapter 30
generate = None                # TODO: your grounded LLM call - see chapter 23

# --- block 1 ---
def advanced_rag(query, k=3, N=20):
    # 1. QUERY-SIDE — turn one bad key into several good ones
    subqueries = expand_query(query)          # e.g. multi-query rephrasings

    # 2. RETRIEVAL-SIDE — dense + sparse, fused, over-retrieved to N
    candidates = []
    for q in subqueries:
        dense  = vector_search(q, top=N)      # bi-encoder, semantic
        sparse = bm25_search(q, top=N)        # keyword, exact tokens
        candidates += reciprocal_rank_fusion(dense, sparse)  # RRF

    # 3. POST-RETRIEVAL — re-rank the shortlist, then trim the noise
    ranked   = cross_encoder_rerank(query, dedupe(candidates))  # slow, sharp
    context  = compress(ranked[:k])           # drop irrelevant sentences

    return generate(query, context)           # grounded answer + citations
