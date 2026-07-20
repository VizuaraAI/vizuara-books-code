"""
Deep Learning Fundamentals
Chapter 16: Backpropagation through a layer of neurons
Section: The Backward Pass (Backpropagation)

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/backprop-through-a-layer

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
class Dense:
    def forward(self, inputs):
        self.inputs = inputs                          # remembered for the backward pass
        self.output = inputs @ self.weights + self.biases

    def backward(self, dvalues):                      # dvalues: (batch, n_neurons)
        self.dweights = self.inputs.T @ dvalues       # (n_inputs, n_neurons)  — same shape as weights
        self.dbiases  = np.sum(dvalues, axis=0, keepdims=True)   # (1, n_neurons) — same shape as biases
        self.dinputs  = dvalues @ self.weights.T      # (batch, n_inputs) — same shape as inputs
