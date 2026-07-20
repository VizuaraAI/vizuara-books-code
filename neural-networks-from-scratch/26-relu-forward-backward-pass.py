"""
Neural Networks from Scratch
Chapter 26: ReLU: Forward and Backward Pass
Section: Coding the Layers

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/relu-forward-backward-pass

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
class Activation_ReLU:
    def forward(self, inputs):
        self.inputs = inputs                    # remember for the backward pass
        self.output = np.maximum(0, inputs)     # negatives -> 0, positives unchanged

# --- block 2 ---
    def backward(self, dvalues):
        self.dinputs = dvalues.copy()      # start from the incoming gradient
        self.dinputs[self.inputs <= 0] = 0 # kill the gradient where input was <= 0

# --- block 3 ---
class Activation_ReLU:
    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.maximum(0, inputs)

    def backward(self, dvalues):
        self.dinputs = dvalues.copy()
        self.dinputs[self.inputs <= 0] = 0
