"""
Memory in AI Systems
Chapter 28: Coding a Vector Memory Store
Section: Coding Memory Layers from Scratch

Read this chapter: https://books.vizuara.ai/read/memory-workshop/coding-a-vector-memory-store

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

class VectorMemory:
    def __init__(self, embed_fn):
        self.embed = embed_fn          # text -> np.array of shape (d,)
        self.texts = []                # the raw memories
        self.vectors = []              # their embeddings

    def add(self, text):
        self.texts.append(text)
        self.vectors.append(self.embed(text))

    def retrieve(self, query, k=3):
        q = self.embed(query)
        q = q / np.linalg.norm(q)                      # normalise the query once
        scores = []
        for v in self.vectors:
            v = v / np.linalg.norm(v)                  # normalise each memory
            scores.append(float(np.dot(q, v)))         # cosine = dot of unit vectors
        ranked = np.argsort(scores)[::-1]              # sort high -> low
        return [(self.texts[i], scores[i]) for i in ranked[:k]]
