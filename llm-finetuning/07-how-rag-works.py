"""
LLM Finetuning
Chapter 7: How RAG Works
Section: Finetuning vs RAG

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/how-rag-works

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def rag_answer(question, chunks, embed, generate, k=3):
    q_vec = embed(question)                      # embed the query (same model as the chunks)
    scored = [(dot(q_vec, c.vec), c) for c in chunks]
    top = [c for _, c in sorted(scored, reverse=True)[:k]]   # k nearest neighbors
    context = "\n".join(f"[{i+1}] {c.text}" for i, c in enumerate(top))
    prompt = f"Use only this context:\n{context}\n\nQuestion: {question}\nAnswer:"
    return generate(prompt)                       # frozen LLM reads and answers
