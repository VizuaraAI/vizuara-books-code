"""
Neural Networks from Scratch - shared context

Later chapters reuse names that an EARLIER chapter of this same book already
defined (Layer_Dense, Activation_ReLU, the spiral dataset, ...). The generated
per-chapter files only contain that chapter's own code blocks, so those names
would be undefined when a file is run on its own.

This module collects those earlier definitions in one place so the later
chapter files can do `from context import ...` and actually run.

Every definition below is COPIED VERBATIM from the extracted code of the
chapter named above it. Nothing here is invented. The only editorial acts are
(a) putting them in one file, and (b) indenting Layer_Dense.backward, which
chapter 24 presents as a bare `def` that the reader is told to add to the
Layer_Dense class.

Book: https://books.vizuara.ai/read/neural-networks-from-scratch
"""

import numpy as np


# ---------------------------------------------------------------------------
# Chapter 21: The Problem: A Spiral Dataset
# https://books.vizuara.ai/read/neural-networks-from-scratch/problem-description
# ---------------------------------------------------------------------------

def spiral_data(samples, classes):
    X = np.zeros((samples * classes, 2))          # (300, 2) for 100×3
    y = np.zeros(samples * classes, dtype='uint8') # (300,)  integer labels
    for class_number in range(classes):
        ix = range(samples * class_number, samples * (class_number + 1))
        r = np.linspace(0.0, 1, samples)                              # radius 0 → 1
        t = (np.linspace(class_number * 4, (class_number + 1) * 4, samples)
             + np.random.randn(samples) * 0.2)                        # angle + noise
        X[ix] = np.c_[r * np.sin(t * 2.5), r * np.cos(t * 2.5)]       # (x, y)
        y[ix] = class_number
    return X, y


X, y = spiral_data(samples=100, classes=3)


# ---------------------------------------------------------------------------
# Chapter 23: Coding the Layer Forward Pass  (the class and its forward)
# https://books.vizuara.ai/read/neural-networks-from-scratch/layer-forward-pass
#
# Chapter 24: Coding the Layer Backward Pass (the backward method, block 7)
# https://books.vizuara.ai/read/neural-networks-from-scratch/layers-backward-pass
# ---------------------------------------------------------------------------

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases  = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.inputs = inputs                          # remember for the backward pass
        self.output = inputs @ self.weights + self.biases

    # chapter 24, block 7 - shown there as a bare `def` to add to this class
    def backward(self, dvalues):
        # gradients on parameters
        self.dweights = np.dot(self.inputs.T, dvalues)          # (n_inputs, n_neurons)
        self.dbiases  = np.sum(dvalues, axis=0, keepdims=True)  # (1, n_neurons)
        # gradient to pass to the previous layer
        self.dinputs  = np.dot(dvalues, self.weights.T)         # (n_samples, n_inputs)


# ---------------------------------------------------------------------------
# Chapter 26: ReLU: Forward and Backward Pass  (block 3, the finished class)
# https://books.vizuara.ai/read/neural-networks-from-scratch/relu-forward-backward-pass
# ---------------------------------------------------------------------------

class Activation_ReLU:
    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.maximum(0, inputs)

    def backward(self, dvalues):
        self.dinputs = dvalues.copy()
        self.dinputs[self.inputs <= 0] = 0


# ---------------------------------------------------------------------------
# Chapter 27: Softmax: The Forward Pass in Code  (block 1)
# https://books.vizuara.ai/read/neural-networks-from-scratch/softmax-forward-pass
# ---------------------------------------------------------------------------

class Activation_Softmax:
    def forward(self, inputs):
        self.inputs = inputs                                    # cache for the backward pass
        # subtract the per-row max BEFORE exponentiating (numerical stability)
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        # normalize each row to sum to 1
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities                             # cache the result


# ---------------------------------------------------------------------------
# Chapter 29: The Combined Softmax + Loss Backward Pass
# https://books.vizuara.ai/read/neural-networks-from-scratch/combined-softmax-loss-backward-pass
# ---------------------------------------------------------------------------

class SoftmaxCrossEntropy:
    def backward(self, softmax_output, y_true):
        n_samples = len(softmax_output)          # rows = samples in the batch
        dinputs = softmax_output.copy()          # start from p
        dinputs[range(n_samples), y_true] -= 1   # subtract 1 at each true class → p - y
        dinputs = dinputs / n_samples            # average over the batch
        return dinputs


# ---------------------------------------------------------------------------
# Chapter 31: Coding the Optimizer  (block 1)
# https://books.vizuara.ai/read/neural-networks-from-scratch/optimizers-in-code
# ---------------------------------------------------------------------------

class Optimizer_SGD:
    def __init__(self, learning_rate=1.0):
        self.learning_rate = learning_rate

    def update_params(self, layer):
        layer.weights += -self.learning_rate * layer.dweights
        layer.biases  += -self.learning_rate * layer.dbiases


# ---------------------------------------------------------------------------
# Chapter 27: Softmax: The Forward Pass in Code  (block 2, the network objects)
# https://books.vizuara.ai/read/neural-networks-from-scratch/softmax-forward-pass
#
# NOTE: these are freshly initialised (untrained). Chapter 32 is what trains
# them; a file that imports them here gets the same objects the book builds,
# but with random starting weights.
# ---------------------------------------------------------------------------

dense1      = Layer_Dense(2, 8)          # 2 inputs -> 8 hidden neurons
activation1 = Activation_ReLU()
dense2      = Layer_Dense(8, 3)          # 8 hidden -> 3 class scores
activation2 = Activation_Softmax()
