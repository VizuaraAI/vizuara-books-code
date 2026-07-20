"""
Vision-Language-Action & World Models for Robotics
Chapter 3: Transformers and Self-Attention, Refreshed
Section: Foundations: Perception, Language, Action

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/transformers-and-self-attention-refresher

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def softmax(x, axis=-1):
    e = np.exp(x - x.max(axis=axis, keepdims=True))
    return e / e.sum(axis=axis, keepdims=True)

def self_attention(X, W_Q, W_K, W_V):
    Q, K, V = X @ W_Q, X @ W_K, X @ W_V      # each (4, 4)
    d_k = Q.shape[-1]
    scores  = Q @ K.T / np.sqrt(d_k)          # (4, 4): every query · every key
    weights = softmax(scores, axis=-1)        # each row sums to 1
    return weights @ V                        # (4, 4): relevance-weighted blend
