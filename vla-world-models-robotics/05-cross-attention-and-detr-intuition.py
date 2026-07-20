"""
Vision-Language-Action & World Models for Robotics
Chapter 5: Cross-Attention and the DETR Intuition
Section: Foundations: Perception, Language, Action

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/cross-attention-and-detr-intuition

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def cross_attention(q_src, kv_src, Wq, Wk, Wv):
    # q_src:  (n_query,   d)   the sequence doing the asking (e.g. words)
    # kv_src: (n_context, d)   the sequence being read      (e.g. patches)
    Q = q_src  @ Wq            # (n_query,   d_k)
    K = kv_src @ Wk            # (n_context, d_k)   <-- from the OTHER sequence
    V = kv_src @ Wv            # (n_context, d_k)   <-- from the OTHER sequence
    scores  = Q @ K.T / np.sqrt(Q.shape[-1])   # (n_query, n_context)
    weights = softmax(scores, axis=-1)          # each query-row sums to 1
    return weights @ V                          # (n_query, d_k)

def softmax(x, axis=-1):
    e = np.exp(x - x.max(axis=axis, keepdims=True))
    return e / e.sum(axis=axis, keepdims=True)
