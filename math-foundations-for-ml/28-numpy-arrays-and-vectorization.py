"""
Mathematical Foundations for Machine Learning
Chapter 28: NumPy Arrays and Vectorization
Section: Python and Numerical Computing

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/numpy-arrays-and-vectorization

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

X = np.array([[150, 50, 20],
              [160, 60, 25],
              [170, 70, 30],
              [180, 80, 35]])

X.shape    # (4, 3)  -> 4 rows (samples), 3 columns (features)
X.dtype    # dtype('int64')
X.ndim     # 2  -> a 2-D array

# --- block 2 ---
mu = X.mean(axis=0)    # mean DOWN the rows -> one value per feature
mu                      # array([165., 65., 27.5])

# --- block 3 ---
X_centered = X - mu
X_centered
# array([[-15., -15.,  -7.5],
#        [ -5.,  -5.,  -2.5],
#        [  5.,   5.,   2.5],
#        [ 15.,  15.,   7.5]])

# --- block 4 ---
a = np.random.rand(1_000_000)
b = np.random.rand(1_000_000)

# the slow way: an explicit Python loop
out = np.empty_like(a)
for i in range(len(a)):
    out[i] = a[i] + b[i]

# the fast way: one vectorized operation
out = a + b

# --- block 5 ---
w = np.array([0.2, 0.5, -0.1])
x = np.array([1.0, 2.0, 3.0])

np.dot(w, x)    # 0.2*1 + 0.5*2 + (-0.1)*3 = 0.2 + 1.0 - 0.3 = 0.9
