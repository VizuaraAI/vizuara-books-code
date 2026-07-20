"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 30: Adding the Token to the Model
Section: The Distillation Token

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/adding-the-token-to-the-model

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch
import torch.nn as nn

# --- block 1 ---
self.cls_token  = nn.Parameter(torch.zeros(1, 1, embed_dim))   # (1, 1, 384)
self.dist_token = nn.Parameter(torch.zeros(1, 1, embed_dim))   # (1, 1, 384)

# --- block 2 ---
cls  = self.cls_token.expand(B, -1, -1)     # (B, 1, 384)
dist = self.dist_token.expand(B, -1, -1)    # (B, 1, 384)
x = torch.cat((cls, dist, x), dim=1)        # (B, 198, 384)  <- CLS at 0, DIST at 1
x = x + self.pos_embed                       # (B, 198, 384)

# --- block 3 ---
num_tokens = self.num_patches + 2            # 196 + 2 = 198
self.pos_embed = nn.Parameter(torch.zeros(1, num_tokens, embed_dim))  # (1, 198, 384)

# --- block 4 ---
x = patch_embed(images)        # (8, 3, 224, 224) -> (8, 198, 384)
for block in self.blocks:      # 12 pre-norm encoder blocks
    x = block(x)               # (8, 198, 384) -> (8, 198, 384), unchanged shape
x = self.norm(x)               # final LayerNorm, still (8, 198, 384)

cls_out  = x[:, 0]             # (8, 384): the CLS token's final vector
dist_out = x[:, 1]             # (8, 384): the distillation token's final vector
