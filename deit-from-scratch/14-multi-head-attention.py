"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 14: Multi-Head Attention
Section: Attention from Scratch

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/multi-head-attention

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):
    def __init__(self, dim=384, num_heads=6):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = dim // num_heads          # 384 // 6 = 64
        self.scale = self.head_dim ** -0.5        # 1/√64 = 0.125

        self.qkv = nn.Linear(dim, dim * 3)        # Q, K, V in one matmul
        self.proj = nn.Linear(dim, dim)           # W_O, mixes the heads

    def forward(self, x):                          # x: (B, N, 384)
        B, N, D = x.shape

        # 1. project, then split into (Q, K, V) and into heads
        qkv = self.qkv(x)                          # (B, N, 3*384)
        qkv = qkv.reshape(B, N, 3, self.num_heads, self.head_dim)
        qkv = qkv.permute(2, 0, 3, 1, 4)           # (3, B, heads, N, 64)
        q, k, v = qkv[0], qkv[1], qkv[2]           # each (B, 6, N, 64)

        # 2. scaled dot-product attention, per head
        attn = (q @ k.transpose(-2, -1)) * self.scale   # (B, 6, N, N)
        attn = attn.softmax(dim=-1)                     # each row sums to 1
        out = attn @ v                                   # (B, 6, N, 64)

        # 3. concat heads back to width D, then mix
        out = out.transpose(1, 2).reshape(B, N, D)       # (B, N, 384)
        return self.proj(out)                            # (B, N, 384)

# --- block 2 ---
mha = MultiHeadAttention(dim=384, num_heads=6)
x = torch.randn(1, 198, 384)     # DeiT: 196 patches + CLS + distill token
out = mha(x)
print(out.shape)                  # torch.Size([1, 198, 384])
