"""
Modern Robot Learning
Chapter 8: Why Generative Models for Robotics
Section: Deep Generative Modeling

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/why-generative-models-for-robotics

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# behavioral cloning, the naive version
loss = ((f(o) - a) ** 2).mean()   # mean squared error
