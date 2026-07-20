"""
Mathematical Foundations for Machine Learning
Chapter 13: Zero Determinant and Collapse
Section: Determinants and the Shape of Space

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/zero-determinant-and-collapse

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

A = np.array([[2, 1],
              [4, 2]])

print(np.linalg.det(A))      # -> 0.0  (up to floating-point dust)
print(np.linalg.matrix_rank(A))   # -> 1  (columns span only a 1D line)
np.linalg.inv(A)             # -> LinAlgError: Singular matrix
