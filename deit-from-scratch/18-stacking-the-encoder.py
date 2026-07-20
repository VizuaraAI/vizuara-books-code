"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 18: Stacking the Encoder
Section: The ViT Backbone

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/stacking-the-encoder

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

class Encoder(nn.Module):
    def __init__(self, dim=384, depth=12, heads=6, mlp_ratio=4):
        super().__init__()
        # 12 SEPARATE blocks — one fresh Block() per layer, each with its own weights
        self.blocks = nn.ModuleList([
            Block(dim=dim, heads=heads, mlp_ratio=mlp_ratio)
            for _ in range(depth)
        ])
        self.norm = nn.LayerNorm(dim)      # final norm after the last block

    def forward(self, x):                  # x: (B, 198, 384)
        for block in self.blocks:
            x = block(x)                   # (B, 198, 384) -> (B, 198, 384)
        x = self.norm(x)                   # (B, 198, 384), normalised
        return x
