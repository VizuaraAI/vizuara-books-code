"""
Vision-Language-Action & World Models for Robotics
Chapter 24: What Is a World Model?
Section: World Models

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/what-is-a-world-model

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# The one equation that defines a world model.
# Given where you are and what you do, predict where you land.
s_next = world_model(s_t, a_t)     # predicted next state
# usually paired with a reward/observation head:
r_next = reward_head(s_t, a_t)     # predicted reward
