"""
Build a Vision Transformer (ViT) from Scratch
Chapter 19: The MLP Feed-Forward Block
Section: The Transformer Encoder Block

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/the-mlp-feedforward-block

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self, dim=768, mlp_dim=3072, dropout=0.0):
        super().__init__()
        self.fc1  = nn.Linear(dim, mlp_dim)   # 768 -> 3072  (expand)
        self.act  = nn.GELU()                  # the nonlinearity
        self.fc2  = nn.Linear(mlp_dim, dim)   # 3072 -> 768  (contract)
        self.drop = nn.Dropout(dropout)

    def forward(self, x):                      # x: (B, N+1, D) = (B, 197, 768)
        x = self.fc1(x)                        # (B, 197, 3072)
        x = self.act(x)                        # (B, 197, 3072)
        x = self.drop(x)
        x = self.fc2(x)                        # (B, 197, 768)
        x = self.drop(x)
        return x                               # (B, 197, 768) — shape preserved

# --- block 2 ---
x = x + self.mlp(self.norm2(x))   # pre-norm + residual around the MLP
