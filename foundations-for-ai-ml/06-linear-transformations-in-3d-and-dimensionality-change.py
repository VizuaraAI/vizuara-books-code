"""
Foundations for AI & ML
Chapter 6: Linear Transformations in 3D and Dimensionality Change
Section: Linear Algebra for ML

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/linear-transformations-in-3d-and-dimensionality-change

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

A = np.array([[2.0, 0.0, 0.0],
              [0.0, 1.0, 0.0],
              [0.0, 0.0, 0.5]])
v = np.array([3.0, 4.0, 10.0])
A @ v          # -> array([6., 4., 5.])

# --- block 2 ---
B = np.array([[1.0, 0.0, 1.0],
              [0.0, 1.0, 1.0],
              [1.0, 1.0, 2.0]])
