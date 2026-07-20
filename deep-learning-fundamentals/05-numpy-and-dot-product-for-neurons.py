"""
Deep Learning Fundamentals
Chapter 5: The beauty of NumPy and the dot product
Section: Neural Network Architecture

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/numpy-and-dot-product-for-neurons

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
inputs  = [1.0, 2.0, 3.0, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0],    # neuron 1
           [0.5, -0.91, 0.26, -0.5], # neuron 2
           [-0.26, -0.27, 0.17, 0.87]] # neuron 3
biases  = [2.0, 3.0, 0.5]

layer_outputs = []
for neuron_weights, neuron_bias in zip(weights, biases):
    z = 0
    for w, x in zip(neuron_weights, inputs):
        z += w * x            # multiply-and-accumulate, one term at a time
    z += neuron_bias
    layer_outputs.append(z)

# --- block 2 ---
import numpy as np

output = np.dot(weights[0], inputs) + biases[0]   # 4.8

# --- block 3 ---
weights = np.array([[ 0.2,  0.8, -0.5,  1.0],
                    [ 0.5, -0.91, 0.26, -0.5],
                    [-0.26,-0.27, 0.17, 0.87]])   # shape (3, 4)
biases  = np.array([2.0, 3.0, 0.5])               # shape (3,)
inputs  = np.array([1.0, 2.0, 3.0, 2.5])          # shape (4,)

# --- block 4 ---
layer_outputs = np.dot(weights, inputs) + biases
# array([4.8, 1.21, 2.385])

# --- block 5 ---
X = np.array([[1.0,  2.0,  3.0,  2.5],   # sample 1
              [2.0,  5.0, -1.0,  2.0],   # sample 2
              [-1.5, 2.7,  3.3, -0.8]])  # shape (3, 4)

layer_outputs = X @ weights.T + biases    # shape (3, 3)
