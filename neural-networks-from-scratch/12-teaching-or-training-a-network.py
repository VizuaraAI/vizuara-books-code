"""
Neural Networks from Scratch
Chapter 12: Teaching, or Training, a Neural Network
Section: How a Network Learns

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/teaching-or-training-a-network

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- placeholders (added so this file runs standalone) ---
# The chapter's own trailing comment states the worked example it is stepping
# through: w = 1 and grad = -32, giving w = 1 - 0.1 * (-32) = 4.2.
# See https://books.vizuara.ai/read/neural-networks-from-scratch/teaching-or-training-a-network
w    = 1.0     # TODO: the weight being updated (the chapter's example uses 1)
grad = -32.0   # TODO: dLoss/dw from the backward pass (the chapter's example uses -32)

# --- block 1 ---
learning_rate = 0.1
w = w - learning_rate * grad     # w = 1 - 0.1 * (-32) = 1 + 3.2 = 4.2
