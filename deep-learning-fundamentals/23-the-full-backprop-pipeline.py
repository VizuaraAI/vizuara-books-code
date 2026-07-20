"""
Deep Learning Fundamentals
Chapter 23: Building the full backpropagation pipeline
Section: The Backward Pass (Backpropagation)

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/the-full-backprop-pipeline

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- shared context (not book text) ---
# This chapter drives the network the book builds across chapters 7-22, but it
# never constructs it in a code block of its own. context.py holds those
# objects, copied verbatim from the book.
from context import dense1, relu, dense2, loss_activation

# --- forward reference (hoisted so this file runs top to bottom) ---
# Block 1 below uses `y`, which the chapter only defines in block 2. Copied
# verbatim from block 2 and hoisted here so the file is self-contained.
import numpy as np

y = np.array([[1.0, 0.0, 0.0],
              [0.0, 0.0, 1.0]])

# --- block 1 ---
# forward already done; loss_activation.output holds ŷ (the softmax probabilities)

# 1. fused softmax + cross-entropy: the very first gradient
loss_activation.backward(loss_activation.output, y)        # sets loss_activation.dinputs = (ŷ - y)/batch

# 2. hand it to dense2 as its dvalues
dense2.backward(loss_activation.dinputs)                    # sets dense2.dweights, dense2.dbiases, dense2.dinputs

# 3. hand dense2's dinputs to ReLU
relu.backward(dense2.dinputs)                               # sets relu.dinputs

# 4. hand ReLU's dinputs to dense1
dense1.backward(relu.dinputs)                              # sets dense1.dweights, dense1.dbiases, dense1.dinputs

# --- block 2 ---
import numpy as np

# ŷ from the forward pass (2 samples, 3 classes) — rows sum to 1
y_hat = np.array([[0.7, 0.2, 0.1],
                  [0.1, 0.3, 0.6]])
# true classes, one-hot: sample 0 is class 0, sample 1 is class 2
y = np.array([[1.0, 0.0, 0.0],
              [0.0, 0.0, 1.0]])
batch = 2

# --- block 3 ---
dz2 = (y_hat - y) / batch
#   ([[0.7-1, 0.2-0, 0.1-0],      [[-0.15,  0.10,  0.05],
#     [0.1-0, 0.3-0, 0.6-1]]) / 2 = [ 0.05,  0.15, -0.20]]     shape (2, 3)

# --- block 4 ---
# forward-order list of the trainable/activation layers
layers = [dense1, relu, dense2]

# kick off the relay with the fused loss+softmax gradient
loss_activation.backward(loss_activation.output, y)
dvalues = loss_activation.dinputs        # the first upstream gradient

# walk the network BACKWARD, handing each dinputs to the next
for layer in reversed(layers):
    layer.backward(dvalues)
    dvalues = layer.dinputs               # this layer's output becomes the next's input
