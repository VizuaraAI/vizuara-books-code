"""
Build a Diffusion Language Model from Scratch
Chapter 13: The Attention Mechanism
Section: The Autoregressive Baseline

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/attention-mechanism

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import numpy as np

# --- block 1 ---
# X:   (4, 8)   the embedding matrix from the previous chapter
# W_Q: (8, 4)   W_K: (8, 4)   W_V: (8, 4)   learned

Q = X @ W_Q     # (4, 4)  — one query  vector per token
K = X @ W_K     # (4, 4)  — one key    vector per token
V = X @ W_V     # (4, 4)  — one value  vector per token

# --- block 2 ---
scores = Q @ K.T     # (4, 4): scores[i, j] = query_i · key_j

# --- block 3 ---
weights = softmax(scores / np.sqrt(d_k), axis=-1)   # (4, 4)
output  = weights @ V                                # (4, 4): the new token vectors

# --- block 4 ---
def attention(Q, K, V):
    d_k = Q.shape[-1]
    scores  = Q @ K.T / np.sqrt(d_k)      # (n, n): every query · every key, scaled
    weights = softmax(scores, axis=-1)    # each row sums to 1
    return weights @ V                     # (n, d_k): relevance-weighted blend of values

def softmax(x, axis=-1):
    e = np.exp(x - x.max(axis=axis, keepdims=True))
    return e / e.sum(axis=axis, keepdims=True)
