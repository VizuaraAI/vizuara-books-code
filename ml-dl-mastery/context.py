"""
Shared context for the Machine Learning & Deep Learning Mastery companion code.

Later chapters keep using classes, functions and the tiny worked example that
an EARLIER chapter introduced, without repeating the code. This module holds
those shared definitions so that each chapter file can say

    from context import Dense, layer1, layer2, X, y

and be checkable on its own.

Everything below is COPIED VERBATIM from the chapter named in the banner above
it. Nothing in this file is invented, rewritten, or "improved".

Read the book: https://books.vizuara.ai/read/ml-dl-mastery
"""

import numpy as np


# ---------------------------------------------------------------------------
# Chapter 32: Backpropagation Recap and Code - block 2
# https://books.vizuara.ai/read/ml-dl-mastery/backpropagation-recap-and-code
#
# The book's dense layer. Chapter 28 introduces it with .forward only;
# chapter 32 reprints it with .backward added. This is chapter 32's version,
# verbatim, because the chapters that import it call .backward.
# ---------------------------------------------------------------------------
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


# ---------------------------------------------------------------------------
# Chapter 33: The Entire Backward Pass in Code - block 2
# https://books.vizuara.ai/read/ml-dl-mastery/the-entire-backward-pass
# ---------------------------------------------------------------------------
class ReLU:
    def forward(self, inputs):
        self.inputs = inputs
        return np.maximum(0, inputs)

    def backward(self, dA):
        dZ = dA.copy()
        dZ[self.inputs <= 0] = 0    # gradient dies where the neuron was off
        return dZ


# ---------------------------------------------------------------------------
# Chapter 28: The Forward Pass in Code - blocks 2, 3, 4
# https://books.vizuara.ai/read/ml-dl-mastery/forward-pass-in-code
# ---------------------------------------------------------------------------
def relu(Z):
    return np.maximum(0, Z)


def softmax(Z):
    Z = Z - np.max(Z, axis=1, keepdims=True)   # numerical stability, changes nothing
    expZ = np.exp(Z)
    return expZ / np.sum(expZ, axis=1, keepdims=True)   # each row sums to 1


def cross_entropy(A2, y_true):
    n = len(y_true)
    p_correct = A2[range(n), y_true]        # pick each sample's true-class prob
    p_correct = np.clip(p_correct, 1e-12, 1.0)   # never log(0)
    return -np.mean(np.log(p_correct))


# ---------------------------------------------------------------------------
# Chapter 28: The Forward Pass in Code - block 5
# https://books.vizuara.ai/read/ml-dl-mastery/forward-pass-in-code
#
# The two-sample toy problem later chapters keep pointing back to ("the
# forward pass from the previous chapter"). Copied verbatim; only the trailing
# print() lines of the block are left out, since this is an importable module.
# ---------------------------------------------------------------------------
np.random.seed(0)
X = np.array([[1.0, 2.0, 3.0],
              [2.0, 1.0, 0.0]])      # (2, 3): two samples
y = np.array([0, 1])                 # true class per sample

layer1 = Dense(3, 4)                 # 3 -> 4
layer2 = Dense(4, 2)                 # 4 -> 2
