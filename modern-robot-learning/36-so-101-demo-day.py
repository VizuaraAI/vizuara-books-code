"""
Modern Robot Learning
Chapter 36: SO-101 Demo Day
Section: Training on Real Robots

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/so-101-demo-day

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# pred, target: shape (chunk_len=50, n_joints=6), in radians
l1 = (pred - target).abs().mean()   # one scalar, averaged over all 300 entries
