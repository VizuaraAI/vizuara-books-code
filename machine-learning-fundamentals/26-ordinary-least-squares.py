"""
Machine Learning Fundamentals
Chapter 26: Ordinary Least Squares: The Closed-Form Solution
Section: Linear Regression

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/ordinary-least-squares

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

X = np.array([[1, 1], [1, 2], [1, 3], [1, 4]])  # bias column + feature
y = np.array([2, 2, 4, 5])

w = np.linalg.solve(X.T @ X, X.T @ y)   # solve, don't invert
print(w)   # [0.5 1.1]
