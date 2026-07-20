"""
Python for Data Science
Chapter 21: NumPy: Arrays and Vectorization
Section: The Data Science Toolkit

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/numpy-arrays-and-vectorization

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

a = np.array([3, 1, 4, 1, 5])
a.shape     # (5,)      — a tuple describing the size along each axis
a.dtype     # dtype('int64')  — every element is a 64-bit integer
a.ndim      # 1         — number of dimensions (axes)

# --- block 2 ---
# The Python way — an explicit loop, one interpreted step per element
result = []
for x in [3, 1, 4, 1, 5]:
    result.append(x + 10)
# result == [13, 11, 14, 11, 15]

# The NumPy way — one vectorized expression, no loop in sight
a = np.array([3, 1, 4, 1, 5])
a + 10
# array([13, 11, 14, 11, 15])

# --- block 3 ---
X = np.array([[2., 4.],
              [4., 8.],
              [6., 6.]])          # shape (3, 2): 3 rows, 2 columns

col_means = X.mean(axis=0)        # shape (2,): mean down each column
# col_means == array([4., 6.])    ( (2+4+6)/3=4 , (4+8+6)/3=6 )

centered = X - col_means          # (3,2) minus (2,) — broadcasting!
