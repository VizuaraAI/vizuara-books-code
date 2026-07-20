"""
Deep Learning Fundamentals
Chapter 35: Dropout layers
Section: Regularization and Testing

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/dropout-layers

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
class Dropout:
    def __init__(self, rate):
        self.rate = rate                 # p: fraction to DROP (e.g. 0.5)
        self.keep = 1.0 - rate           # fraction to KEEP

    def forward(self, inputs, training):
        self.inputs = inputs
        if not training:                 # TEST: identity, no randomness
            self.output = inputs
            return
        # draw a 0/1 mask, already scaled by 1/keep (inverted dropout)
        self.mask = np.random.binomial(1, self.keep, inputs.shape) / self.keep
        self.output = inputs * self.mask

    def backward(self, dvalues):
        # gradient flows through survivors only, with the SAME scaling
        self.dinputs = dvalues * self.mask
