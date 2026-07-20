"""
Machine Learning Fundamentals
Chapter 27: Ridge Regression: Regularizing the Fit
Section: Linear Regression

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/ridge-regression

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

# X: (n, d) design matrix, y: (n,) targets, lam: λ >= 0
d = X.shape[1]
I = np.eye(d)

w_ols   = np.linalg.inv(X.T @ X)          @ X.T @ y   # fails if X.T @ X is singular
w_ridge = np.linalg.inv(X.T @ X + lam*I)  @ X.T @ y   # always works for lam > 0
