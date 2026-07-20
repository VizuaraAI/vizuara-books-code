"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 40: Reproducing the Paper Results
Section: Putting It Together

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/reproducing-the-paper-results

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch.nn.functional as F

# --- block 1 ---
# y      : true label      -> supervises the CLS head
# y_t    : teacher argmax   -> supervises the DIST head, y_t = teacher(x).argmax(-1)
# z_cls, z_dist: the two student logit vectors from the two-head forward pass
loss = 0.5 * F.cross_entropy(z_cls,  y) \
     + 0.5 * F.cross_entropy(z_dist, y_t)

# --- block 2 ---
import torch
z_cls  = torch.tensor([2.1, 1.9, 0.2])   # [cat, lynx, dog]  — nearly a tie
z_dist = torch.tensor([2.8, 1.0, 0.1])   # [cat, lynx, dog]  — confident: cat

fused = z_cls + z_dist                     # tensor([4.9, 2.9, 0.3])
print(fused.argmax())                      # -> 0  (cat)
