"""
Memory in AI Systems
Chapter 20: Embeddings and Vector Search
Section: Retrieval and Knowledge

Read this chapter: https://books.vizuara.ai/read/memory-workshop/embeddings-and-vector-search

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# Toy embeddings, d = 3.  (axes ~ biology, math, question)
store = {
    "m1: confuses mitosis and meiosis":      [0.90, 0.10, 0.00],
    "m2: prepping for a bio exam March 12":  [0.80, 0.05, 0.20],
    "m3: struggles with fraction word probs":[0.05, 0.95, 0.30],
}
query = "why do cells end up with half the chromosomes?"
q_vec = [0.85, 0.15, 0.60]

# --- block 2 ---
import numpy as np

def cosine(a, b):
    a, b = np.array(a), np.array(b)
    return a @ b / (np.linalg.norm(a) * np.linalg.norm(b))

def search(q_vec, store, k=2):
    scored = [(cosine(q_vec, vec), text) for text, vec in store.items()]
    scored.sort(reverse=True)          # highest similarity first
    return scored[:k]                  # the top-k most relevant memories

for score, text in search(q_vec, store, k=2):
    print(round(score, 2), text)
# 0.93  m2: prepping for a bio exam March 12
# 0.82  m1: confuses mitosis and meiosis
