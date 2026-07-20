"""
Build Large Language Models (LLMs) from Scratch
Chapter 11: Multi-head Attention - Part 1
Section: LLM Attention Mechanism

Read this chapter: https://books.vizuara.ai/read/build-llm-from-scratch/multi-head-attention-part-1

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

B, T, d_model, num_heads = 2, 4, 8, 2
head_dim = d_model // num_heads          # 8 // 2 = 4  (must divide evenly)

x = torch.randn(B, T, d_model)           # (2, 4, 8) token embeddings

W_q = nn.Linear(d_model, d_model, bias=False)
W_k = nn.Linear(d_model, d_model, bias=False)
W_v = nn.Linear(d_model, d_model, bias=False)

Q = W_q(x)                               # (2, 4, 8)  — all heads at once
K = W_k(x)
V = W_v(x)

# split the last dim (8) into (num_heads, head_dim) = (2, 4)
Q = Q.view(B, T, num_heads, head_dim)    # (2, 4, 2, 4)  — a relabel, no data moved
K = K.view(B, T, num_heads, head_dim)
V = V.view(B, T, num_heads, head_dim)

# bring heads to the front so each head is a clean (T, head_dim) matrix
Q = Q.transpose(1, 2)                    # (2, 2, 4, 4)  = (B, num_heads, T, head_dim)
K = K.transpose(1, 2)
V = V.transpose(1, 2)

# from here, ordinary attention runs per head — Part 2.
print(Q.shape)                           # torch.Size([2, 2, 4, 4])
