"""
RAG in Production
Chapter 30: Context Compression and Filtering
Section: Advanced RAG

Read this chapter: https://books.vizuara.ai/read/rag-in-production/context-compression-and-filtering

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not in the book; the reader supplies these) ---
split_sentences = None  # TODO: naive sentence splitter (on '. ' etc.) - see
                        # https://books.vizuara.ai/read/rag-in-production/context-compression-and-filtering

# --- block 1 ---
import numpy as np

def cosine(a, b):
    return a @ b / (np.linalg.norm(a) * np.linalg.norm(b))

def compress_chunk(query, chunk, embed, threshold=0.35):
    # embed the query once, and every sentence in the chunk
    sentences = split_sentences(chunk)          # naive: on '. ' etc.
    q = embed(query)
    kept = []
    for s in sentences:
        score = cosine(q, embed(s))             # sentence vs. query
        if score >= threshold:                  # keep only what clears the bar
            kept.append(s)
    return " ".join(kept)                        # verbatim subset — no rewriting
