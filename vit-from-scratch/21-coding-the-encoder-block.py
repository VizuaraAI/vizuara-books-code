"""
Build a Vision Transformer (ViT) from Scratch
Chapter 21: Coding One Encoder Block
Section: The Transformer Encoder Block

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/coding-the-encoder-block

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self, dim, mlp_dim, dropout=0.0):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(dim, mlp_dim),   # up-project: D -> 4D
            nn.GELU(),                 # smooth non-linearity
            nn.Dropout(dropout),
            nn.Linear(mlp_dim, dim),   # down-project: 4D -> D
            nn.Dropout(dropout),
        )

    def forward(self, x):
        return self.net(x)

class TransformerEncoderBlock(nn.Module):
    def __init__(self, dim, heads, mlp_dim, dropout=0.0):
        super().__init__()
        self.norm1 = nn.LayerNorm(dim)
        self.attn  = MultiHeadAttention(dim, heads, dropout=dropout)
        self.norm2 = nn.LayerNorm(dim)
        self.mlp   = MLP(dim, mlp_dim, dropout=dropout)

    def forward(self, x):
        # pre-norm: normalize INSIDE each sublayer, add back the raw x
        x = x + self.attn(self.norm1(x))   # communicate across tokens
        x = x + self.mlp(self.norm2(x))    # compute per token
        return x

# --- block 2 ---
block = TransformerEncoderBlock(dim=8, heads=2, mlp_dim=32)
x = torch.randn(1, 4, 8)          # (B, N, D)
out = block(x)
print(out.shape)                   # torch.Size([1, 4, 8])
assert out.shape == x.shape
