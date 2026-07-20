"""
Transformers: Theory, intuition, and Building from Scratch
Chapter 4: Understanding Attention
Section: Foundations of Attention

Read this chapter: https://books.vizuara.ai/read/transformers-from-scratch/understanding-attention

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def softmax(x, axis=-1):
    x = x - x.max(axis=axis, keepdims=True)      # stability: subtract row max
    e = np.exp(x)
    return e / e.sum(axis=axis, keepdims=True)

def attention(X, W_Q, W_K, W_V):
    Q = X @ W_Q                     # (n, d_k)  — what each token asks
    K = X @ W_K                     # (n, d_k)  — what each token advertises
    V = X @ W_V                     # (n, d_v)  — what each token offers
    d_k = Q.shape[-1]
    scores = Q @ K.T / np.sqrt(d_k) # (n, n)    — scaled alignment grid
    A = softmax(scores, axis=-1)    # (n, n)    — each row sums to 1
    return A @ V, A                 # (n, d_v)  — the blended, context-aware output
