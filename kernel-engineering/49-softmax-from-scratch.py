"""
Kernel Engineering
Chapter 49: Softmax from scratch (and online)
Section: Kernels for Inference

Read this chapter: https://books.vizuara.ai/read/kernel-engineering/softmax-from-scratch

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
def softmax_naive(x):
    e = np.exp(x)          # <-- overflows the moment max(x) is large
    return e / e.sum()

# --- block 2 ---
def softmax_stable(x):
    m = x.max()            # pass 1: the max
    e = np.exp(x - m)      # pass 2: shifted exponentials + their sum
    return e / e.sum()     # pass 3: normalize

# --- block 3 ---
def softmax_online(x):
    m = -np.inf            # running max
    d = 0.0                # running denominator, relative to current m
    for xi in x:                       # single pass
        m_new = max(m, xi)
        d = d * np.exp(m - m_new) + np.exp(xi - m_new)
        m = m_new
    return np.exp(x - m) / d           # pointwise; fuses into the consumer
