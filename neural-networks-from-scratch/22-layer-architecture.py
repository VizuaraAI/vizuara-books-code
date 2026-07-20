"""
Neural Networks from Scratch
Chapter 22: Designing the Dense Layer Class
Section: Coding the Layers

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/layer-architecture

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        # weights: one column per neuron, one row per input
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)  # (n_inputs, n_neurons)
        self.biases  = np.zeros((1, n_neurons))                     # (1, n_neurons)

    def forward(self, inputs):
        pass   # we implement this next chapter

# --- block 2 ---
dense1 = Layer_Dense(2, 8)    # hidden layer:  2 inputs  -> 8 neurons
dense2 = Layer_Dense(8, 3)    # output layer:  8 inputs  -> 3 neurons
