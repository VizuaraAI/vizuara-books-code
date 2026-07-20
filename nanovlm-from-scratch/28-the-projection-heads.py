"""
Build a NanoVLM from Scratch
Chapter 28: The Projection Heads
Section: Building the NanoVLM

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/the-projection-heads

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn
import torch.nn.functional as F

class ProjectionHead(nn.Module):
    """Map a tower's raw feature vector into the shared space R^d."""
    def __init__(self, in_features: int, d: int):
        super().__init__()
        self.proj = nn.Linear(in_features, d, bias=False)   # W: (d, in_features)

    def forward(self, x):                    # x: (batch, in_features)
        z = self.proj(x)                     # (batch, d)  -- rotate + remix
        return F.normalize(z, dim=-1)        # (batch, d)  -- onto the unit sphere

# one head per tower, different input widths, SAME output d
D = 128
image_head = ProjectionHead(in_features=768, d=D)   # W is (128, 768)
text_head  = ProjectionHead(in_features=512, d=D)   # W is (128, 512)
