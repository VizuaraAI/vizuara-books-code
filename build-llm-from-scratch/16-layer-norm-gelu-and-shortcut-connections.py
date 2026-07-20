"""
Build Large Language Models (LLMs) from Scratch
Chapter 16: Layer Norm, GELU, and Shortcut Connections
Section: LLM Architecture

Read this chapter: https://books.vizuara.ai/read/build-llm-from-scratch/layer-norm-gelu-and-shortcut-connections

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports / shared context (added to make this file runnable) ---
# Block 3 calls `GELU()` (the torch.nn module class) even though this chapter
# defines a `gelu` function in block 2.
from torch.nn import GELU
# `MultiHeadAttention` is defined in chapter 12 and reused here.
from context import MultiHeadAttention

# --- block 1 ---
import torch
import torch.nn as nn

class LayerNorm(nn.Module):
    def __init__(self, emb_dim, eps=1e-5):
        super().__init__()
        self.eps = eps
        self.scale = nn.Parameter(torch.ones(emb_dim))   # gamma
        self.shift = nn.Parameter(torch.zeros(emb_dim))  # beta

    def forward(self, x):
        mean = x.mean(dim=-1, keepdim=True)
        var = x.var(dim=-1, keepdim=True, unbiased=False)   # divide by n
        x_norm = (x - mean) / torch.sqrt(var + self.eps)
        return self.scale * x_norm + self.shift

# --- block 2 ---
import torch

def gelu(x):
    return 0.5 * x * (1.0 + torch.tanh(
        torch.sqrt(torch.tensor(2.0 / torch.pi)) *
        (x + 0.044715 * torch.pow(x, 3))
    ))

# --- block 3 ---
class FeedForward(nn.Module):
    def __init__(self, emb_dim):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(emb_dim, 4 * emb_dim),   # 768 -> 3072
            GELU(),
            nn.Linear(4 * emb_dim, emb_dim),   # 3072 -> 768
        )

    def forward(self, x):
        return self.layers(x)

# --- block 4 ---
class TransformerBlock(nn.Module):
    def __init__(self, emb_dim, n_heads, context_length, drop_rate):
        super().__init__()
        self.att = MultiHeadAttention(emb_dim, emb_dim, context_length,
                                      drop_rate, n_heads)
        self.ff = FeedForward(emb_dim)
        self.norm1 = LayerNorm(emb_dim)
        self.norm2 = LayerNorm(emb_dim)
        self.drop = nn.Dropout(drop_rate)

    def forward(self, x):
        # sublayer 1: attention, with pre-norm and a shortcut
        shortcut = x
        x = self.norm1(x)
        x = self.att(x)
        x = self.drop(x)
        x = x + shortcut          # add the input back

        # sublayer 2: feed-forward, with pre-norm and a shortcut
        shortcut = x
        x = self.norm2(x)
        x = self.ff(x)
        x = self.drop(x)
        x = x + shortcut          # add the input back
        return x
