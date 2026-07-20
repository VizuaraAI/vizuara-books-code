"""
Machine Learning Fundamentals
Chapter 36: Hands-On: Training a Neural Network in Python
Section: Neural Networks

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/training-a-neural-network-in-python

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from sklearn.datasets import make_moons
X, y = make_moons(n_samples=200, noise=0.20, random_state=1)
# X is (200, 2) — two coordinates per point; y is 0/1

# --- block 2 ---
import numpy as np
rng = np.random.default_rng(1)

def sigmoid(z): return 1.0 / (1.0 + np.exp(-z))

# --- init: small random weights break symmetry ---
W1 = rng.normal(0, 0.5, size=(2, 8)); b1 = np.zeros(8)
W2 = rng.normal(0, 0.5, size=(8, 1)); b2 = np.zeros(1)

eta, epochs = 0.5, 4000
y = y.reshape(-1, 1)                     # (200, 1)
n = len(y)

for epoch in range(epochs):
    # --- forward ---
    h  = np.tanh(X @ W1 + b1)            # (200, 8)
    p  = sigmoid(h @ W2 + b2)            # (200, 1)
    p  = np.clip(p, 1e-12, 1 - 1e-12)    # keep log() finite

    # --- backward (chain rule) ---
    d2 = (p - y) / n                     # output error  (200, 1)
    gW2 = h.T @ d2;  gb2 = d2.sum(0)
    d1 = (d2 @ W2.T) * (1 - h**2)        # push error through tanh  (200, 8)
    gW1 = X.T @ d1;  gb1 = d1.sum(0)

    # --- step ---
    W1 -= eta * gW1;  b1 -= eta * gb1
    W2 -= eta * gW2;  b2 -= eta * gb2
