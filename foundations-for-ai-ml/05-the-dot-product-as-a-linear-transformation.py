"""
Foundations for AI & ML
Chapter 5: The Dot Product as a Linear Transformation
Section: Linear Algebra for ML

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/the-dot-product-as-a-linear-transformation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

w = np.array([2.0, 0.5, 1.5])
x = np.array([1.0, 4.0, 0.0])

z = np.dot(w, x)     # or w @ x
print(z)             # 4.0
