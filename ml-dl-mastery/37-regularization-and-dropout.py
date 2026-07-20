"""
Machine Learning & Deep Learning Mastery
Chapter 37: Regularization and Dropout in Neural Nets
Section: Optimizers & Training

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/regularization-and-dropout

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
# NOTE: this block is prose in the book, not runnable code.
# The L2 objective in maths notation; y, X, w and lam are symbols in a
# formula, and mse() is never defined anywhere in the book.
# # L2 / ridge objective
# loss = mse(y, X @ w) + lam * np.sum(w ** 2)   # penalize ||w||^2

# --- block 2 ---
# NOTE: this block is prose in the book, not runnable code.
# The L1 objective, same notation, same undefined mse().
# # L1 / lasso objective
# loss = mse(y, X @ w) + lam * np.sum(np.abs(w))   # penalize ||w||_1

# --- block 3 ---
def dropout_forward(a, p=0.5, training=True):
    if not training:
        return a                          # test time: use the full network
    mask = (np.random.rand(*a.shape) > p) # keep with prob (1 - p)
    return a * mask / (1 - p)             # zero some, scale the rest up
