"""
LLM Finetuning
Chapter 36: RAFT: Retrieval-Augmented Finetuning
Section: Research Projects

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/raft-retrieval-augmented-finetuning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# One RAFT example, formatted for standard instruction finetuning.
def format_raft_example(question, documents, cot_answer):
    context = "\n\n".join(f"[Doc {i}] {d}" for i, d in enumerate(documents))
    prompt  = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    return {
        "prompt":   prompt,       # documents live INSIDE the prompt -> masked in loss
        "response": cot_answer,   # quote-then-reason -> the only tokens the loss sees
    }
