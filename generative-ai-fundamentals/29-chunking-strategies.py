"""
Generative AI Fundamentals
Chapter 29: Chunking Strategies
Section: Semantic Search & Dense Retrieval

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/chunking-strategies

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def fixed_chunks(text, chunk_size=500, overlap=100):
    stride = chunk_size - overlap        # how far we advance each step
    chunks = []
    for start in range(0, len(text), stride):
        chunks.append(text[start:start + chunk_size])
    return chunks
