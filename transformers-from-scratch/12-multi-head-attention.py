"""
Transformers: Theory, intuition, and Building from Scratch
Chapter 12: Multi-Head Attention
Section: Attention Mechanisms in Transformers

Read this chapter: https://books.vizuara.ai/read/transformers-from-scratch/multi-head-attention

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def softmax(x, axis=-1):
    x = x - x.max(axis=axis, keepdims=True)
    e = np.exp(x)
    return e / e.sum(axis=axis, keepdims=True)

def multi_head_attention(X, W_Q, W_K, W_V, W_O, h):
    n, d_model = X.shape                      # e.g. (n, 512)
    d_k = d_model // h                        # 512 // 8 = 64

    # one big projection each, then split into h heads of width d_k
    Q = (X @ W_Q).reshape(n, h, d_k).transpose(1, 0, 2)   # (h, n, d_k)
    K = (X @ W_K).reshape(n, h, d_k).transpose(1, 0, 2)
    V = (X @ W_V).reshape(n, h, d_k).transpose(1, 0, 2)

    scores = Q @ K.transpose(0, 2, 1) / np.sqrt(d_k)      # (h, n, n): 8 grids
    A = softmax(scores, axis=-1)                          # 8 private softmaxes
    Z = A @ V                                             # (h, n, d_k)

    Z = Z.transpose(1, 0, 2).reshape(n, d_model)          # concat: (n, 512)
    return Z @ W_O                                        # mix the heads
