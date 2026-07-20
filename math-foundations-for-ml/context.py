"""
Shared context for the Mathematical Foundations for Machine Learning
companion code.

A few chapters use a helper that the book builds in a DIFFERENT chapter and
then reuses without reprinting it. This module holds those shared definitions
so each chapter file can say

    from context import dot

instead of tripping over an undefined name.

Every definition below is COPIED VERBATIM from the chapter cited above it.
Nothing here is invented.
"""

# ---------------------------------------------------------------------------
# Chapter 26: Python for Math - A Fast Start (block 4)
# https://books.vizuara.ai/read/math-foundations-for-ml/python-for-math-a-fast-start
# Reused by chapter 27 (Layer.forward calls dot(row, x) without redefining it).
# ---------------------------------------------------------------------------
def dot(a, b):
    total = 0
    for i in range(len(a)):
        total = total + a[i] * b[i]
    return total            # hand the answer back to the caller


# ---------------------------------------------------------------------------
# Chapter 41: A Neuron from Scratch (block 1)
# https://books.vizuara.ai/read/math-foundations-for-ml/a-neuron-from-scratch
# Chapter 2 shows the same neuron as a preview, calling sigmoid() several
# hundred pages before the book defines it. This is that definition.
# ---------------------------------------------------------------------------
import math


def sigmoid(z):
    return 1 / (1 + math.exp(-z))
