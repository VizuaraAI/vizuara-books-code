"""
Generative AI Fundamentals
Chapter 32: RAG from First Principles
Section: Retrieval-Augmented Generation (RAG)

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/rag-from-first-principles

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
C0 = [ 0.8,  0.5,  0.1,  0.3]   # refund + time window
C1 = [ 0.1,  0.2,  0.9,  0.3]   # office hours
C2 = [ 0.7,  0.6,  0.2,  0.3]   # refund + order number
C3 = [ 0.2,  0.1,  0.3,  0.9]   # location

# --- block 2 ---
q  = [ 0.75, 0.55, 0.15, 0.30]

# --- block 3 ---
prompt = f"""Answer the question using ONLY the context below.
If the context does not contain the answer, say "I don't know."

Context:
{retrieved_chunks}

Question: {user_question}
Answer:"""
