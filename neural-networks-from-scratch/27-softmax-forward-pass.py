"""
Neural Networks from Scratch
Chapter 27: Softmax: The Forward Pass in Code
Section: Coding the Layers

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/softmax-forward-pass

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- context (added so this file runs standalone) ---
# Layer_Dense (chapters 22-24), Activation_ReLU (chapter 26) and the spiral
# dataset X (chapter 21) all come from earlier chapters of this same book.
# context.py holds those definitions verbatim.
from context import Layer_Dense, Activation_ReLU, X

# --- block 1 ---
import numpy as np

class Activation_Softmax:
    def forward(self, inputs):
        self.inputs = inputs                                    # cache for the backward pass
        # subtract the per-row max BEFORE exponentiating (numerical stability)
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        # normalize each row to sum to 1
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities                             # cache the result

# --- block 2 ---
# X is the spiral data, shape (300, 2)
dense1      = Layer_Dense(2, 8)          # 2 inputs -> 8 hidden neurons
activation1 = Activation_ReLU()
dense2      = Layer_Dense(8, 3)          # 8 hidden -> 3 class scores
activation2 = Activation_Softmax()

dense1.forward(X)
activation1.forward(dense1.output)
dense2.forward(activation1.output)
activation2.forward(dense2.output)       # <- softmax turns logits into probabilities

print(activation2.output[:3])

# --- block 3 ---
row_sums = np.sum(activation2.output, axis=1)
print(row_sums[:5])
# [1. 1. 1. 1. 1.]
print(np.allclose(row_sums, 1.0))
# True

# --- block 4 ---
test = Activation_Softmax()
test.forward(np.array([[2.3, -1.7, 0.5]]))
print(test.output)          # [[0.845  0.015  0.140]]
print(test.output.sum())    # 1.0
