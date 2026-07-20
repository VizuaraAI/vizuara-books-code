"""
Foundations for AI & ML
Chapter 4: Matrix-Vector Multiplication as a Transformation
Section: Linear Algebra for ML

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/matrix-vector-multiplication-as-a-transformation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

A = np.array([[2, 0],
              [0, 3]])
x = np.array([3, 1])

print(A @ x)          # [6 3]  — the row-dot-product view
print(3*A[:, 0] + 1*A[:, 1])   # [6 3]  — the weighted-columns view
