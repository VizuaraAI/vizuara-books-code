"""
Build Large Language Models (LLMs) from Scratch
Chapter 9: The self attention mechanism with keys, query and values: coded form scratch
Section: LLM Attention Mechanism

Read this chapter: https://books.vizuara.ai/read/build-llm-from-scratch/the-self-attention-mechanism-with-keys-query-and-values-code

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def softmax(x, axis=-1):
    x = x - x.max(axis=axis, keepdims=True)   # subtract max for stability
    e = np.exp(x)
    return e / e.sum(axis=axis, keepdims=True)

def self_attention(X, W_q, W_k, W_v):
    # X:   (T, d_in)     T token embeddings
    # W_*: (d_in, d_out)
    Q = X @ W_q                     # (T, d_out)  queries
    K = X @ W_k                     # (T, d_out)  keys
    V = X @ W_v                     # (T, d_out)  values

    d_k = K.shape[-1]
    scores  = Q @ K.T               # (T, T)   affinity of every token pair
    scores  = scores / np.sqrt(d_k) # scale, keep softmax in its live range
    weights = softmax(scores, -1)   # (T, T)   each row sums to 1

    context = weights @ V           # (T, d_out)  attention-weighted values
    return context, weights

# tiny worked example: 3 tokens, d_in=3, d_out=2
rng = np.random.default_rng(0)
X   = rng.random((3, 3))
W_q, W_k, W_v = (rng.random((3, 2)) for _ in range(3))

context, weights = self_attention(X, W_q, W_k, W_v)
print(context.shape)   # (3, 2)
print(weights.sum(1))  # [1. 1. 1.]  every row is a distribution
