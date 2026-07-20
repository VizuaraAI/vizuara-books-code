"""
AI Context Engineering
Chapter 13: Why RAG Exists: Grounding, Freshness, and Cost
Section: Write and Select: RAG

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/why-rag-exists

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
q_vec   = embed(question)                      # question → a vector
hits    = store.search(q_vec, top_k=2)         # nearest chunks by cosine similarity
context = "\n\n".join(h.text for h in hits)    # the retrieved evidence
answer  = model(f"Use this context:\n{context}\n\nQ: {question}")
