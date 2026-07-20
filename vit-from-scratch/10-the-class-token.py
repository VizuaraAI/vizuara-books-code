"""
Build a Vision Transformer (ViT) from Scratch
Chapter 10: The [CLS] Class Token
Section: Turning Images into Tokens

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/the-class-token

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

# one learnable vector of length D, stored with two leading
# dims so it broadcasts cleanly across the batch.
self.cls_token = nn.Parameter(torch.zeros(1, 1, D))   # shape (1, 1, 768)

# --- block 2 ---
def forward(self, x):                 # x: (B, 196, 768) from PatchEmbedding
    B = x.shape[0]
    # expand the single token to one copy per image in the batch
    cls = self.cls_token.expand(B, -1, -1)   # (B, 1, 768)
    x = torch.cat([cls, x], dim=1)           # (B, 197, 768)  -- CLS is now token 0
    return x

# --- block 3 ---
encoded = encoder(x)        # (1, 5, 8)   -- toy sizes
cls_out = encoded[:, 0]     # (1, 8)      -- the class-token state, row 0
logits  = head(cls_out)     # (1, num_classes)
