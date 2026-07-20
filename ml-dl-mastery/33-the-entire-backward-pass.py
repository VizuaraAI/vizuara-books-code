"""
Machine Learning & Deep Learning Mastery
Chapter 33: The Entire Backward Pass in Code
Section: Neural Networks: Backpropagation

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/the-entire-backward-pass

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import numpy as np

# softmax() and cross_entropy() are chapter 28's, reused here without being
# reprinted.
from context import softmax, cross_entropy

# Blocks 3 and 4 walk through the chain BEFORE block 5 actually builds the
# objects, so these names are stubbed here. Block 5 below assigns all of them
# for real - it is the runnable script for this chapter.
X = None       # TODO: block 5 below builds this
y = None       # TODO: block 5 below builds this
layer1 = None  # TODO: block 5 below builds this (Layer_Dense(2, 8))
layer2 = None  # TODO: block 5 below builds this (Layer_Dense(8, 2))
relu = None    # TODO: block 5 below builds this (ReLU())

# --- block 1 ---
class Layer_Dense:
    def __init__(self, n_in, n_out):
        self.weights = 0.10 * np.random.randn(n_in, n_out)
        self.biases  = np.zeros((1, n_out))

    def forward(self, inputs):
        self.inputs = inputs                       # cached for backward
        self.output = inputs @ self.weights + self.biases
        return self.output

    def backward(self, dZ):
        self.dW = self.inputs.T @ dZ               # gradient wrt weights
        self.db = np.sum(dZ, axis=0, keepdims=True)# gradient wrt biases
        return dZ @ self.weights.T                 # gradient to pass back (dX)

# --- block 2 ---
class ReLU:
    def forward(self, inputs):
        self.inputs = inputs
        return np.maximum(0, inputs)

    def backward(self, dA):
        dZ = dA.copy()
        dZ[self.inputs <= 0] = 0    # gradient dies where the neuron was off
        return dZ

# --- block 3 ---
# --- forward ---
Z1 = layer1.forward(X)
A1 = relu.forward(Z1)
Z2 = layer2.forward(A1)
A2 = softmax(Z2)
loss = cross_entropy(A2, y)

# --- backward ---
y_onehot = np.eye(2)[y]                 # labels -> one-hot rows
dZ2 = (A2 - y_onehot) / len(y)          # the fused softmax+CE gradient
dA1 = layer2.backward(dZ2)              # fills layer2.dW, layer2.db
dZ1 = relu.backward(dA1)               # gate through ReLU
_   = layer1.backward(dZ1)              # fills layer1.dW, layer1.db

# --- block 4 ---
lr = 1.0
for layer in (layer1, layer2):
    layer.weights -= lr * layer.dW
    layer.biases  -= lr * layer.db

# --- block 5 ---
np.random.seed(0)
# a tiny two-class problem: class 0 clustered low, class 1 clustered high
X = np.vstack([np.random.randn(50, 2) - 1.5,
               np.random.randn(50, 2) + 1.5])
y = np.array([0]*50 + [1]*50)

layer1 = Layer_Dense(2, 8)
relu   = ReLU()
layer2 = Layer_Dense(8, 2)

for step in range(500):
    # forward
    A1   = relu.forward(layer1.forward(X))
    A2   = softmax(layer2.forward(A1))
    loss = cross_entropy(A2, y)
    # backward
    dZ2  = (A2 - np.eye(2)[y]) / len(y)
    dZ1  = relu.backward(layer2.backward(dZ2))
    layer1.backward(dZ1)
    # update
    for layer in (layer1, layer2):
        layer.weights -= 1.0 * layer.dW
        layer.biases  -= 1.0 * layer.db

    if step % 100 == 0:
        acc = (A2.argmax(axis=1) == y).mean()
        print(f"step {step:3d}  loss {loss:.3f}  acc {acc:.2f}")
