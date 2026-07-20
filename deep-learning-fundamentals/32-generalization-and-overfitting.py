"""
Deep Learning Fundamentals
Chapter 32: Testing, generalization, and overfitting
Section: Regularization and Testing

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/generalization-and-overfitting

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def train_test_split(X, y, test_frac=0.2, seed=0):
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(X))          # 1. shuffle the row order
    cut = int(len(X) * (1 - test_frac))    # 2. 80% mark
    train_idx, test_idx = idx[:cut], idx[cut:]
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]
