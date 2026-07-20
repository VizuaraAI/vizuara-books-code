"""
Deep Learning Fundamentals
Chapter 19: Coding the backpropagation building blocks
Section: The Backward Pass (Backpropagation)

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/backprop-building-blocks

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- shared context (not book text) ---
# Block 4 instantiates `Dense`, the class the book builds in chapter 7
# (__init__/forward) and chapter 16 (backward). context.py holds it, copied
# verbatim from the book.
from context import Dense

# --- block 1 ---
def forward(self, inputs):
    self.output = inputs @ self.weights + self.biases   # inputs used, then thrown away

# --- block 2 ---
def forward(self, inputs):
    self.inputs = inputs                                # remember X for the backward pass
    self.output = inputs @ self.weights + self.biases

# --- block 3 ---
def backward(self, dvalues):
    # gradients on the layer's own parameters
    self.dweights = self.inputs.T @ dvalues                       # (n_inputs, n_neurons)
    self.dbiases  = np.sum(dvalues, axis=0, keepdims=True)        # (1, n_neurons)
    # gradient to hand back to the previous layer
    self.dinputs  = dvalues @ self.weights.T                      # (batch, n_inputs)

# --- block 4 ---
import numpy as np

X = np.array([[1.0, 2.0, 3.0],      # sample 1, 3 features
              [4.0, 5.0, 6.0]])     # sample 2         shape (2, 3)

layer = Dense(3, 2)                 # 3 inputs -> 2 neurons
layer.forward(X)                    # fills layer.inputs (2,3) and layer.output (2,2)

dvalues = np.array([[0.1, 0.2],     # a made-up upstream gradient
                    [0.3, 0.4]])    #                   shape (2, 2)
layer.backward(dvalues)             # fills the three gradient attributes
