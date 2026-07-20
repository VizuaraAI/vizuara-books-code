"""
RAG in Production
Chapter 38: Beyond Single-Shot Retrieval
Section: Agentic & Graph RAG

Read this chapter: https://books.vizuara.ai/read/rag-in-production/beyond-single-shot-retrieval

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not in the book; the reader supplies these) ---
# https://books.vizuara.ai/read/rag-in-production/beyond-single-shot-retrieval
retrieve = None    # TODO: one trip to the index - chapter 41 builds this
llm_reason = None  # TODO: LLM call returning .enough and .next_query
generate = None    # TODO: your grounded LLM call - see chapter 23

# --- block 1 ---
def iterative_retrieve(question, max_hops=4):
    evidence = []
    query = question
    for hop in range(max_hops):
        chunks = retrieve(query, top_k=3)        # one trip to the index
        evidence += chunks
        # the model reads what we have and decides the next move
        decision = llm_reason(question, evidence)
        if decision.enough:                      # stop condition
            return generate(question, evidence)
        query = decision.next_query              # built from what we just learned
    return generate(question, evidence)          # give up gracefully after max_hops
