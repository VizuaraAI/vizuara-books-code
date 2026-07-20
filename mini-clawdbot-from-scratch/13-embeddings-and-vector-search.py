"""
Build a Mini ClawdBot from Scratch
Chapter 13: Embeddings and Vector Search
Section: Memory and RAG

Read this chapter: https://books.vizuara.ai/read/mini-clawdbot-from-scratch/embeddings-and-vector-search

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def cosine(a, b):
    dot   = np.dot(a, b)                      # sum of elementwise products
    norm  = np.linalg.norm(a) * np.linalg.norm(b)   # ‖a‖ · ‖b‖
    return dot / norm

# --- block 2 ---
collection.add(
    ids       = ["msg_9f3a"],
    embeddings= [[0.021, -0.11, 0.34, ...]],   # 1,536 floats
    documents = ["let's cap the payment webhook retries at 3"],
    metadatas = [{"channel": "#backend", "user": "Ana"}],
)

# --- block 3 ---
results = collection.query(
    query_embeddings=[q_vector],   # the embedded question
    n_results=3,                    # top-k
)
