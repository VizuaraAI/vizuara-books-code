"""
Deep Learning Fundamentals
Chapter 37: Classification project: Fashion-MNIST
Section: Hands-On Projects

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/classification-fashion-mnist

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import numpy as np

# --- shared context (not book text) ---
# This chapter reuses ReLU (chapter 20), copied verbatim into context.py.
from context import ReLU

# --- placeholders the reader supplies ---
# The chapter also names two classes it never defines anywhere in the book:
# `DenseLayer` (the book's class is called `Dense`, chapters 7/16) and
# `Softmax` (the book has a `softmax` function in chapter 9 and a fused
# `SoftmaxCrossEntropy` in chapter 24, but no standalone `Softmax` class).
# Stubbed rather than guessed at.
# See https://books.vizuara.ai/read/deep-learning-fundamentals/classification-fashion-mnist
DenseLayer = None   # TODO: the book's equivalent class is `Dense` (chapters 7, 16)
Softmax    = None   # TODO: the book has `softmax()` (chapter 9), not a Softmax class
X_batch    = None   # TODO: a batch of Fashion-MNIST images, shape (32, 784)
y_true     = None   # TODO: the matching labels, shape (32,)

# --- block 1 ---
# X_batch shape: (32, 784)          # 32 images, 784 pixels each
dense1  = DenseLayer(784, 128)      # W1: (784, 128)
relu    = ReLU()
dense2  = DenseLayer(128, 10)       # W2: (128, 10)
softmax = Softmax()

a = relu.forward(dense1.forward(X_batch))   # (32, 128)
logits = dense2.forward(a)                   # (32, 10)   raw scores
probs  = softmax.forward(logits)             # (32, 10)   rows sum to 1

# --- block 2 ---
predictions = np.argmax(probs, axis=1)   # (32,) predicted class per image
accuracy = np.mean(predictions == y_true)
