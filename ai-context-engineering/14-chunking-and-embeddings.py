"""
AI Context Engineering
Chapter 14: Chunking and Embeddings
Section: Write and Select: RAG

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/chunking-and-embeddings

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def chunk(tokens, size=300, overlap=50):
    stride = size - overlap          # advance 250 tokens each step
    chunks = []
    for start in range(0, len(tokens), stride):
        chunks.append(tokens[start:start + size])
    return chunks

# len(tokens) = 3000, size=300, overlap=50  ->  12 chunks,
# each sharing 50 tokens with the one before it.
