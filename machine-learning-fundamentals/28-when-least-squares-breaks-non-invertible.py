"""
Machine Learning Fundamentals
Chapter 28: When Least Squares Breaks: Non-Invertible Matrices
Section: Linear Regression

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/when-least-squares-breaks-non-invertible

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

x1 = np.array([10., 20., 30., 40.])
x2 = 2 * x1 + np.array([0.001, -0.001, 0.001, -0.001])  # almost exactly 2·x1
X  = np.column_stack([x1, x2])
y  = np.array([5., 9., 14., 18.])

w_naive = np.linalg.inv(X.T @ X) @ X.T @ y   # explicit inverse of a near-singular matrix
print(w_naive)        # [ -585.7   293.1 ]  ← enormous, nonsense weights
