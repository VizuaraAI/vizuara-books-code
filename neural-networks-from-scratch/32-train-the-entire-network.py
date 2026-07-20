"""
Neural Networks from Scratch
Chapter 32: Training the Entire Network
Section: Loss, Optimizer, and Training

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/train-the-entire-network

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- context (added so this file runs standalone) ---
# spiral_data (chapter 21), Layer_Dense (chapters 22-24), Activation_ReLU
# (chapter 26) and Optimizer_SGD (chapter 31) all come from earlier chapters
# of this same book. context.py holds those definitions verbatim.
from context import spiral_data, Layer_Dense, Activation_ReLU, Optimizer_SGD

# --- placeholders (added so this file runs standalone) ---
# The book names the fused softmax + cross-entropy class
# Activation_Softmax_Loss_CategoricalCrossentropy, but no code block in the
# book actually defines it. Chapter 29 shows only its backward pass, under the
# name SoftmaxCrossEntropy (available in context.py).
# See https://books.vizuara.ai/read/neural-networks-from-scratch/train-the-entire-network
Activation_Softmax_Loss_CategoricalCrossentropy = None   # TODO: the fused class

# --- block 1 ---
import numpy as np

X, y = spiral_data(samples=100, classes=3)   # X: (300, 2),  y: (300,)

dense1     = Layer_Dense(2, 8)               # 2 inputs  -> 8 hidden neurons
activation1 = Activation_ReLU()             # the bend between the layers
dense2     = Layer_Dense(8, 3)              # 8 hidden  -> 3 class scores
loss_activation = Activation_Softmax_Loss_CategoricalCrossentropy()  # fused
optimizer  = Optimizer_SGD(learning_rate=1.0)

# --- block 2 ---
for epoch in range(10001):

    # --- 1. FORWARD ---
    dense1.forward(X)                       # (300,2) @ (2,8) -> (300,8)
    activation1.forward(dense1.output)      # ReLU: (300,8) -> (300,8)
    dense2.forward(activation1.output)      # (300,8) @ (8,3) -> (300,3) logits
    loss = loss_activation.forward(dense2.output, y)   # softmax + CE -> scalar

    # a quick accuracy read-out (not used for training, just to watch)
    predictions = np.argmax(loss_activation.output, axis=1)
    accuracy = np.mean(predictions == y)

    # --- 2. BACKWARD ---
    loss_activation.backward(loss_activation.output, y)  # grad = (p - y)/N
    dense2.backward(loss_activation.dinputs)
    activation1.backward(dense2.dinputs)
    dense1.backward(activation1.dinputs)

    # --- 3. UPDATE ---
    optimizer.update_params(dense1)
    optimizer.update_params(dense2)

    # --- 4. REPORT (every 100th epoch) ---
    if not epoch % 100:
        print(f'epoch {epoch}: loss {loss:.3f}, acc {accuracy:.3f}')
