"""
RLHF from Scratch
Chapter 8: States, Actions, and the Policy
Section: The LLM as an RL Agent

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/states-actions-and-the-policy

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
vocab = ["Tell", "me", "a", "story", "joke", "."]   # V = 6
#          0       1    2     3        4     5        (token IDs)

# --- block 2 ---
import numpy as np

# logits for [Tell, me, a, story, joke, .]  at state s_1 = "Tell me a"
z = np.array([-1.0, -0.5, 0.2, 2.4, 1.6, -0.8])

probs = np.exp(z) / np.exp(z).sum()
# probs ≈ [0.020, 0.033, 0.066, 0.592, 0.266, 0.024]  (worked out by hand below)
