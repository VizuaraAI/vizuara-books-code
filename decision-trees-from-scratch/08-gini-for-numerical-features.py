"""
Build Decision Trees from Scratch
Chapter 8: Gini Impurity for Numerical Features
Section: Classification Trees

Read this chapter: https://books.vizuara.ai/read/decision-trees-from-scratch/gini-for-numerical-features

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def gini(labels):
    # labels: 1-D array of class values in one node
    if len(labels) == 0:
        return 0.0
    _, counts = np.unique(labels, return_counts=True)
    p = counts / counts.sum()
    return 1.0 - np.sum(p ** 2)          # 1 − Σ pₖ²

def best_numeric_split(x, y):
    # x: numeric feature column, y: class labels (aligned)
    values = np.unique(x)                # sorted, distinct
    n = len(y)
    best_t, best_score = None, np.inf
    for a, b in zip(values[:-1], values[1:]):
        t = (a + b) / 2                  # midpoint threshold
        left, right = y[x <= t], y[x > t]
        score = (len(left)/n) * gini(left) + (len(right)/n) * gini(right)
        if score < best_score:           # keep the LOWEST weighted Gini
            best_score, best_t = score, t
    return best_t, best_score
