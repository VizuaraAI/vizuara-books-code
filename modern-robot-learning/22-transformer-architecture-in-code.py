"""
Modern Robot Learning
Chapter 22: The Transformer in Code
Section: Transformer Architecture from Scratch

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/transformer-architecture-in-code

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch, math

def positional_encoding(seq_len, d):
    pe = torch.zeros(seq_len, d)
    pos = torch.arange(seq_len).unsqueeze(1)               # (seq_len, 1)
    i   = torch.arange(0, d, 2)                             # even indices
    div = torch.pow(10000, i / d)                          # wavelengths
    pe[:, 0::2] = torch.sin(pos / div)                     # even dims -> sin
    pe[:, 1::2] = torch.cos(pos / div)                     # odd  dims -> cos
    return pe                                              # (seq_len, d)

# --- block 2 ---
import torch.nn as nn

class FeedForward(nn.Module):
    def __init__(self, d, hidden):          # canonically hidden = 4 * d
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d, hidden),           # (d) -> (4d): widen
            nn.ReLU(),                      # nonlinearity
            nn.Linear(hidden, d),           # (4d) -> (d): project back
        )
    def forward(self, x):
        return self.net(x)                  # same shape in, same shape out

# --- block 3 ---
class TransformerBlock(nn.Module):
    def __init__(self, d, n_heads, hidden):
        super().__init__()
        self.attn = nn.MultiheadAttention(d, n_heads, batch_first=True)
        self.ffn  = FeedForward(d, hidden)
        self.norm1 = nn.LayerNorm(d)
        self.norm2 = nn.LayerNorm(d)

    def forward(self, x):                          # x: (batch, seq_len, d)
        a, _ = self.attn(x, x, x)                  # self-attn: Q=K=V=x
        x = self.norm1(x + a)                      # 1. mix, then add + norm
        f = self.ffn(x)
        x = self.norm2(x + f)                      # 2. think, then add + norm
        return x                                   # (batch, seq_len, d) — unchanged

# --- block 4 ---
block = TransformerBlock(d=8, n_heads=2, hidden=32)
x = torch.randn(1, 4, 8)          # (batch=1, seq_len=4, d=8)
y = block(x)
print(y.shape)                     # torch.Size([1, 4, 8])
