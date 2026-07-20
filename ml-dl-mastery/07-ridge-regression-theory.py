"""
Machine Learning & Deep Learning Mastery
Chapter 7: Ridge Regression Theory
Section: Regression

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/ridge-regression-theory

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

X = np.array([[1.0, 1.001],
              [2.0, 2.002],
              [3.0, 3.001]])   # feature 2 ≈ feature 1
y = np.array([2.0, 4.0, 6.0])  # target is just 2 × feature 1

# --- block 2 ---
np.linalg.solve(X.T @ X, X.T @ y)              # → [ 2.000,  0.000 ]
y2 = np.array([2.01, 4.0, 6.0])                 # wiggle one label by 0.01
np.linalg.solve(X.T @ X, X.T @ y2)             # → [-1.001,  3.000 ]
