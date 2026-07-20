"""
RLHF from Scratch
Chapter 4: Prerequisites and Notation
Section: Why Alignment

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/prerequisites-and-notation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

z = np.array([0.5, 1.0, 2.2, 1.8])          # logits for [the, cat, sat, sad]
probs = np.exp(z) / np.exp(z).sum()
# probs ≈ [0.08, 0.14, 0.46, 0.31]  — a distribution over the 4 tokens
