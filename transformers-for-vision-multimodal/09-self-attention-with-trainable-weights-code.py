"""
Transformers for Vision & Multimodal LLMs
Chapter 9: Self-Attention With Trainable Weights
Section: Attention From Scratch

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/self-attention-with-trainable-weights-code

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

class SelfAttention(nn.Module):
    def __init__(self, d_in, d_k):
        super().__init__()
        # the ONLY trainable parameters in the block
        self.W_q = nn.Linear(d_in, d_k, bias=False)
        self.W_k = nn.Linear(d_in, d_k, bias=False)
        self.W_v = nn.Linear(d_in, d_k, bias=False)
        self.d_k = d_k

    def forward(self, x):                    # x: (batch, n, d_in)
        Q = self.W_q(x)                      # (batch, n, d_k)
        K = self.W_k(x)                      # (batch, n, d_k)
        V = self.W_v(x)                      # (batch, n, d_k)

        scores = Q @ K.transpose(-2, -1)     # (batch, n, n)
        scores = scores / self.d_k ** 0.5    # scale by 1/√d_k
        attn = torch.softmax(scores, dim=-1) # softmax over KEYS
        return attn @ V                      # (batch, n, d_k)

# --- block 2 ---
x = torch.rand(1, 4, 8)          # batch=1, 4 tokens, d_in=8
layer = SelfAttention(d_in=8, d_k=4)
out = layer(x)
print(out.shape)                 # torch.Size([1, 4, 4])  →  (batch, n, d_k)
