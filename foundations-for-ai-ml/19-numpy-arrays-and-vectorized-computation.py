"""
Foundations for AI & ML
Chapter 19: NumPy: Arrays and Vectorized Computation
Section: Python & the ML Toolkit

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/numpy-arrays-and-vectorized-computation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
sizes = [1200, 850, 2000, 1500]
meters = []
for s in sizes:
    meters.append(s / 10.76)

# --- block 2 ---
import numpy as np
sizes = np.array([1200, 850, 2000, 1500])   # shape (4,), dtype int64
meters = sizes / 10.76                        # shape (4,), dtype float64

# --- block 3 ---
X = np.array([[10, 20, 30, 40],
              [11, 21, 31, 41],
              [12, 22, 32, 42]])     # shape (3, 4)
mean = X.mean(axis=0)                # shape (4,)  -> [11., 21., 31., 41.]
centered = X - mean                  # shape (3, 4), each row mean-subtracted
# row 0 becomes [-1, -1, -1, -1]; row 1 -> [0,0,0,0]; row 2 -> [1,1,1,1]

# --- block 4 ---
X = np.random.randn(2, 3)     # 2 samples, 3 features each
W = np.random.randn(3, 4)     # 3 -> 4 linear map
b = np.random.randn(4)        # one bias per output unit
Z = X @ W + b                 # (2,3)@(3,4) = (2,4), then + (4,) broadcasts to every row
