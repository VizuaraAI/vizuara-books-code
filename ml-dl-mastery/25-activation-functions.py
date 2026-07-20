"""
Machine Learning & Deep Learning Mastery
Chapter 25: Activation Functions
Section: Neural Networks: The Forward Pass

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/activation-functions

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def relu(z):
    return max(0, z)   # keep positives, zero out negatives
