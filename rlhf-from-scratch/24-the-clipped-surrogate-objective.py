"""
RLHF from Scratch
Chapter 24: The Clipped Surrogate Objective
Section: Proximal Policy Optimization

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/the-clipped-surrogate-objective

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
clipped = clip(ratio, 1 - eps, 1 + eps)   # eps = 0.2  →  ratio kept in [0.8, 1.2]
naive   = clipped * advantage             # the tempting-but-wrong objective
