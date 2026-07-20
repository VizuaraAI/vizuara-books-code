"""
LLM Production & Deployment
Chapter 27: Generation & Grounding
Section: RAG in Production

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/generation-and-grounding

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
from context import query   # Chapter 26 defines this question verbatim

retrieved = None  # TODO: the ranked chunks returned by Chapter 26's retriever.
llm = None        # TODO: your generation client (vLLM or an API client).
# --- end fixups ---

# --- block 1 ---
SYSTEM = (
    "Answer the question using ONLY the context below. "
    "If the answer is not in the context, reply exactly: "
    "\"I don't have that information.\" Do not use outside knowledge."
)

def build_prompt(query, chunks):
    context = "\n\n".join(
        f"[{i+1}] {c.text}" for i, c in enumerate(chunks)
    )
    return (
        f"{SYSTEM}\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {query}\n\nAnswer:"
    )

prompt = build_prompt(query, retrieved[:3])   # top-3 chunks
answer = llm.generate(prompt, temperature=0.0)
