"""
Deep Learning Fundamentals
Chapter 7: Implementing the dense layer class
Section: The Forward Pass

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/the-dense-layer-class

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

class Dense:
    def __init__(self, n_inputs, n_neurons):
        # small random weights, zero biases
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)  # (n_inputs, n_neurons)
        self.biases  = np.zeros((1, n_neurons))                     # (1, n_neurons)

    def forward(self, inputs):
        self.output = inputs @ self.weights + self.biases           # (batch, n_neurons)

# --- block 2 ---
np.random.seed(0)

X = np.array([[1.0, 2.0, 3.0, 2.5],
              [2.0, 5.0, -1.0, 2.0]])   # a batch of 2 samples, 4 features each → (2, 4)

layer1 = Dense(4, 5)     # 4 inputs  -> 5 neurons
layer2 = Dense(5, 3)     # 5 inputs  -> 3 neurons  (the 5 must match layer1's 5)

layer1.forward(X)                  # fills layer1.output, shape (2, 5)
layer2.forward(layer1.output)      # fills layer2.output, shape (2, 3)

print(layer1.output.shape)   # (2, 5)
print(layer2.output.shape)   # (2, 3)
