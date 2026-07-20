"""
Mathematical Foundations for Machine Learning
Chapter 29: Linear Algebra in NumPy
Section: Python and Numerical Computing

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/linear-algebra-in-numpy

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.dot(a, b)   # 32
a @ b          # 32  — the @ operator, since Python 3.5
a.dot(b)       # 32

# --- block 2 ---
A = np.array([[2, -1],
              [1,  1]])
v = np.array([3, 2])

A @ v          # array([4, 5])

# --- block 3 ---
A = np.array([[0, -1],
              [1,  0]])
B = np.array([[1, 0],
              [0, -1]])

A @ B          # array([[0, 1], [1, 0]])
B @ A          # array([[0, -1], [-1, 0]])

# --- block 4 ---
M = np.array([[2, 1],
              [1, 2]])

np.linalg.det(M)   # 2.9999999999999996

# --- block 5 ---
S = np.array([[1, 2],
              [2, 4]])          # row 2 = 2 × row 1 → dependent columns

np.linalg.det(S)               # ~ 0.0  (a tiny number like -8.9e-17)
np.linalg.inv(S)               # LinAlgError: Singular matrix

# --- block 6 ---
A = np.array([[2, 1],
              [1, 3]])
b = np.array([5, 10])

np.linalg.solve(A, b)        # array([1., 3.])
np.linalg.inv(A) @ b         # array([1., 3.])  — same answer, worse road

# --- block 7 ---
A = np.array([[2, 1],
              [1, 2]])

values, vectors = np.linalg.eig(A)
print(values)          # [3. 1.]   ← note the order: NOT sorted small-to-large
print(vectors)         # [[ 0.707... -0.707...]
                       #  [ 0.707...  0.707...]]

# --- block 8 ---
lam = values[0]              # 3.0
v   = vectors[:, 0]          # eigenvector for λ = 3
np.allclose(A @ v, lam * v)  # True
