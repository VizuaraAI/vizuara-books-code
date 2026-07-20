"""
Machine Learning & Deep Learning Mastery
Chapter 8: Regression in Code
Section: Regression

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/regression-in-code

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

np.random.seed(0)                    # reproducible
n = 100
x = np.linspace(0, 5, n)             # 100 points from 0 to 5
true_b, true_w = 2.0, 3.0
noise = np.random.normal(0, 1.0, n)
y = true_b + true_w * x + noise      # y ≈ 2 + 3x + noise

# --- block 2 ---
X = np.column_stack([np.ones(n), x])   # shape (100, 2): [1, x]
print(X.shape)                          # (100, 2)
print(X[:3])                            # [[1, 0.0], [1, 0.05], [1, 0.10]]

# --- block 3 ---
def fit_ols(X, y):
    return np.linalg.inv(X.T @ X) @ X.T @ y   # β̂ = (XᵀX)⁻¹ Xᵀy

beta = fit_ols(X, y)
print(beta)          # ≈ [2.03, 2.98]  →  intercept ≈ 2, slope ≈ 3

# --- block 4 ---
x2 = 2 * x                                  # perfectly collinear with x
X_bad = np.column_stack([np.ones(n), x, x2]) # [1, x, 2x] — column 3 = 2 × column 2

beta_bad = np.linalg.inv(X_bad.T @ X_bad) @ X_bad.T @ y
# LinAlgError: Singular matrix

# --- block 5 ---
def fit_ridge(X, y, lam):
    p = X.shape[1]                            # number of columns
    I = np.eye(p)                             # identity, same size as XᵀX
    return np.linalg.inv(X.T @ X + lam * I) @ X.T @ y   # (XᵀX + λI)⁻¹ Xᵀy

beta_ridge = fit_ridge(X_bad, y, lam=1.0)
print(beta_ridge)     # runs cleanly — no LinAlgError

# --- block 6 ---
def fit_ols(X, y):        return np.linalg.inv(X.T @ X)              @ X.T @ y
def fit_ridge(X, y, lam): return np.linalg.inv(X.T @ X + lam*np.eye(X.shape[1])) @ X.T @ y
