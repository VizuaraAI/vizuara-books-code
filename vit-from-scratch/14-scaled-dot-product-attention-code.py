"""
Build a Vision Transformer (ViT) from Scratch
Chapter 14: Coding Scaled Dot-Product Attention
Section: Attention Inside the ViT

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/scaled-dot-product-attention-code

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

torch.manual_seed(0)
Q = torch.randn(4, 8)   # 4 tokens, d_k = 8
K = torch.randn(4, 8)
V = torch.randn(4, 8)

scores = Q @ K.transpose(-2, -1)   # (4, 8) @ (8, 4) -> (4, 4)
print(scores.shape)                # torch.Size([4, 4])

# --- block 2 ---
import math

d_k = Q.shape[-1]              # 8
scores = scores / math.sqrt(d_k)   # divide by √8 ≈ 2.83

# --- block 3 ---
import torch.nn.functional as F

weights = F.softmax(scores, dim=-1)   # (4, 4), each row sums to 1
print(weights.sum(dim=-1))            # tensor([1., 1., 1., 1.])

# --- block 4 ---
row = torch.tensor([2.0, 0.0, 1.0, 0.0])
print(F.softmax(row, dim=-1))   # tensor([0.6103, 0.0826, 0.2245, 0.0826])

# --- block 5 ---
out = weights @ V   # (4, 4) @ (4, 8) -> (4, 8)
print(out.shape)    # torch.Size([4, 8])

# --- block 6 ---
import torch
import torch.nn.functional as F

def scaled_dot_product_attention(Q, K, V):
    # Q, K, V: (..., N, d_k)  — any leading batch/head dims
    d_k = Q.shape[-1]
    scores = Q @ K.transpose(-2, -1)        # (..., N, N)
    scores = scores / (d_k ** 0.5)          # scale by √d_k
    weights = F.softmax(scores, dim=-1)     # (..., N, N), rows sum to 1
    out = weights @ V                       # (..., N, d_k)
    return out, weights

# --- block 7 ---
B, h, N, d_k = 2, 12, 197, 64          # a real ViT-Base batch, all heads
Q = torch.randn(B, h, N, d_k)
K = torch.randn(B, h, N, d_k)
V = torch.randn(B, h, N, d_k)

out, weights = scaled_dot_product_attention(Q, K, V)
print(out.shape)                        # torch.Size([2, 12, 197, 64])
print(weights.shape)                    # torch.Size([2, 12, 197, 197])
print(torch.allclose(weights.sum(-1), torch.ones(B, h, N)))   # True
