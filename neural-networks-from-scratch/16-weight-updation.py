"""
Neural Networks from Scratch
Chapter 16: Weight Updation with Gradient Descent
Section: How a Network Learns

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/weight-updation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- placeholders (added so this file runs standalone) ---
# The block is the update step applied to one layer. `layer` is a Layer_Dense
# (chapters 22-24) that has ALREADY been through a backward pass, so it carries
# .dweights and .dbiases; a freshly constructed one does not.
# See https://books.vizuara.ai/read/neural-networks-from-scratch/weight-updation
layer = None            # TODO: a Layer_Dense whose backward() has already run
learning_rate = 0.1     # TODO: your step size (chapter 12 uses 0.1)

# --- block 1 ---
# after the backward pass has filled in layer.dweights and layer.dbiases
layer.weights = layer.weights - learning_rate * layer.dweights
layer.biases  = layer.biases  - learning_rate * layer.dbiases
