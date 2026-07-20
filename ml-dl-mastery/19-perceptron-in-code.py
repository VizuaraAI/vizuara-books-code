"""
Machine Learning & Deep Learning Mastery
Chapter 19: The Perceptron in Code
Section: Linear Classifiers & the Perceptron

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/perceptron-in-code

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

rng = np.random.default_rng(5)
n = 50
# class +1: blob around (1.5, 1.5);  class -1: blob around (-1.5, -1.5)
X_pos = rng.normal(loc=[ 1.5,  1.5], scale=1.0, size=(n, 2))
X_neg = rng.normal(loc=[-1.5, -1.5], scale=1.0, size=(n, 2))

X = np.vstack([X_pos, X_neg])                     # shape (100, 2)
y = np.hstack([np.ones(n), -np.ones(n)])          # shape (100,), values in {+1, -1}

# --- block 2 ---
def perceptron(X, y, eta=1.0, epochs=20):
    n_features = X.shape[1]
    w = np.zeros(n_features)     # w = [0., 0.]
    b = 0.0
    for epoch in range(epochs):
        mistakes = 0
        for xi, yi in zip(X, y):
            score = np.dot(w, xi) + b
            pred  = 1.0 if score > 0 else -1.0
            if pred != yi:                    # only learn on mistakes
                w += eta * yi * xi
                b += eta * yi
                mistakes += 1
        print(f"epoch {epoch:2d}: {mistakes} mistakes,  w={np.round(w,2)}, b={round(b,2)}")
        if mistakes == 0:                     # perfectly separated → stop
            break
    return w, b
