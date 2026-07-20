"""
Modern Robot Learning
Chapter 17: Attention Is All You Need: A Recap
Section: Transformer Architecture from Scratch

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/attention-is-all-you-need-recap

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

scaled = np.array([2.12, 0.71, 0.35, 1.06])
weights = np.exp(scaled) / np.exp(scaled).sum()
# weights ≈ [0.57, 0.14, 0.10, 0.20], and they sum to 1.0

# --- block 2 ---
def attention(Q, K, V):
    d_k = Q.shape[-1]
    scores  = Q @ K.T / np.sqrt(d_k)     # (4,4): every query · every key, scaled
    weights = softmax(scores, axis=-1)   # each row sums to 1
    return weights @ V                    # (4,8): relevance-weighted blend of values

def softmax(x, axis=-1):
    e = np.exp(x - x.max(axis=axis, keepdims=True))
    return e / e.sum(axis=axis, keepdims=True)
