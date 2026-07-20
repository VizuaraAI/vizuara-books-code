"""
Transformers for Vision & Multimodal LLMs
Chapter 10: Masked (Causal) Self-Attention
Section: Attention From Scratch

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/masked-self-attention

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn.functional as F

def causal_self_attention(Q, K, V):
    # Q, K, V: (seq_len, d_k), already projected from X by W_q, W_k, W_v
    seq_len, d_k = Q.shape
    scores = Q @ K.transpose(-2, -1) / d_k ** 0.5    # (seq_len, seq_len)

    # 1 in the strictly-upper triangle (the future cells), 0 elsewhere
    future = torch.triu(torch.ones(seq_len, seq_len), diagonal=1).bool()

    scores = scores.masked_fill(future, float('-inf'))  # future → −∞ BEFORE softmax
    weights = F.softmax(scores, dim=-1)                  # each row sums to 1
    return weights @ V                                   # (seq_len, d_k)
