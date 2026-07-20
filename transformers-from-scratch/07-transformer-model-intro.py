"""
Transformers: Theory, intuition, and Building from Scratch
Chapter 7: Transformer Model Intro
Section: Introduction to Transformers

Read this chapter: https://books.vizuara.ai/read/transformers-from-scratch/transformer-model-intro

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch.nn as nn

# --- block 1 ---
class TransformerBlock(nn.Module):
    def __init__(self, d_model, n_heads, d_ff):
        super().__init__()
        self.attn = MultiHeadAttention(d_model, n_heads)
        self.ffn  = nn.Sequential(
            nn.Linear(d_model, d_ff), nn.GELU(),
            nn.Linear(d_ff, d_model),
        )
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)

    def forward(self, x, mask=None):
        # pre-norm: normalize, run sublayer, then ADD back the input (residual)
        x = x + self.attn(self.norm1(x), mask=mask)   # mix across tokens
        x = x + self.ffn(self.norm2(x))               # think per token
        return x                                       # shape unchanged: (seq_len, d_model)

# a "transformer" is just N of these in a row
blocks = nn.ModuleList([TransformerBlock(512, 8, 2048) for _ in range(6)])
