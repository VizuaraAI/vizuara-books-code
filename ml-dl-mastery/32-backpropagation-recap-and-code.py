"""
Machine Learning & Deep Learning Mastery
Chapter 32: Backpropagation Recap and Code
Section: Neural Networks: Backpropagation

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/backpropagation-recap-and-code

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import numpy as np

# Block 4 below reuses the forward pass "from the previous chapter": the toy
# dataset and the two layers built in chapter 28.
from context import X, y, layer1, layer2

# AUTHORING BUG: block 4 calls relu_forward(), which the book never defines.
# Chapter 28 defines the same function under the name `relu`, and this chapter
# defines its partner as `relu_backward`. Stubbed rather than guessed at.
# See https://books.vizuara.ai/read/ml-dl-mastery/forward-pass-in-code
relu_forward = None  # TODO: the book never defines this name

# --- block 1 ---
def softmax_forward(Z):
    Z = Z - np.max(Z, axis=1, keepdims=True)      # numerical stability
    expZ = np.exp(Z)
    return expZ / np.sum(expZ, axis=1, keepdims=True)

def softmax_ce_backward(A2, y_true):
    n = len(y_true)
    dZ2 = A2.copy()
    dZ2[range(n), y_true] -= 1        # subtract 1 from the true-class column of each row
    return dZ2 / n                    # average over the batch

# --- block 2 ---
class Dense:
    def __init__(self, n_in, n_out):
        self.W = 0.10 * np.random.randn(n_in, n_out)
        self.b = np.zeros((1, n_out))

    def forward(self, X):
        self.X = X                       # cache for the backward pass
        return X @ self.W + self.b

    def backward(self, dvalues):
        self.dW = self.X.T @ dvalues     # (n_in, batch) @ (batch, n_out) -> (n_in, n_out)
        self.db = np.sum(dvalues, axis=0, keepdims=True)
        return dvalues @ self.W.T        # (batch, n_out) @ (n_out, n_in) -> (batch, n_in)

# --- block 3 ---
def relu_backward(dvalues, Z):
    dZ = dvalues.copy()
    dZ[Z <= 0] = 0        # kill the gradient where the neuron was inactive
    return dZ

# --- block 4 ---
# --- forward (from the previous chapter) ---
Z1 = layer1.forward(X)          # (2, 4)
A1 = relu_forward(Z1)           # (2, 4)
Z2 = layer2.forward(A1)         # (2, 2)
A2 = softmax_forward(Z2)        # (2, 2) probabilities
# loss = cross_entropy(A2, y)

# --- backward: reverse the exact same chain ---
dZ2 = softmax_ce_backward(A2, y)     # (2, 2)  -> A2 - Y, averaged
dA1 = layer2.backward(dZ2)           # fills layer2.dW, layer2.db; returns (2, 4)
dZ1 = relu_backward(dA1, Z1)         # gate: zero where Z1 <= 0
_   = layer1.backward(dZ1)           # fills layer1.dW, layer1.db
