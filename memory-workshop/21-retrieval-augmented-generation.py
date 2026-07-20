"""
Memory in AI Systems
Chapter 21: Retrieval-Augmented Generation (RAG)
Section: Retrieval and Knowledge

Read this chapter: https://books.vizuara.ai/read/memory-workshop/retrieval-augmented-generation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def build_prompt(query, retrieved_chunks):
    context = "\n".join(f"- {c}" for c in retrieved_chunks)
    return (
        "Answer using ONLY the context below. "
        "If the answer isn't there, say you don't know.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {query}"
    )
