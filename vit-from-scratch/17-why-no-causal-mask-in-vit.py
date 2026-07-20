"""
Build a Vision Transformer (ViT) from Scratch
Chapter 17: Why ViT Attention is Bidirectional
Section: Attention Inside the ViT

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/why-no-causal-mask-in-vit

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn.functional as F

def attention(Q, K, V, causal=False):
    # Q, K, V: (batch, heads, N, d_k)
    d_k = Q.size(-1)
    scores = (Q @ K.transpose(-2, -1)) / (d_k ** 0.5)   # (batch, heads, N, N)

    if causal:                                           # GPT: enforce the arrow of time
        N = scores.size(-1)
        mask = torch.triu(torch.ones(N, N, dtype=torch.bool), diagonal=1)
        scores = scores.masked_fill(mask, float("-inf"))
    # ViT: causal=False → no masking, attention is bidirectional

    weights = F.softmax(scores, dim=-1)                  # each query's weights sum to 1
    return weights @ V                                   # (batch, heads, N, d_k)
