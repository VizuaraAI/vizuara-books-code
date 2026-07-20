"""
Deep Learning Fundamentals
Chapter 20: Backpropagation through ReLU
Section: The Backward Pass (Backpropagation)

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/backprop-through-relu

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

class Activation_ReLU:
    def forward(self, inputs):
        self.inputs = inputs                 # stash for the backward pass
        self.output = np.maximum(0, inputs)  # negatives → 0, positives unchanged

    def backward(self, dvalues):
        self.dinputs = dvalues.copy()        # start from the upstream gradient
        self.dinputs[self.inputs <= 0] = 0   # kill it where the input was not positive
