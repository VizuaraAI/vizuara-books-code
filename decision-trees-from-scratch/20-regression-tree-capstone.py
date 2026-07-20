"""
Build Decision Trees from Scratch
Chapter 20: Capstone: Fit and Read a Regression Tree
Section: Regression Trees

Read this chapter: https://books.vizuara.ai/read/decision-trees-from-scratch/regression-tree-capstone

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

X = np.array([
    [14, 40],   # cold, dry     → 40
    [18, 45],   # mild          → 35
    [22, 55],   # warm, humid   → 0
    [24, 65],   # warm, humid   → 30
    [27, 70],   # hot, humid    → 0
    [30, 40],   # hot, dry      → 45
])
y = np.array([40, 35, 0, 30, 0, 45])

tree = RegressionTree(max_depth=2)
tree.fit(X, y)

# --- block 2 ---
tree.predict(np.array([[20, 50]]))   # → array([37.5])
