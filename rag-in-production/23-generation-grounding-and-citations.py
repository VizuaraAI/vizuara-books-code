"""
RAG in Production
Chapter 23: Generation, Grounding, and Citations
Section: Retrieval & Generation

Read this chapter: https://books.vizuara.ai/read/rag-in-production/generation-grounding-and-citations

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
SYSTEM_PROMPT = """You are a precise assistant. Answer the user's question
using ONLY the information in the context below. Each context passage is
tagged with a source id like [1], [2].

Rules:
- If the answer is not in the context, reply exactly:
  "I don't have enough information to answer that."
- Do not use any prior knowledge or make assumptions.
- After each claim, cite the source id(s) it came from, e.g. [1].

Context:
{context}

Question: {question}
"""

# --- block 2 ---
def format_context(chunks):
    # chunks: list of dicts with 'text' and 'metadata'
    blocks = []
    for i, ch in enumerate(chunks, start=1):     # 1-based ids
        src = ch["metadata"]["source"]           # e.g. "refund_policy.pdf p.3"
        blocks.append(f"[{i}] (source: {src})\n{ch['text']}")
    return "\n\n".join(blocks)
