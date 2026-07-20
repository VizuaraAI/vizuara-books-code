"""
Mathematical Foundations for Machine Learning
Chapter 5: The Dot Product, Two Ways
Section: Linear Algebra as Transformations

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/the-dot-product-two-ways

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

a = np.array([3, 4])
b = np.array([2, 1])
print(a @ b)     # 10  — the @ operator is the dot product
print(np.dot(a, b))  # 10  — same thing, spelled out
