"""
Reinforcement Learning
Chapter 17: Why Optimize the Policy Directly?
Section: Policy Gradient Methods from Scratch

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/why-optimize-the-policy-directly

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

x = np.array([1.0, 0.5, -1.0, 2.0])      # state features, d = 4

W = np.array([[ 0.2,  0.1,  0.0,  0.3],   # weights for "left"
              [-0.1,  0.4,  0.2, -0.2],   # weights for "stay"
              [ 0.5, -0.3,  0.1,  0.6]])  # weights for "right"

logits = W @ x                            # 3 raw scores
probs  = np.exp(logits) / np.exp(logits).sum()
print(logits)   # [ 0.85 -0.5   1.45]
print(probs)    # [0.32 0.08 0.59]
