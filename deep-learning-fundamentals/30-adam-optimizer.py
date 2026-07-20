"""
Deep Learning Fundamentals
Chapter 30: Coding the Adam optimizer
Section: Optimizers

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/adam-optimizer

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import numpy as np

# --- block 1 ---
class Optimizer_Adam:
    def __init__(self, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-7):
        self.lr = learning_rate
        self.beta1 = beta1
        self.beta2 = beta2
        self.eps = epsilon
        self.t = 0                      # step count, for bias correction

    def pre_update(self):
        self.t += 1                     # bump ONCE per training step, before touching layers

    def update_params(self, layer):
        # first touch: give this layer zero-filled moment + cache buffers
        if not hasattr(layer, "weight_m"):
            layer.weight_m = np.zeros_like(layer.weights)
            layer.weight_v = np.zeros_like(layer.weights)
            layer.bias_m   = np.zeros_like(layer.biases)
            layer.bias_v   = np.zeros_like(layer.biases)

        # 1st moment (momentum) and 2nd moment (RMSProp cache)
        layer.weight_m = self.beta1 * layer.weight_m + (1 - self.beta1) * layer.dweights
        layer.weight_v = self.beta2 * layer.weight_v + (1 - self.beta2) * layer.dweights**2
        layer.bias_m   = self.beta1 * layer.bias_m   + (1 - self.beta1) * layer.dbiases
        layer.bias_v   = self.beta2 * layer.bias_v   + (1 - self.beta2) * layer.dbiases**2

        # bias-correct both moments using the current step t
        w_m_hat = layer.weight_m / (1 - self.beta1**self.t)
        w_v_hat = layer.weight_v / (1 - self.beta2**self.t)
        b_m_hat = layer.bias_m   / (1 - self.beta1**self.t)
        b_v_hat = layer.bias_v   / (1 - self.beta2**self.t)

        # the update: momentum direction / RMSProp scale
        layer.weights += -self.lr * w_m_hat / (np.sqrt(w_v_hat) + self.eps)
        layer.biases  += -self.lr * b_m_hat / (np.sqrt(b_v_hat) + self.eps)
