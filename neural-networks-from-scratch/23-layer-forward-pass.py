"""
Neural Networks from Scratch
Chapter 23: Coding the Layer Forward Pass
Section: Coding the Layers

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/layer-forward-pass

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases  = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.inputs = inputs                          # remember for the backward pass
        self.output = inputs @ self.weights + self.biases

# --- block 2 ---
import numpy as np
np.random.seed(0)

X = np.random.randn(3, 2)          # a stand-in batch: 3 points, 2 features

layer1 = Layer_Dense(2, 8)         # 2 inputs → 8 neurons
layer1.forward(X)

print(layer1.output.shape)         # (3, 8)
print(layer1.output)               # 3 rows of 8 tiny numbers, all near zero
