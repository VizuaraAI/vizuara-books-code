"""
Deep Learning Fundamentals - shared context for the companion code.

This module is NOT part of the book. It exists only so that a chapter file
which relies on something the book built in an EARLIER chapter can be run on
its own.

Every definition below is COPIED VERBATIM from the book's own code blocks.
The source chapter is named above each one. Nothing here is invented.

Book: https://books.vizuara.ai/read/deep-learning-fundamentals
"""

import numpy as np

# Chapter 24, block 1.
np.random.seed(0)


# ---------------------------------------------------------------------------
# The building blocks.
#
# Copied verbatim from chapter 24, "The entire forward-backward pass in
# Python", block 1 - the book's own consolidation, under the heading
# "the building blocks (built in earlier chapters)", of the classes it
# developed in chapter 7 (Dense.__init__ / Dense.forward), chapter 16
# (Dense.backward), chapter 20 (ReLU) and chapter 22 (the fused
# softmax + cross-entropy backward).
#
# https://books.vizuara.ai/read/deep-learning-fundamentals/forward-backward-pass-in-python
# ---------------------------------------------------------------------------
class Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases  = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.inputs  = inputs                          # remember for backward
        self.output  = inputs @ self.weights + self.biases

    def backward(self, dvalues):
        self.dweights = self.inputs.T @ dvalues        # (n_inputs, n_neurons)
        self.dbiases  = np.sum(dvalues, axis=0, keepdims=True)
        self.dinputs  = dvalues @ self.weights.T       # baton to the previous layer


class ReLU:
    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.maximum(0, inputs)

    def backward(self, dvalues):
        self.dinputs = dvalues.copy()
        self.dinputs[self.inputs <= 0] = 0             # zero the dead neurons


class SoftmaxCrossEntropy:
    def forward(self, logits, y_true):
        exp = np.exp(logits - logits.max(axis=1, keepdims=True))   # stable softmax
        self.output = exp / exp.sum(axis=1, keepdims=True)         # y-hat, rows sum to 1
        clipped = np.clip(self.output, 1e-7, 1 - 1e-7)             # avoid log(0)
        correct = np.sum(clipped * y_true, axis=1)                 # y-hat of the true class
        return np.mean(-np.log(correct))                           # scalar loss

    def backward(self, y_true):
        batch = len(y_true)
        self.dinputs = (self.output - y_true) / batch              # the y-hat - y shortcut


# ---------------------------------------------------------------------------
# The network and the tiny batch.
#
# Copied verbatim from chapter 24, block 2. Chapters 23, 25 and 31 all drive
# this exact network (dense1 -> relu -> dense2 -> fused softmax/cross-entropy)
# without re-constructing it in a code block of their own.
# ---------------------------------------------------------------------------
# ---- the network: a 4 -> 5 -> 3 classifier ----
dense1 = Dense(4, 5)
relu   = ReLU()
dense2 = Dense(5, 3)
loss_fn = SoftmaxCrossEntropy()

layers = [dense1, relu, dense2]        # forward order

# ---- a tiny batch: 2 samples, 4 features, 3 classes ----
X = np.array([[1.0, 2.0, 3.0, 2.5],
              [2.0, 5.0, -1.0, 2.0]])
y = np.array([[1.0, 0.0, 0.0],         # sample 0 is class 0
              [0.0, 0.0, 1.0]])        # sample 1 is class 2

# Chapter 24 names the fused softmax + cross-entropy object `loss_fn`;
# chapters 23, 25 and 31 refer to the same object as `loss_activation`.
# Same object, two names in the book - exported under both so either
# chapter's code resolves.
loss_activation = loss_fn


# ---------------------------------------------------------------------------
# The optimizer.
# Copied verbatim from chapter 25, "Coding the gradient descent optimizer",
# block 1 (the class) and block 2 (the instance). Chapter 31 uses `optimizer`
# without constructing it.
# https://books.vizuara.ai/read/deep-learning-fundamentals/gradient-descent-optimizer
# ---------------------------------------------------------------------------
class Optimizer_SGD:
    def __init__(self, learning_rate=1.0):
        self.learning_rate = learning_rate

    def update_params(self, layer):
        layer.weights += -self.learning_rate * layer.dweights
        layer.biases  += -self.learning_rate * layer.dbiases


optimizer = Optimizer_SGD(learning_rate=1.0)
