"""
RAG in Production
Chapter 22: Prompt Augmentation and Context Assembly
Section: Retrieval & Generation

Read this chapter: https://books.vizuara.ai/read/rag-in-production/prompt-augmentation-and-context-assembly

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not in the book; the reader supplies these) ---
interleave_ends = None  # TODO: reorders a list to [1st, 3rd, 5th, ..., 4th, 2nd] - see
                        # https://books.vizuara.ai/read/rag-in-production/prompt-augmentation-and-context-assembly

# --- block 1 ---
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
def n_tokens(text: str) -> int:
    return len(enc.encode(text))

def assemble_prompt(question, chunks, token_budget=3250):
    # chunks: list of dicts {text, source, score}, already sorted best-first
    kept, used = [], 0
    for c in chunks:
        block = f"[source: {c['source']}]\n{c['text']}"
        cost = n_tokens(block)
        if used + cost > token_budget:
            break                     # stop BEFORE we blow the budget
        kept.append(block)
        used += cost

    # place strongest at the ENDS, weaker toward the middle (dodge lost-in-the-middle)
    kept = interleave_ends(kept)      # [1st, 3rd, 5th, ..., 4th, 2nd]
    context = "\n\n---\n\n".join(kept)

    return (
        "Answer the question using ONLY the context below.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {question}"
    )
