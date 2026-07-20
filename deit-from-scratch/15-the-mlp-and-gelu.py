"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 15: The MLP Block and GELU
Section: Attention from Scratch

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/the-mlp-and-gelu

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self, dim=384, mlp_ratio=4):
        super().__init__()
        hidden = dim * mlp_ratio          # 384 * 4 = 1536
        self.fc1 = nn.Linear(dim, hidden) # (384 -> 1536)
        self.act = nn.GELU()              # the smooth gate
        self.fc2 = nn.Linear(hidden, dim) # (1536 -> 384)

    def forward(self, x):                 # x: (B, 198, 384)
        x = self.fc1(x)                   # (B, 198, 1536)
        x = self.act(x)                   # same shape, per-element GELU
        x = self.fc2(x)                   # (B, 198, 384)  back to D
        return x
