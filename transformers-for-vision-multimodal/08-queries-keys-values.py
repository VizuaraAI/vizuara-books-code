"""
Transformers for Vision & Multimodal LLMs
Chapter 8: Queries, Keys and Values
Section: Attention From Scratch

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/queries-keys-values

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

def self_attention(X, Wq, Wk, Wv):
    Q, K, V = X @ Wq, X @ Wk, X @ Wv          # three learned projections
    d_k = Q.shape[-1]
    scores = Q @ K.transpose(-2, -1)          # (n, n): every query · every key
    scores = scores / d_k ** 0.5              # scale by 1/sqrt(d_k)
    weights = torch.softmax(scores, dim=-1)   # each row sums to 1, over keys
    return weights @ V                        # (n, d_v): relevance-weighted blend
