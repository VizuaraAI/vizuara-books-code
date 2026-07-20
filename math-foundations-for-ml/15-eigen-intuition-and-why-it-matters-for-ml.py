"""
Mathematical Foundations for Machine Learning
Chapter 15: Eigen-Intuition and Why It Matters for ML
Section: Determinants and the Shape of Space

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/eigen-intuition-and-why-it-matters-for-ml

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# NOTE: this block is prose in the book, not runnable code.
# The 2x2 covariance matrix written in maths notation: Var and Cov are the
# mathematical operators, not Python functions, and x and y are symbols in a
# formula rather than variables any earlier block defines.
# C = [[ Var(x),      Cov(x, y) ],
#      [ Cov(x, y),   Var(y)    ]]

# --- block 2 ---
import numpy as np
X = np.array([[-2, -2], [-1, -1], [0, 0], [1, 1], [2, 2]])  # centered, mean = (0, 0)

# --- block 3 ---
C = [[4, 2],
     [2, 4]]
