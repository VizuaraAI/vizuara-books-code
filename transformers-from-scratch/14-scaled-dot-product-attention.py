"""
Transformers: Theory, intuition, and Building from Scratch
Chapter 14: Scaled Dot-Product Attention
Section: Attention Mechanisms in Transformers

Read this chapter: https://books.vizuara.ai/read/transformers-from-scratch/scaled-dot-product-attention

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def softmax(x, axis=-1):
    x = x - x.max(axis=axis, keepdims=True)   # stability: subtract row max
    e = np.exp(x)
    return e / e.sum(axis=axis, keepdims=True)

def scaled_dot_product_attention(Q, K, V):
    d_k = Q.shape[-1]                          # e.g. 64
    scores = Q @ K.T / np.sqrt(d_k)            # (n, n): score then scale
    A = softmax(scores, axis=-1)               # (n, n): each row sums to 1
    return A @ V, A                            # (n, d_v): blend the values
