"""
Transformers for Vision & Multimodal LLMs
Chapter 17: Coding DeiT From Scratch
Section: The Vision Transformer

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/coding-deit-from-scratch

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
import torch.nn.functional as F

# --- block 1 ---
# --- new in DeiT, on top of the ViT you already built ---
self.dist_token = nn.Parameter(torch.zeros(1, 1, D))      # the extra read-out
self.pos_embed  = nn.Parameter(torch.zeros(1, num_patches + 2, D))  # was +1, now +2
self.dist_head  = nn.Linear(D, num_classes)               # its own classifier

# --- block 2 ---
def forward_features(self, x):
    x = self.patch_embed(x)                       # (B, N, D)
    cls  = self.cls_token.expand(x.shape[0], -1, -1)
    dist = self.dist_token.expand(x.shape[0], -1, -1)
    x = torch.cat((cls, x, dist), dim=1)          # (B, N+2, D)
    x = x + self.pos_embed                        # positions for all N+2 tokens
    x = self.blocks(x)                            # unchanged ViT encoder
    return x[:, 0], x[:, -1]                       # cls output, dist output

# --- block 3 ---
teacher.eval()
with torch.no_grad():
    teacher_logits = teacher(images)              # frozen CNN
    teacher_labels = teacher_logits.argmax(dim=1) # hard labels

cls_logits, dist_logits = student(images)         # two heads
loss = 0.5 * F.cross_entropy(cls_logits,  labels) \
     + 0.5 * F.cross_entropy(dist_logits, teacher_labels)
loss.backward()
