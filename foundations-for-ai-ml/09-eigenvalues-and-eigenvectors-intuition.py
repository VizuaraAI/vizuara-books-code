"""
Foundations for AI & ML
Chapter 9: Eigenvalues and Eigenvectors, Intuitively
Section: Linear Algebra for ML

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/eigenvalues-and-eigenvectors-intuition

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

A = np.array([[2.0, 1.0],
              [0.0, 3.0]])

eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)          # [2. 3.]
print(eigenvectors[:, 0])   # eigenvector for λ=2, direction (1, 0)
print(eigenvectors[:, 1])   # eigenvector for λ=3, direction ~(0.707, 0.707)
