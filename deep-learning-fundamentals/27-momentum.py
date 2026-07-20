"""
Deep Learning Fundamentals
Chapter 27: Momentum in training
Section: Optimizers

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/momentum

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import numpy as np

# --- block 1 (commented out) ---
# NOTE: this block is prose in the book, not runnable code. It is the momentum
# update written as maths notation - beta, v, lr, dw and w are symbols, and the
# chapter never assigns any of them. Block 2 below is the runnable version.
# # momentum: keep a velocity, let the gradient only nudge it
# v = beta * v - lr * dw     # decay old velocity, add a small push downhill
# w = w + v                  # step by the accumulated velocity, not the raw gradient

# --- block 2 ---
class Optimizer_SGD_Momentum:
    def __init__(self, learning_rate=1.0, momentum=0.9):
        self.lr = learning_rate
        self.momentum = momentum

    def update_params(self, layer):
        # first time we touch this layer, give it zero-filled velocity buffers
        if not hasattr(layer, "weight_v"):
            layer.weight_v = np.zeros_like(layer.weights)
            layer.bias_v   = np.zeros_like(layer.biases)

        # v = beta*v - lr*grad   (grads came from the backward pass)
        layer.weight_v = self.momentum * layer.weight_v - self.lr * layer.dweights
        layer.bias_v   = self.momentum * layer.bias_v   - self.lr * layer.dbiases

        # w = w + v
        layer.weights += layer.weight_v
        layer.biases  += layer.bias_v
