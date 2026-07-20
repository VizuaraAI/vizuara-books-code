"""
Modern Robot Learning
Chapter 18: Self-Attention: Queries, Keys, and Values
Section: Transformer Architecture from Scratch

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/self-attention-queries-keys-values

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

Q = X @ W_Q      # (4, 8) @ (8, 4) -> (4, 4)  one query per token
K = X @ W_K      # (4, 8) @ (8, 4) -> (4, 4)  one key   per token
V = X @ W_V      # (4, 8) @ (8, 4) -> (4, 4)  one value per token

# --- block 2 ---
def softmax(x, axis=-1):
    e = np.exp(x - x.max(axis=axis, keepdims=True))   # subtract max for stability
    return e / e.sum(axis=axis, keepdims=True)

def attention(Q, K, V):
    d_k = Q.shape[-1]
    scores  = Q @ K.T / np.sqrt(d_k)   # (4, 4): every query · every key, scaled
    weights = softmax(scores, axis=-1) # (4, 4): each row sums to 1
    return weights @ V                 # (4, 4): relevance-weighted blend of values
