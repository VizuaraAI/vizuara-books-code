"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 31: The Two-Head Forward Pass
Section: The Distillation Token

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/the-two-head-forward-pass

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
x = encoder(x)          # (B, 198, 384) -> (B, 198, 384)
cls_final  = x[:, 0]    # (B, 384): the CLS token summary
dist_final = x[:, 1]    # (B, 384): the distillation token summary

# --- block 2 ---
import torch.nn as nn

D           = 384      # DeiT-Small embedding width
NUM_CLASSES = 1000     # ImageNet-1k

norm      = nn.LayerNorm(D)              # shared final norm (see note)
head_cls  = nn.Linear(D, NUM_CLASSES)   # CLS head:  384 -> 1000
head_dist = nn.Linear(D, NUM_CLASSES)   # DIST head: 384 -> 1000, separate weights

# --- block 3 ---
cls_logits  = head_cls(norm(cls_final))    # (B, 1000)
dist_logits = head_dist(norm(dist_final))  # (B, 1000)

# --- block 4 ---
class DeiTHead(nn.Module):
    def __init__(self, D=384, num_classes=1000):
        super().__init__()
        self.norm      = nn.LayerNorm(D)
        self.head_cls  = nn.Linear(D, num_classes)
        self.head_dist = nn.Linear(D, num_classes)

    def forward(self, x):                 # x: (B, 198, 384) from the encoder
        x = self.norm(x)                  # normalize the whole sequence, then slice
        cls_logits  = self.head_cls(x[:, 0])   # (B, 1000)
        dist_logits = self.head_dist(x[:, 1])  # (B, 1000)

        if self.training:
            return cls_logits, dist_logits          # two answers -> two losses
        return (cls_logits + dist_logits) / 2       # fused single prediction
