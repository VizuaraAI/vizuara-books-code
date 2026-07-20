"""
Kernel Engineering
Chapter 51: Attention, the naive way
Section: Kernels for Inference

Read this chapter: https://books.vizuara.ai/read/kernel-engineering/attention-naive

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import math

# --- block 1 ---
# Q, K, V : (N, d)
S = (Q @ K.transpose(-2, -1)) / math.sqrt(d)   # (N, N)  scores
P = softmax(S, dim=-1)                          # (N, N)  probabilities
O = P @ V                                       # (N, d)  output
