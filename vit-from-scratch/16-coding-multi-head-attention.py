"""
Build a Vision Transformer (ViT) from Scratch
Chapter 16: Coding Multi-Head Attention
Section: Attention Inside the ViT

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/coding-multi-head-attention

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, emb_dim=768, num_heads=12):
        super().__init__()
        assert emb_dim % num_heads == 0, "D must be divisible by h"
        self.num_heads = num_heads
        self.d_k = emb_dim // num_heads          # 768 // 12 = 64

        self.W_q = nn.Linear(emb_dim, emb_dim)   # D -> D, shared across heads
        self.W_k = nn.Linear(emb_dim, emb_dim)
        self.W_v = nn.Linear(emb_dim, emb_dim)
        self.W_o = nn.Linear(emb_dim, emb_dim)   # output projection

    def forward(self, x):
        B, N, D = x.shape

        # 1. project, then split D -> (h, d_k) and lift head axis to front
        def split_heads(t):
            t = t.view(B, N, self.num_heads, self.d_k)   # (B, N, h, d_k)
            return t.transpose(1, 2)                      # (B, h, N, d_k)

        Q = split_heads(self.W_q(x))
        K = split_heads(self.W_k(x))
        V = split_heads(self.W_v(x))

        # 2. scaled dot-product attention, per head, in parallel
        scores = (Q @ K.transpose(-2, -1)) / (self.d_k ** 0.5)  # (B, h, N, N)
        weights = scores.softmax(dim=-1)
        out = weights @ V                                       # (B, h, N, d_k)

        # 3. concat heads back to width D, then project
        out = out.transpose(1, 2).contiguous()   # (B, N, h, d_k)
        out = out.reshape(B, N, D)               # (B, N, D)  <- concat
        return self.W_o(out)

# --- block 2 ---
torch.manual_seed(0)
mha = MultiHeadAttention(emb_dim=4, num_heads=2)

x = torch.randn(1, 2, 4)        # (B, N, D)
out = mha(x)

print(out.shape)                # torch.Size([1, 2, 4])
print(out.shape == x.shape)     # True

# --- block 3 ---
mha = MultiHeadAttention()              # emb_dim=768, num_heads=12
x = torch.randn(8, 197, 768)            # (B, N, D): 197 = 196 patches + CLS
out = mha(x)

print(out.shape)                        # torch.Size([8, 197, 768])

n_params = sum(p.numel() for p in mha.parameters())
print(n_params)                         # 2,362,368
