"""
Mathematical Foundations for Machine Learning
Chapter 14: Eigenvalues and Eigenvectors
Section: Determinants and the Shape of Space

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/eigenvalues-and-eigenvectors

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
A = [[2, 1],
     [1, 2]]

# --- block 2 ---
import numpy as np

A = np.array([[2, 1],
              [1, 2]])

values, vectors = np.linalg.eig(A)
print(values)          # [1. 3.]  → the eigenvalues
print(vectors[:, 1])   # [0.707..., 0.707...]  → eigenvector for λ = 3, i.e. (1,1) normalized
