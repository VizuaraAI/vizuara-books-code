"""
Modern Robot Learning
Chapter 33: Training an ACT Policy from Scratch
Section: Training on Real Robots

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/training-an-act-policy-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
loss = l1_action_loss + kl_weight * kl_divergence
