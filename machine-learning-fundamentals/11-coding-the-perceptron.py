"""
Machine Learning Fundamentals
Chapter 11: Coding the Perceptron from Scratch
Section: Linear Classifiers and the Perceptron

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/coding-the-perceptron

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def predict_one(w, b, x):
    z = w @ x + b                 # scalar score wᵀx + b
    return 1 if z >= 0 else -1     # sign, tie -> +1

# --- block 2 ---
X = np.array([[2, 3], [3, 2], [1, 1], [-1, -2], [-2, -1], [-1, 1]], dtype=float)
y = np.array([1, 1, 1, -1, -1, -1], dtype=float)

# --- block 3 ---
def train_perceptron(X, y, eta=1.0, max_epochs=100):
    n, d = X.shape
    w = np.zeros(d)          # start from a dead-flat line
    b = 0.0
    history = [(w.copy(), b)]  # snapshot for plotting later

    for epoch in range(max_epochs):
        mistakes = 0
        for xi, yi in zip(X, y):
            if predict_one(w, b, xi) != yi:   # only mistakes update
                w = w + eta * yi * xi
                b = b + eta * yi
                mistakes += 1
                history.append((w.copy(), b))
        print(f"epoch {epoch:2d}: {mistakes} mistakes")
        if mistakes == 0:        # a clean pass -> we are done
            break
    return w, b, history

# --- block 4 ---
def boundary_line(w, b, x1_range):
    # w1*x1 + w2*x2 + b = 0  ->  x2 = -(w1*x1 + b) / w2
    x1 = np.array(x1_range)
    x2 = -(w[0] * x1 + b) / w[1]
    return x1, x2
