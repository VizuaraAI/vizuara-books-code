"""
Vision-Language-Action & World Models for Robotics
Chapter 18: Self-Paced VLA Deep Dive
Section: From Simulation to the TurboPi Car

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/self-paced-vla-deep-dive

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
d          = 2      # action = (steer, throttle)
k          = 4      # chunk size: predict 4 future actions at once
state_dim  = 4      # proprioceptive robot state q
d_model    = 8      # transformer hidden width
image      = (3, 64, 64)   # one RGB camera frame
# goal: policy(image, q) -> action_chunk of shape (k, d) = (4, 2)

# --- block 2 ---
action_chunk = [[0.10, 0.55],   # t+0  steer slightly right, cruise
                [0.14, 0.55],   # t+1
                [0.19, 0.54],   # t+2  steering ramps into the turn
                [0.25, 0.52]]   # t+3  shape (4, 2) — a plan, not a reflex
