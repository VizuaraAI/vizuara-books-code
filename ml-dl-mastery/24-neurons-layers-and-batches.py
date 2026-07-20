"""
Machine Learning & Deep Learning Mastery
Chapter 24: Neurons, Layers, and Batches
Section: Neural Networks: The Forward Pass

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/neurons-layers-and-batches

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def relu(z):
    return np.maximum(0, z)          # elementwise, keeps shape

# a batch of 32 flattened MNIST images
X  = np.random.randn(32, 784)
W1 = np.random.randn(784, 128) * 0.01;  b1 = np.zeros(128)   # layer 1
W2 = np.random.randn(128, 10)  * 0.01;  b2 = np.zeros(10)    # layer 2

Z1 = X  @ W1 + b1;  A1 = relu(Z1)     # (32, 784)@(784,128) -> (32, 128)
Z2 = A1 @ W2 + b2                     # (32, 128)@(128, 10)  -> (32,  10)
print(Z1.shape, Z2.shape)            # (32, 128) (32, 10)
