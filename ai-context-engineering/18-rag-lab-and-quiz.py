"""
AI Context Engineering
Chapter 18: RAG Lab and Interactive Quiz
Section: Write and Select: RAG

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/rag-lab-and-quiz

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def ask(question: str) -> str:
    q_vec  = embed(question)                       # same model as the corpus
    chunks = retrieve(q_vec, corpus_vecs, texts, k=4)   # top-4 by cosine
    context = "\n\n".join(text for text, score in chunks)
    prompt  = f"Answer using ONLY this context:\n{context}\n\nQ: {question}"
    return llm(prompt)

# --- block 2 ---
def ask_verbose(question: str, k: int = 4):
    q_vec  = embed(question)
    hits   = retrieve(q_vec, corpus_vecs, texts, k=k)   # [(text, score), ...]
    context = "\n\n".join(text for text, _ in hits)
    answer  = llm(f"Answer using ONLY this context:\n{context}\n\nQ: {question}")
    return answer, hits                                  # <- return the evidence too

# --- block 3 ---
def hit_rate(eval_set, k=4):
    hits = 0
    for q, gold_chunk_id in eval_set:
        retrieved_ids = [cid for cid, _ in retrieve_ids(embed(q), k=k)]
        hits += gold_chunk_id in retrieved_ids     # was the RIGHT chunk fetched?
    return hits / len(eval_set)
