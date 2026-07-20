"""
Neural Networks from Scratch
Chapter 3: A Mathematical Function to Switch a Neuron On or Off
Section: The Ten Questions

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/the-switch-on-off-function

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import numpy as np

# --- placeholders (added so this file runs standalone) ---
# Block 1 is the neuron's weighted-sum formula. The book writes it as maths;
# the two inputs, the two weights and the bias are values the reader supplies.
# See https://books.vizuara.ai/read/neural-networks-from-scratch/the-switch-on-off-function
x1 = 0.0   # TODO: first input feature
x2 = 0.0   # TODO: second input feature
w1 = 0.0   # TODO: weight on x1
w2 = 0.0   # TODO: weight on x2
b  = 0.0   # TODO: the neuron's bias

# --- block 1 ---
z = w1*x1 + w2*x2 + b

# --- block 2 ---
def step(z):
    return 1 if z > 0 else 0

# --- block 3 ---
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# --- block 4 ---
def relu(z):
    return np.maximum(0, z)
