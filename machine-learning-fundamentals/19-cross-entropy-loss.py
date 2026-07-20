"""
Machine Learning Fundamentals
Chapter 19: Cross-Entropy Loss: Measuring Wrongness
Section: Logistic Regression and Optimization

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/cross-entropy-loss

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def binary_cross_entropy(y, y_hat, eps=1e-12):
    # y, y_hat are arrays of shape (n,); y_hat in (0, 1)
    y_hat = np.clip(y_hat, eps, 1 - eps)          # keep log() away from 0
    losses = -(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))
    return losses.mean()                           # the cost J
