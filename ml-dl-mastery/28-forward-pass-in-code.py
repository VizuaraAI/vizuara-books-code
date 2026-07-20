"""
Machine Learning & Deep Learning Mastery
Chapter 28: The Forward Pass in Code
Section: Neural Networks: The Forward Pass

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/forward-pass-in-code

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

class Dense:
    def __init__(self, n_in, n_out):
        # small random weights, zero biases — the standard init
        self.W = 0.10 * np.random.randn(n_in, n_out)
        self.b = np.zeros((1, n_out))

    def forward(self, X):
        self.X = X                      # cached — the backward pass needs it
        self.Z = X @ self.W + self.b    # (batch, n_in) @ (n_in, n_out) -> (batch, n_out)
        return self.Z

# --- block 2 ---
def relu(Z):
    return np.maximum(0, Z)

# --- block 3 ---
def softmax(Z):
    Z = Z - np.max(Z, axis=1, keepdims=True)   # numerical stability, changes nothing
    expZ = np.exp(Z)
    return expZ / np.sum(expZ, axis=1, keepdims=True)   # each row sums to 1

# --- block 4 ---
def cross_entropy(A2, y_true):
    n = len(y_true)
    p_correct = A2[range(n), y_true]        # pick each sample's true-class prob
    p_correct = np.clip(p_correct, 1e-12, 1.0)   # never log(0)
    return -np.mean(np.log(p_correct))

# --- block 5 ---
np.random.seed(0)
X = np.array([[1.0, 2.0, 3.0],
              [2.0, 1.0, 0.0]])      # (2, 3): two samples
y = np.array([0, 1])                 # true class per sample

layer1 = Dense(3, 4)                 # 3 -> 4
layer2 = Dense(4, 2)                 # 4 -> 2

Z1 = layer1.forward(X)               # (2, 4)
A1 = relu(Z1)                        # (2, 4)
Z2 = layer2.forward(A1)              # (2, 2)
A2 = softmax(Z2)                     # (2, 2) — probabilities
loss = cross_entropy(A2, y)          # a single float

print(A2)                            # each row sums to 1
print(loss)                          # e.g. ~0.69 with random init
