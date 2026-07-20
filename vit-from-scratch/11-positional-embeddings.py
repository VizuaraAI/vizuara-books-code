"""
Build a Vision Transformer (ViT) from Scratch
Chapter 11: Positional Embeddings
Section: Turning Images into Tokens

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/positional-embeddings

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# tokens:   (B, N+1, D)   patch tokens with the class token already prepended
# pos_embed: (1, N+1, D)  a learnable nn.Parameter, one row per position
x = tokens + pos_embed     # broadcast-add; result is still (B, N+1, D)

# --- block 2 ---
import torch
import torch.nn as nn

class PositionalEmbedding(nn.Module):
    def __init__(self, num_patches: int, embed_dim: int):
        super().__init__()
        # one learnable row per position, +1 for the class-token slot
        self.pos_embed = nn.Parameter(
            torch.zeros(1, num_patches + 1, embed_dim)
        )
        nn.init.trunc_normal_(self.pos_embed, std=0.02)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: (B, N+1, D) — class token already prepended
        return x + self.pos_embed          # broadcast over the batch
