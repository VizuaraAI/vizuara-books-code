"""
Neural Networks from Scratch
Chapter 7: Tensors: The Data Containers
Section: Turning Scores into Probabilities

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/tensors

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

scores = np.array([[ 1.60, -0.70,  0.00],   # sample 0
                   [-0.30,  1.20,  0.50],   # sample 1
                   [ 0.10,  0.10,  2.00],   # sample 2
                   [ 0.40, -1.10,  0.90]])  # sample 3

print(scores.shape)   # (4, 3)
print(scores.ndim)    # 2   → rank 2, a matrix
print(scores.size)    # 12  → total numbers = 4 × 3

# --- block 2 ---
z = scores - scores.max(axis=1, keepdims=True)   # (4, 3) - (4, 1) → (4, 3)
exp = np.exp(z)                                   # (4, 3)
probs = exp / exp.sum(axis=1, keepdims=True)      # (4, 3) / (4, 1) → (4, 3)

print(probs.shape)          # (4, 3)
print(probs.sum(axis=1))    # [1. 1. 1. 1.]  → every row sums to 1
