"""
Build Decision Trees from Scratch
Chapter 15: Variance and SSR as the Split Criterion
Section: Regression Trees

Read this chapter: https://books.vizuara.ai/read/decision-trees-from-scratch/variance-as-a-split-criterion

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def ssr(y):
    """Sum of squared residuals about the node's own mean."""
    if len(y) == 0:
        return 0.0
    return float(np.sum((y - y.mean()) ** 2))

def split_score(y_left, y_right):
    """Lower is better. Two children, no weighting needed — SSR is a total."""
    return ssr(y_left) + ssr(y_right)
