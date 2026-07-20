"""
Neural Networks from Scratch
Chapter 8: The Logic for Calculating Weight Values
Section: Weights and Wiring

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/logic-for-calculating-w-values

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
# The layer's shape is whatever the reader chooses. Chapter 22 builds its
# first hidden layer as 2 -> 8, so those are used here as stand-in sizes.
# See https://books.vizuara.ai/read/neural-networks-from-scratch/logic-for-calculating-w-values
n_inputs  = 2   # TODO: how many numbers arrive at this layer
n_neurons = 8   # TODO: how many neurons this layer has

# --- block 1 ---
weights = 0.01 * np.random.randn(n_inputs, n_neurons)
biases  = np.zeros((1, n_neurons))
