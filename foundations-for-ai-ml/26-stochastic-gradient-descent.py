"""
Foundations for AI & ML
Chapter 26: Stochastic Gradient Descent
Section: Optimization & Neural Networks

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/stochastic-gradient-descent

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def sgd_epoch(params, X, y, grad_fn, lr=0.01, batch_size=32):
    N = X.shape[0]                      # e.g. 60000
    idx = np.random.permutation(N)      # 1. shuffle once per epoch
    for start in range(0, N, batch_size):
        batch = idx[start:start + batch_size]   # 2. next mini-batch of indices
        Xb, yb = X[batch], y[batch]             # e.g. shapes (32, 784), (32,)
        g = grad_fn(params, Xb, yb)             # 3. average gradient over the batch
        params = params - lr * g                # 4. one step per batch
    return params
