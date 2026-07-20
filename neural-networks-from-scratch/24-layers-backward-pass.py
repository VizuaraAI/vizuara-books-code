"""
Neural Networks from Scratch
Chapter 24: Coding the Layer Backward Pass
Section: Coding the Layers

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/layers-backward-pass

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import numpy as np

# --- block 1 ---
X = [[ 1.0, 2.0, 3.0],      # (2, 3) — 2 samples, 3 features
     [-1.0, 0.5, 2.0]]

W = [[ 0.2, -0.5],          # (3, 2) — weights: n_inputs × n_neurons
     [ 0.1,  0.4],
     [-0.3,  0.6]]
b = [[ 0.0,  0.1]]          # (1, 2) — one bias per neuron

# --- block 2 ---
dvalues = [[ 0.5, -0.2],    # (2, 2) — same shape as output
           [-0.1,  0.3]]

# --- block 3 (COMMENTED OUT) ---
# NOTE: this block is a fragment of a method body in the book, not runnable
# code. It uses `self` at module level, which is undefined outside a class.
# The finished method it belongs to is block 7 at the bottom of this file.
# dweights = np.dot(self.inputs.T, dvalues)
# = [[ 0.6 , -0.5 ],     (3, 2)
#    [ 0.95, -0.25],
#    [ 1.3 , -0.  ]]

# --- block 4 ---
dbiases = np.sum(dvalues, axis=0, keepdims=True)
# column 0: 0.5 + (-0.1) = 0.4
# column 1: -0.2 + 0.3   = 0.1
# = [[0.4, 0.1]]          (1, 2)

# --- block 5 (COMMENTED OUT) ---
# NOTE: this block is a fragment of a method body in the book, not runnable
# code. It uses `self` at module level, which is undefined outside a class.
# The finished method it belongs to is block 7 at the bottom of this file.
# dinputs = np.dot(dvalues, self.weights.T)
# = [[ 0.2 , -0.03, -0.27],   (2, 3)
#    [-0.17,  0.11,  0.21]]

# --- block 6 ---
def forward(self, inputs):
    self.inputs = inputs                                  # save for backward!
    self.output = np.dot(inputs, self.weights) + self.biases

# --- block 7 ---
def backward(self, dvalues):
    # gradients on parameters
    self.dweights = np.dot(self.inputs.T, dvalues)          # (n_inputs, n_neurons)
    self.dbiases  = np.sum(dvalues, axis=0, keepdims=True)  # (1, n_neurons)
    # gradient to pass to the previous layer
    self.dinputs  = np.dot(dvalues, self.weights.T)         # (n_samples, n_inputs)
