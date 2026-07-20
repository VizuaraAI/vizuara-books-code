"""
Transformers for Vision & Multimodal LLMs
Chapter 11: Multi-Head Attention
Section: Attention From Scratch

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/multi-head-attention

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        assert d_model % num_heads == 0, "d_model must divide by num_heads"
        self.num_heads = num_heads
        self.d_k = d_model // num_heads          # per-head width

        self.W_q = nn.Linear(d_model, d_model, bias=False)
        self.W_k = nn.Linear(d_model, d_model, bias=False)
        self.W_v = nn.Linear(d_model, d_model, bias=False)
        self.W_o = nn.Linear(d_model, d_model)   # the head-mixing projection

    def _split_heads(self, x, B, n):             # (B, n, d_model) -> (B, h, n, d_k)
        return x.view(B, n, self.num_heads, self.d_k).transpose(1, 2)

    def forward(self, x):                        # x: (B, n, d_model)
        B, n, _ = x.shape
        Q = self._split_heads(self.W_q(x), B, n) # (B, h, n, d_k)
        K = self._split_heads(self.W_k(x), B, n)
        V = self._split_heads(self.W_v(x), B, n)

        scores = Q @ K.transpose(-2, -1)         # (B, h, n, n)
        scores = scores / self.d_k ** 0.5        # scale by 1/√d_k, per head!
        attn = torch.softmax(scores, dim=-1)     # softmax over KEYS
        ctx = attn @ V                           # (B, h, n, d_k)

        ctx = ctx.transpose(1, 2).contiguous()   # (B, n, h, d_k)
        ctx = ctx.view(B, n, self.num_heads * self.d_k)   # concat -> (B, n, d_model)
        return self.W_o(ctx)                     # (B, n, d_model)

# --- block 2 ---
x = torch.rand(1, 4, 8)                    # batch=1, 4 tokens, d_model=8
mha = MultiHeadAttention(d_model=8, num_heads=2)
print(mha(x).shape)                        # torch.Size([1, 4, 8])
