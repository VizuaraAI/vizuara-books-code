"""
Build Decision Trees from Scratch
Chapter 16: Building the First Regression Split
Section: Regression Trees

Read this chapter: https://books.vizuara.ai/read/decision-trees-from-scratch/starting-a-regression-tree

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def ssr(y):
    # y: 1-D array of target values in one node
    if len(y) == 0:
        return 0.0
    return np.sum((y - y.mean()) ** 2)      # Σ (yᵢ − ȳ)²

def best_regression_split(x, y):
    # x: numeric feature column, y: continuous target (aligned)
    values = np.unique(x)                    # sorted, distinct
    best_t, best_score = None, np.inf
    for a, b in zip(values[:-1], values[1:]):
        t = (a + b) / 2                      # midpoint threshold
        left, right = y[x <= t], y[x > t]
        score = ssr(left) + ssr(right)       # NOTE: a sum, not a weighted average
        if score < best_score:               # keep the LOWEST total SSR
            best_score, best_t = score, t
    return best_t, best_score
