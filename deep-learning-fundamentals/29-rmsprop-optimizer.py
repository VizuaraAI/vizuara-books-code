"""
Deep Learning Fundamentals
Chapter 29: Coding the RMSProp optimizer
Section: Optimizers

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/rmsprop-optimizer

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

class Optimizer_RMSprop:
    def __init__(self, learning_rate=0.001, decay=0.0, epsilon=1e-7, rho=0.9):
        self.learning_rate = learning_rate   # lr_0
        self.current_lr    = learning_rate
        self.decay         = decay
        self.iterations    = 0
        self.epsilon       = epsilon          # keeps the division safe
        self.rho           = rho              # cache decay rate, ~0.9

    def pre_update(self):
        if self.decay:
            self.current_lr = self.learning_rate / (1 + self.decay * self.iterations)

    def update(self, layer):
        # lazily create the caches the first time we see this layer
        if not hasattr(layer, "weight_cache"):
            layer.weight_cache = np.zeros_like(layer.weights)
            layer.bias_cache   = np.zeros_like(layer.biases)

        # moving average of squared gradients — the ONE new idea
        layer.weight_cache = self.rho * layer.weight_cache + (1 - self.rho) * layer.dweights**2
        layer.bias_cache   = self.rho * layer.bias_cache   + (1 - self.rho) * layer.dbiases**2

        # same adaptive step as AdaGrad, using the averaged cache
        layer.weights += -self.current_lr * layer.dweights / (np.sqrt(layer.weight_cache) + self.epsilon)
        layer.biases  += -self.current_lr * layer.dbiases  / (np.sqrt(layer.bias_cache)   + self.epsilon)

    def post_update(self):
        self.iterations += 1

# --- block 2 ---
optimizer = Optimizer_RMSprop(learning_rate=0.001, decay=1e-4, rho=0.9)
