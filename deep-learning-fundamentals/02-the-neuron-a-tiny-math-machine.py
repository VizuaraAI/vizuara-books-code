"""
Deep Learning Fundamentals
Chapter 2: The neuron: a tiny math machine
Section: Foundations

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/the-neuron-a-tiny-math-machine

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
inputs  = [0.8, 0.3, 0.9]
weights = [1.5, 0.4, -0.7]
bias    = -0.5

z = 0.0
for x, w in zip(inputs, weights):
    z += x * w          # multiply each input by its weight, accumulate
z += bias               # nudge by the bias

print(z)                # 0.18999999999999995  ≈ 0.19

# --- block 2 ---
import numpy as np

inputs  = np.array([0.8, 0.3, 0.9])
weights = np.array([1.5, 0.4, -0.7])
bias    = -0.5

z = np.dot(weights, inputs) + bias   # the whole neuron, in one line
print(z)                              # 0.19
