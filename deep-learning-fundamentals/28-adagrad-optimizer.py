"""
Deep Learning Fundamentals
Chapter 28: Coding the AdaGrad optimizer
Section: Optimizers

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/adagrad-optimizer

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

class Optimizer_AdaGrad:
    def __init__(self, learning_rate=1.0, epsilon=1e-7):
        self.learning_rate = learning_rate
        self.epsilon = epsilon          # tiny constant, avoids /0

    def update_params(self, layer):
        # First time we touch this layer, create its per-parameter caches.
        if not hasattr(layer, 'weight_cache'):
            layer.weight_cache = np.zeros_like(layer.weights)
            layer.bias_cache   = np.zeros_like(layer.biases)

        # 1. accumulate squared gradients (element-wise, per parameter)
        layer.weight_cache += layer.dweights ** 2
        layer.bias_cache   += layer.dbiases  ** 2

        # 2. step, scaled per-parameter by 1 / sqrt(cache)
        layer.weights -= (self.learning_rate * layer.dweights /
                          (np.sqrt(layer.weight_cache) + self.epsilon))
        layer.biases  -= (self.learning_rate * layer.dbiases /
                          (np.sqrt(layer.bias_cache)  + self.epsilon))
