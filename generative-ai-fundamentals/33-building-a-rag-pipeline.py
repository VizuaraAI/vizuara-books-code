"""
Generative AI Fundamentals
Chapter 33: Building a RAG Pipeline
Section: Retrieval-Augmented Generation (RAG)

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/building-a-rag-pipeline

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
chunks = [
    "The billing service listens on port 8080 by default.",
    "Our mascot is a red panda named Pixel.",
    "Set BILLING_TIMEOUT to change the request timeout in seconds.",
]

# --- block 2 ---
TEMPLATE = """Answer the question using ONLY the context below.
If the context does not contain the answer, say "I don't know."

Context:
{context}

Question: {question}
Answer:"""

def augment(question, retrieved_chunks):
    context = "\n".join(
        f"[{i+1}] {c}" for i, c in enumerate(retrieved_chunks)
    )
    return TEMPLATE.format(context=context, question=question)

# --- block 3 ---
def rag_answer(question, k=3):
    q_vec   = embed(question)               # reuse: embedder
    hits    = index.search(q_vec, k=k)      # reuse: retriever → top-k chunks
    prompt  = augment(question, hits)       # NEW: fill the template
    return generate(prompt)                 # reuse: the LLM
