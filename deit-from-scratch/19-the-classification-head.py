"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 19: The Classification Head
Section: The ViT Backbone

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/the-classification-head

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
x = encoder(x)          # (B, 197, 384) -> (B, 197, 384)
cls_final = x[:, 0]     # (B, 384): keep ONLY position 0, the CLS token

# --- block 2 ---
import torch.nn as nn

D          = 384                  # DeiT-Small embedding width
NUM_CLASSES = 1000                # ImageNet-1k

norm = nn.LayerNorm(D)            # the FINAL norm, after the last block
head = nn.Linear(D, NUM_CLASSES) # 384 -> 1000

# forward:
cls_final = x[:, 0]              # (B, 384)
logits    = head(norm(cls_final)) # (B, 1000)
