"""
Vision-Language-Action & World Models for Robotics
Chapter 9: ACT: The Action Chunking Transformer
Section: Introduction to Vision-Language-Action

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/act-the-action-chunking-transformer

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# one action = (steer, throttle),  d = 2
single_step = [0.10, 0.55]                 # shape (2,)  — just "now"

chunk = [[0.10, 0.55],   # t+0   steer right a little, cruise
         [0.13, 0.55],   # t+1
         [0.17, 0.54],   # t+2   steering ramps into the turn
         [0.22, 0.52]]   # t+3   shape (4, 2) — a plan, not a reflex
