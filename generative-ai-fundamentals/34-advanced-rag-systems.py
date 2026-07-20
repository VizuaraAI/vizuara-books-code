"""
Generative AI Fundamentals
Chapter 34: Advanced RAG Systems
Section: Retrieval-Augmented Generation (RAG)

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/advanced-rag-systems

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# one cheap LLM call turns the raw query into targeted sub-queries
rewrite_prompt = """Break the user's question into standalone search queries.
Question: why did the q3 launch slip and who signed off on the new date?"""

# model returns:
sub_queries = [
    "reasons the Q3 product launch was delayed",
    "who approved the revised Q3 launch date",
]

# --- block 2 ---
def rrf(rank_lists, k=60):
    scores = {}
    for ranked in rank_lists:               # e.g. [dense_ids, bm25_ids]
        for rank, doc_id in enumerate(ranked):
            scores[doc_id] = scores.get(doc_id, 0) + 1 / (k + rank)
    return sorted(scores, key=scores.get, reverse=True)

# --- block 3 ---
query = "who approved the revised Q3 launch date?"
context = []
for hop in range(MAX_HOPS):          # a hard cap — always cap the hops
    chunks = retrieve(query)         # hybrid search from above
    context += chunks
    step = llm(f"Given:\n{context}\nAnswer or ask ONE follow-up query:")
    if step.is_answer:
        break
    query = step.followup_query      # hop 2: "what did <name> previously ship?"
