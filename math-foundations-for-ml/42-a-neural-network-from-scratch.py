"""
Mathematical Foundations for Machine Learning
Chapter 42: A Neural Network from Scratch
Section: Putting It Together

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/a-neural-network-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# NOTE: this block is prose in the book, not runnable code.
# The forward pass for a single example, written as annotated equations to
# introduce the shapes. The weights, the input x and sigmoid() are symbols
# here; block 2 below is the runnable, batched version that actually defines
# sigmoid, W1, b1, W2 and b2.
# z1 = W1 @ x  + b1     # (2×2)(2,) + (2,) -> (2,)   hidden pre-activation
# a1 = sigmoid(z1)      # (2,)                        hidden activation
# z2 = W2 @ a1 + b2     # (1×2)(2,) + (1,) -> (1,)   output pre-activation
# a2 = sigmoid(z2)      # (1,)                        prediction, in (0,1)

# --- block 2 ---
import numpy as np

def sigmoid(z):  return 1 / (1 + np.exp(-z))

X = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=float)   # (4,2)
y = np.array([[0],[1],[1],[0]], dtype=float)           # (4,1)

rng = np.random.default_rng(0)
W1 = rng.normal(0, 1, (2,2)); b1 = np.zeros((1,2))     # layer 1
W2 = rng.normal(0, 1, (2,1)); b2 = np.zeros((1,1))     # layer 2
eta = 0.5

for step in range(10000):
    # ---- forward ----
    Z1 = X @ W1 + b1;  A1 = sigmoid(Z1)                 # (4,2)
    Z2 = A1 @ W2 + b2; A2 = sigmoid(Z2)                 # (4,1)
    loss = np.mean((A2 - y) ** 2)

    # ---- backward (chain rule) ----
    dZ2 = 2*(A2 - y) * A2*(1 - A2)                      # (4,1) output error δ2
    dW2 = A1.T @ dZ2;            db2 = dZ2.sum(0, keepdims=True)
    dZ1 = (dZ2 @ W2.T) * A1*(1 - A1)                    # (4,2) hidden error δ1
    dW1 = X.T  @ dZ1;           db1 = dZ1.sum(0, keepdims=True)

    # ---- gradient-descent step ----
    W1 -= eta*dW1; b1 -= eta*db1
    W2 -= eta*dW2; b2 -= eta*db2
