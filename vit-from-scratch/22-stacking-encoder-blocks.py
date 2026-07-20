"""
Build a Vision Transformer (ViT) from Scratch
Chapter 22: Stacking the Encoder
Section: The Transformer Encoder Block

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/stacking-encoder-blocks

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

class TransformerEncoder(nn.Module):
    def __init__(self, depth=12, emb_dim=768, num_heads=12, mlp_dim=3072):
        super().__init__()
        self.blocks = nn.ModuleList([
            TransformerEncoderBlock(emb_dim, num_heads, mlp_dim)
            for _ in range(depth)          # depth SEPARATE blocks, own weights each
        ])

    def forward(self, x):                  # x: (B, N, D)
        for block in self.blocks:
            x = block(x)                   # (B, N, D) -> (B, N, D), reassigned each pass
        return x                           # (B, N, D)

# --- block 2 ---
enc = TransformerEncoder(depth=12, emb_dim=768, num_heads=12, mlp_dim=3072)
x = torch.randn(8, 197, 768)          # (B, N, D)
out = enc(x)
print(out.shape)                      # torch.Size([8, 197, 768])
assert out.shape == x.shape           # passes: depth preserves shape
