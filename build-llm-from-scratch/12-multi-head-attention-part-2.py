"""
Build Large Language Models (LLMs) from Scratch
Chapter 12: Multi-head Attention - Part 2
Section: LLM Attention Mechanism

Read this chapter: https://books.vizuara.ai/read/build-llm-from-scratch/multi-head-attention-part-2

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added to make this file runnable) ---
# Block 1 uses `nn` but the chapter only repeats the import line in block 2.
import torch.nn as nn

# --- stubs (not book code) ---
# Block 1 instantiates `SingleHeadAttention`, a name the book never defines.
# The class with this exact signature is `CausalSelfAttention` in chapter 10
# (https://books.vizuara.ai/read/build-llm-from-scratch/causal-self-attention-coded-from-scratch);
# it is NOT aliased here because the book does not say they are the same thing.
SingleHeadAttention = None  # TODO: supply the single-head attention class

# --- block 1 ---
class MultiHeadAttentionNaive(nn.Module):
    def __init__(self, d_in, d_out, num_heads, context_length):
        super().__init__()
        assert d_out % num_heads == 0
        self.heads = nn.ModuleList([
            SingleHeadAttention(d_in, d_out // num_heads, context_length)
            for _ in range(num_heads)
        ])

    def forward(self, x):                       # x: (B, T, d_in)
        return torch.cat([head(x) for head in self.heads], dim=-1)

# --- block 2 ---
import torch
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, d_in, d_out, context_length, num_heads, dropout=0.0):
        super().__init__()
        assert d_out % num_heads == 0, "d_out must divide evenly into heads"
        self.d_out = d_out
        self.num_heads = num_heads
        self.head_dim = d_out // num_heads          # e.g. 768 // 12 = 64

        self.W_query = nn.Linear(d_in, d_out, bias=False)
        self.W_key   = nn.Linear(d_in, d_out, bias=False)
        self.W_value = nn.Linear(d_in, d_out, bias=False)
        self.out_proj = nn.Linear(d_out, d_out)     # the mixing matrix W_out
        self.dropout = nn.Dropout(dropout)
        self.register_buffer(
            "mask",
            torch.triu(torch.ones(context_length, context_length), diagonal=1)
        )

    def forward(self, x):                           # x: (B, T, d_in)
        B, T, _ = x.shape

        queries = self.W_query(x)                   # (B, T, d_out)
        keys    = self.W_key(x)
        values  = self.W_value(x)

        # split the d_out axis into (num_heads, head_dim)
        queries = queries.view(B, T, self.num_heads, self.head_dim)
        keys    = keys.view(B, T, self.num_heads, self.head_dim)
        values  = values.view(B, T, self.num_heads, self.head_dim)

        # lift heads into a batch dimension: (B, num_heads, T, head_dim)
        queries = queries.transpose(1, 2)
        keys    = keys.transpose(1, 2)
        values  = values.transpose(1, 2)

        # scaled dot-product attention, all heads at once
        scores = queries @ keys.transpose(-2, -1)   # (B, num_heads, T, T)
        scores = scores.masked_fill(
            self.mask.bool()[:T, :T], float("-inf")
        )
        weights = torch.softmax(scores / self.head_dim**0.5, dim=-1)
        weights = self.dropout(weights)

        context = weights @ values                  # (B, num_heads, T, head_dim)

        # reassemble heads: (B, T, num_heads, head_dim) -> (B, T, d_out)
        context = context.transpose(1, 2).contiguous().view(B, T, self.d_out)

        return self.out_proj(context)               # (B, T, d_out)
