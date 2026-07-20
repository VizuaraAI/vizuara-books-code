"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 34: Data Augmentation That Matters
Section: Training DeiT

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/data-augmentation-that-matters

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import numpy as np

# --- block 1 ---
lam = np.random.beta(alpha, alpha)   # alpha ~ 0.8 in DeiT; lam in [0, 1]
x = lam * x_A + (1 - lam) * x_B        # ghostly superposition of two photos
y = lam * y_A + (1 - lam) * y_B        # labels blend by the SAME lam
