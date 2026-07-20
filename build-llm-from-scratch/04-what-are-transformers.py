"""
Build Large Language Models (LLMs) from Scratch
Chapter 4: What are transformers?
Section: LLM Basics

Read this chapter: https://books.vizuara.ai/read/build-llm-from-scratch/what-are-transformers

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def attention(Q, K, V):
    # Q, K, V each have shape (seq_len, d_k)
    d_k = Q.shape[-1]
    scores = Q @ K.T / np.sqrt(d_k)      # (seq_len, seq_len): every query · every key
    weights = softmax(scores, axis=-1)   # each row sums to 1
    return weights @ V                    # (seq_len, d_k): relevance-weighted blend of values

def softmax(x, axis=-1):
    e = np.exp(x - x.max(axis=axis, keepdims=True))
    return e / e.sum(axis=axis, keepdims=True)
