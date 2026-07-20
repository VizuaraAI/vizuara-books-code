"""
Neural Networks from Scratch
Chapter 13: The Forward Pass and Cross-Entropy Loss
Section: How a Network Learns

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/forward-pass-and-cross-entropy-loss

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import numpy as np

# --- placeholders (added so this file runs standalone) ---
# This block is the tail end of a forward pass. Its three inputs come from
# whatever batch the reader is running; the chapter does not build them here.
# See https://books.vizuara.ai/read/neural-networks-from-scratch/forward-pass-and-cross-entropy-loss
p = None   # TODO: (n_samples, n_classes) softmax probabilities from the forward pass
n = None   # TODO: number of samples in the batch
y = None   # TODO: (n_samples,) integer class labels

# --- block 1 ---
p_clipped = np.clip(p, 1e-7, 1 - 1e-7)   # never exactly 0 or 1
loss = -np.log(p_clipped[range(n), y])   # pick out p[y] for each sample
