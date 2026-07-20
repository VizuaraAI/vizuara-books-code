"""
Transformers: Theory, intuition, and Building from Scratch
Chapter 8: Other Positional Encodings
Section: Positional Encoding

Read this chapter: https://books.vizuara.ai/read/transformers-from-scratch/other-positional-encodings

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch.nn as nn

class LearnedPositionalEncoding(nn.Module):
    def __init__(self, max_len, d_model):
        super().__init__()
        self.pos = nn.Embedding(max_len, d_model)   # the whole trick

    def forward(self, x):                # x: (batch, seq_len, d_model)
        seq_len = x.size(1)
        positions = torch.arange(seq_len, device=x.device)
        return x + self.pos(positions)   # broadcast-add a learned vector per slot

# --- block 2 ---
import torch

def build_rope(seq_len, d, base=10000.0):
    # one angle per (position, pair): shape (seq_len, d//2)
    theta = base ** (-torch.arange(0, d, 2).float() / d)   # d/2 frequencies
    pos = torch.arange(seq_len).float()
    angles = torch.outer(pos, theta)                       # (seq_len, d//2)
    return angles.cos(), angles.sin()

def apply_rope(x, cos, sin):        # x: (batch, heads, seq_len, d)
    x1, x2 = x[..., 0::2], x[..., 1::2]          # even / odd coords -> the pairs
    # rotate each pair (x1, x2) by its position's angle
    rot_even = x1 * cos - x2 * sin
    rot_odd  = x1 * sin + x2 * cos
    out = torch.empty_like(x)
    out[..., 0::2], out[..., 1::2] = rot_even, rot_odd
    return out
