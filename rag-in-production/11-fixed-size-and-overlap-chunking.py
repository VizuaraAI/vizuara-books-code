"""
RAG in Production
Chapter 11: Fixed-Size and Overlap Chunking
Section: Chunking

Read this chapter: https://books.vizuara.ai/read/rag-in-production/fixed-size-and-overlap-chunking

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def fixed_size_chunks(tokens, chunk_size=200, chunk_overlap=40):
    assert chunk_overlap < chunk_size, "overlap must be smaller than the chunk"
    stride = chunk_size - chunk_overlap          # 160 with the defaults above
    chunks = []
    for start in range(0, len(tokens), stride):
        chunk = tokens[start : start + chunk_size]   # a window, not a stride-sized slice
        chunks.append(chunk)
        if start + chunk_size >= len(tokens):
            break                                     # last window already reached the end
    return chunks
