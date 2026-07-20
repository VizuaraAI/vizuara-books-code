"""
Machine Learning Fundamentals
Chapter 35: Momentum in Gradient Descent
Section: Neural Networks

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/momentum-in-gradient-descent

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
v = beta * v + grad          # blend: mostly old velocity, a little new gradient
w = w - eta * v              # step along the accumulated velocity, not the raw gradient
