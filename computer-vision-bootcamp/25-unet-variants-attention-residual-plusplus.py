"""
Computer Vision Bootcamp
Chapter 25: U-Net Variants: Attention, Residual, U-Net++
Section: Semantic Segmentation with U-Net

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/unet-variants-attention-residual-plusplus

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch

# --- block 1 ---
import torch.nn as nn

class AttentionGate(nn.Module):
    def __init__(self, ch):
        super().__init__()
        self.wx = nn.Conv2d(ch, ch, 1)   # transform skip feature x
        self.wg = nn.Conv2d(ch, ch, 1)   # transform gating signal g
        self.psi = nn.Sequential(        # collapse to a 1-channel map
            nn.Conv2d(ch, 1, 1), nn.Sigmoid())

    def forward(self, x, g):
        a = torch.relu(self.wx(x) + self.wg(g))  # additive attention
        alpha = self.psi(a)                      # (B, 1, H, W) in [0,1]
        return x * alpha                         # gated skip
