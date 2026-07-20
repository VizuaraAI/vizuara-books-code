"""
Build Large Language Models (LLMs) from Scratch - shared context.

Several chapters use names that the book defines in an EARLIER chapter and
does not repeat. This module holds those definitions, COPIED VERBATIM from
the chapter that first introduces them, so that a later chapter file can do

    from context import MultiHeadAttention

and still be reading exactly the code the book printed.

Nothing here is invented. Every definition below is followed by a comment
naming the chapter and block it was copied from.
"""

import numpy as np
import torch
import torch.nn as nn
from torch.nn import GELU  # the class `FeedForward` (ch. 16, block 3) calls


# ---------------------------------------------------------------------------
# From chapter 4 "What are transformers?", block 1
# https://books.vizuara.ai/read/build-llm-from-scratch/what-are-transformers
# ---------------------------------------------------------------------------
def softmax(x, axis=-1):
    e = np.exp(x - x.max(axis=axis, keepdims=True))
    return e / e.sum(axis=axis, keepdims=True)


# ---------------------------------------------------------------------------
# From chapter 12 "Multi-head Attention - Part 2", block 2
# https://books.vizuara.ai/read/build-llm-from-scratch/multi-head-attention-part-2
# ---------------------------------------------------------------------------
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


# ---------------------------------------------------------------------------
# From chapter 16 "Layer Norm, GELU, and Shortcut Connections", block 1
# https://books.vizuara.ai/read/build-llm-from-scratch/layer-norm-gelu-and-shortcut-connections
# ---------------------------------------------------------------------------
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


# ---------------------------------------------------------------------------
# From chapter 16 "Layer Norm, GELU, and Shortcut Connections", block 2
# ---------------------------------------------------------------------------
def gelu(x):
    return 0.5 * x * (1.0 + torch.tanh(
        torch.sqrt(torch.tensor(2.0 / torch.pi)) *
        (x + 0.044715 * torch.pow(x, 3))
    ))


# ---------------------------------------------------------------------------
# From chapter 16 "Layer Norm, GELU, and Shortcut Connections", block 3
# NOTE: the book's block calls `GELU()` (a module class) even though this
# chapter defines `gelu` (a function) just above it. Copied verbatim; the
# `GELU` name is resolved by the torch.nn import at the top of this file.
# ---------------------------------------------------------------------------
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


# ---------------------------------------------------------------------------
# From chapter 17 "Coding the Transformer Block and the 124M GPT-2", block 1
# https://books.vizuara.ai/read/build-llm-from-scratch/coding-the-transformer-block-and-gpt-2
# ---------------------------------------------------------------------------
GPT_CONFIG_124M = {
    "vocab_size": 50257,   # BPE tokenizer vocabulary
    "context_length": 1024, # max tokens the model can see at once
    "emb_dim": 768,        # width of every token vector (d_model)
    "n_heads": 12,         # attention heads per block
    "n_layers": 12,        # number of transformer blocks
    "drop_rate": 0.1,      # dropout probability
    "qkv_bias": False      # no bias on the Q/K/V projections
}


# ---------------------------------------------------------------------------
# From chapter 17 "Coding the Transformer Block and the 124M GPT-2", block 2
# ---------------------------------------------------------------------------
class TransformerBlock(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.att = MultiHeadAttention(
            d_in=cfg["emb_dim"], d_out=cfg["emb_dim"],
            context_length=cfg["context_length"],
            num_heads=cfg["n_heads"], dropout=cfg["drop_rate"],
            qkv_bias=cfg["qkv_bias"])
        self.ff = FeedForward(cfg)
        self.norm1 = LayerNorm(cfg["emb_dim"])
        self.norm2 = LayerNorm(cfg["emb_dim"])
        self.drop = nn.Dropout(cfg["drop_rate"])

    def forward(self, x):
        shortcut = x                      # (1) save residual
        x = self.norm1(x)                 # (2) normalize
        x = self.att(x)                   # (2) attention sublayer
        x = self.drop(x)
        x = x + shortcut                  # (3) add shortcut back

        shortcut = x                      # repeat for feed-forward
        x = self.norm2(x)
        x = self.ff(x)
        x = self.drop(x)
        x = x + shortcut
        return x


# ---------------------------------------------------------------------------
# From chapter 17 "Coding the Transformer Block and the 124M GPT-2", block 3
# ---------------------------------------------------------------------------
class GPTModel(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.tok_emb = nn.Embedding(cfg["vocab_size"], cfg["emb_dim"])   # 50257 x 768
        self.pos_emb = nn.Embedding(cfg["context_length"], cfg["emb_dim"]) # 1024 x 768
        self.drop_emb = nn.Dropout(cfg["drop_rate"])
        self.trf_blocks = nn.Sequential(
            *[TransformerBlock(cfg) for _ in range(cfg["n_layers"])])     # 12 blocks
        self.final_norm = LayerNorm(cfg["emb_dim"])
        self.out_head = nn.Linear(cfg["emb_dim"], cfg["vocab_size"], bias=False) # 768 -> 50257

    def forward(self, in_idx):
        batch, seq_len = in_idx.shape
        tok = self.tok_emb(in_idx)                                   # (b, seq, 768)
        pos = self.pos_emb(torch.arange(seq_len, device=in_idx.device))
        x = self.drop_emb(tok + pos)                                 # add position signal
        x = self.trf_blocks(x)                                       # 12 blocks refine x
        x = self.final_norm(x)
        logits = self.out_head(x)                                    # (b, seq, 50257)
        return logits
