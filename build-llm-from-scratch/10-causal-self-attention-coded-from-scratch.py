"""
Build Large Language Models (LLMs) from Scratch
Chapter 10: Causal Self Attention - Coded from scratch
Section: LLM Attention Mechanism

Read this chapter: https://books.vizuara.ai/read/build-llm-from-scratch/causal-self-attention-coded-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 (COMMENTED OUT) ---
# NOTE: this block is prose in the book, not runnable code.
# It restates the attention score formula in maths notation; Q and K are
# symbols from the equation, not variables defined anywhere in the chapter.
# scores = Q @ K.T          # shape (T, T)

# --- block 2 ---
import torch

T = 4
allowed = torch.tril(torch.ones(T, T))   # lower-triangular ones
# tensor([[1., 0., 0., 0.],
#         [1., 1., 0., 0.],
#         [1., 1., 1., 0.],
#         [1., 1., 1., 1.]])

# --- block 3 ---
import torch
import torch.nn as nn

class CausalSelfAttention(nn.Module):
    def __init__(self, d_in, d_out, context_length):
        super().__init__()
        self.W_query = nn.Linear(d_in, d_out, bias=False)
        self.W_key   = nn.Linear(d_in, d_out, bias=False)
        self.W_value = nn.Linear(d_in, d_out, bias=False)
        self.d_out = d_out
        # register the mask as a buffer so it moves with the model (.to(device))
        # but is NOT a learnable parameter
        mask = torch.triu(torch.ones(context_length, context_length), diagonal=1)
        self.register_buffer("mask", mask.bool())   # True = forbidden (future)

    def forward(self, x):
        # x: (batch, T, d_in)
        b, T, _ = x.shape
        Q = self.W_query(x)                      # (b, T, d_out)
        K = self.W_key(x)                        # (b, T, d_out)
        V = self.W_value(x)                      # (b, T, d_out)

        scores = Q @ K.transpose(-2, -1)         # (b, T, T)
        scores = scores.masked_fill(             # overwrite the future with -inf
            self.mask[:T, :T], float('-inf'))
        weights = torch.softmax(
            scores / self.d_out**0.5, dim=-1)    # (b, T, T), rows sum to 1
        return weights @ V                       # (b, T, d_out)
