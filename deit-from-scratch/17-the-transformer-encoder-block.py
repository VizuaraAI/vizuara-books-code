"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 17: The Transformer Encoder Block
Section: The ViT Backbone

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/the-transformer-encoder-block

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch.nn as nn

class EncoderBlock(nn.Module):
    def __init__(self, dim=384, num_heads=6, mlp_ratio=4):
        super().__init__()
        self.norm1 = nn.LayerNorm(dim)                    # before attention
        self.attn  = MultiHeadAttention(dim, num_heads)   # mix across tokens
        self.norm2 = nn.LayerNorm(dim)                    # before the MLP
        self.mlp   = MLP(dim, mlp_ratio)                  # 384 -> 1536 -> 384

    def forward(self, x):                # x: (B, N, 384)
        x = x + self.attn(self.norm1(x)) # pre-norm attention + residual
        x = x + self.mlp(self.norm2(x))  # pre-norm MLP + residual
        return x                         # (B, N, 384) — unchanged shape

# --- block 2 ---
import torch

block = EncoderBlock(dim=384, num_heads=6, mlp_ratio=4)

x = torch.randn(2, 198, 384)     # (B, N, D): 2 images, 198 tokens, width 384
y = block(x)

print(y.shape)                   # torch.Size([2, 198, 384])
assert y.shape == x.shape        # the invariant that lets blocks stack
print(sum(p.numel() for p in block.parameters()))   # 1774464
