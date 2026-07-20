"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 35: Regularization: Stochastic Depth and More
Section: Training DeiT

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/regularization-stochastic-depth-and-more

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch, torch.nn.functional as F

# 5 classes, true label = 2, epsilon = 0.1  (DeiT uses 0.1 on 1000 classes)
K, eps, true = 5, 0.1, 2
smooth = torch.full((K,), eps / K)      # every class starts at 0.02
smooth[true] += 1.0 - eps               # correct class → 0.92
# smooth = [0.02, 0.02, 0.92, 0.02, 0.02], sums to 1.0

# In practice you never build this by hand — it is one argument:
loss = F.cross_entropy(logits, target, label_smoothing=0.1)

# --- block 2 ---
# one residual sublayer with stochastic depth, probability p to drop f
if self.training and torch.rand(1).item() < p:
    x = x                          # DROP: block is identity this step
else:
    x = x + f(x) / (1.0 - p)       # KEEP: scale up to preserve the mean
