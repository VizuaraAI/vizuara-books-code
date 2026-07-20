"""
Machine Learning Fundamentals
Chapter 24: Implementing Regularization for Logistic Regression
Section: Logistic Regression and Optimization

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/regularization-for-logistic-regression

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def cost_and_grad(X, y, w, b, lam):
    n = X.shape[0]
    yhat = sigmoid(X @ w + b)                       # predicted probabilities, shape (n,)

    # --- data-fit (cross-entropy), plus the L2 penalty on w only ---
    eps  = 1e-12                                     # guard log(0)
    fit  = -np.mean(y*np.log(yhat+eps) + (1-y)*np.log(1-yhat+eps))
    cost = fit + (lam/2.0) * np.dot(w, w)           # + (λ/2)·‖w‖²   <-- ADDED

    # --- gradients: fit term + λ·w on the weights, nothing on the bias ---
    err  = yhat - y                                 # (prediction − target)
    dw   = (X.T @ err) / n + lam * w                # + λ·w           <-- ADDED
    db   = np.mean(err)                             # bias: unchanged
    return cost, dw, db
