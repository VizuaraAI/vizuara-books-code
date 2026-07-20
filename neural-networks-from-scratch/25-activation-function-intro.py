"""
Neural Networks from Scratch
Chapter 25: Adding Activation Functions
Section: Coding the Layers

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/activation-function-intro

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- context (added so this file runs standalone) ---
# Layer_Dense is built in chapters 22-24 of this same book. context.py holds
# that definition verbatim.
from context import Layer_Dense

# --- block 1 (COMMENTED OUT) ---
# NOTE: this block is a fragment of a method body in the book, not runnable
# code. It uses `self` and `inputs` at module level, where both are undefined.
# The book shows it only as the shortcut it then argues against.
# # the tempting shortcut (don't do this)
# self.output = np.maximum(0, inputs @ self.weights + self.biases)

# --- block 2 ---
class Activation_ReLU:
    def forward(self, inputs):
        self.inputs = inputs                 # remember the input — the backward pass needs it
        self.output = np.maximum(0, inputs)  # element-wise, shape unchanged

    def backward(self, dvalues):
        self.dinputs = dvalues.copy()        # start from the incoming gradient
        self.dinputs[self.inputs <= 0] = 0   # kill the gradient where the input was off

# --- block 3 ---
import numpy as np
np.random.seed(0)

X = np.random.randn(5, 2)          # 5 spiral points, 2 features each

dense1 = Layer_Dense(2, 8)         # 2 -> 8
relu   = Activation_ReLU()         # the drop-in nonlinearity
dense2 = Layer_Dense(8, 3)         # 8 -> 3

# forward pass: feed each layer's output into the next
dense1.forward(X)                  # (5,2)@(2,8) -> dense1.output is (5, 8)
relu.forward(dense1.output)        # element-wise -> relu.output is (5, 8)
dense2.forward(relu.output)        # (5,8)@(8,3) -> dense2.output is (5, 3)

print(dense1.output.shape, relu.output.shape, dense2.output.shape)
# (5, 8) (5, 8) (5, 3)
