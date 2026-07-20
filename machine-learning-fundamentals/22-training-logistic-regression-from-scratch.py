"""
Machine Learning Fundamentals
Chapter 22: Training Logistic Regression from Scratch
Section: Logistic Regression and Optimization

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/training-logistic-regression-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def train(X, y, eta=0.5, epochs=2000):
    n, d = X.shape
    w = np.zeros(d)          # cold start
    b = 0.0
    for epoch in range(epochs):
        p    = sigmoid(X @ w + b)          # 1. forward: all predictions
        grad_w = (X.T @ (p - y)) / n       # 3. gradient: (pred - target)·input
        grad_b = (p - y).mean()            #    bias gradient
        w -= eta * grad_w                  # 4. step downhill
        b -= eta * grad_b
    return w, b
