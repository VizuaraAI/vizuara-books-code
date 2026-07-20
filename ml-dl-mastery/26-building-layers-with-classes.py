"""
Machine Learning & Deep Learning Mastery
Chapter 26: Building Layers with Python Classes
Section: Neural Networks: The Forward Pass

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/building-layers-with-classes

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

X = np.random.randn(3, 4)          # 3 samples, 4 features each

W1 = 0.01 * np.random.randn(4, 5)  # layer 1: 4 in, 5 out
b1 = np.zeros((1, 5))
W2 = 0.01 * np.random.randn(5, 2)  # layer 2: 5 in, 2 out
b2 = np.zeros((1, 2))

Z1 = X  @ W1 + b1                   # (3, 5)
Z2 = Z1 @ W2 + b2                   # (3, 2)

# --- block 2 ---
import numpy as np

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        # weights shaped (n_inputs, n_neurons) so no transpose is needed later
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases  = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.inputs = inputs                              # cache for backprop
        self.output = inputs @ self.weights + self.biases
        return self.output

# --- block 3 ---
np.random.seed(0)
X = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])      # shape (2, 3)

layer1 = Layer_Dense(3, 4)           # 3 inputs -> 4 neurons
out = layer1.forward(X)
print(out.shape)                     # (2, 4)

# --- block 4 ---
layer2 = Layer_Dense(4, 1)           # 4 inputs -> 1 output
final  = layer2.forward(out)
print(final.shape)                   # (2, 1)

# --- block 5 ---
class ReLU:
    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.maximum(0, inputs)   # f(z) = max(0, z)
        return self.output

network = [
    Layer_Dense(4, 16), ReLU(),
    Layer_Dense(16, 8),  ReLU(),
    Layer_Dense(8, 3),
]

X = np.random.randn(10, 4)     # batch of 10 samples, 4 features
out = X
for layer in network:
    out = layer.forward(out)   # feed each layer's output into the next
print(out.shape)               # (10, 3)
