"""
Generative AI Fundamentals
Chapter 12: Embeddings: The Hidden Workhorse
Section: Text Clustering & Topic Modeling

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/embeddings-the-hidden-workhorse

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def cosine_sim(a, b):
    a = a / np.linalg.norm(a)       # scale to unit length
    b = b / np.linalg.norm(b)
    return float(a @ b)             # dot product of unit vectors = cosine

a = np.array([0.9, 0.1])
b = np.array([0.8, 0.2])
c = np.array([0.1, 0.9])
print(cosine_sim(a, b))            # ≈ 0.99
print(cosine_sim(a, c))            # ≈ 0.22
