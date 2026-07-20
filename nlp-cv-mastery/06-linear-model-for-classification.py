"""
NLP & Computer Vision Mastery
Chapter 6: A Linear Model for 5-Class Classification
Section: From Linear Models to Deep Networks

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/linear-model-for-classification

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
W = [[ 0.5, -0.2,  0.1],   # weights for class "rose"
     [-0.3,  0.4,  0.6]]    # weights for class "sunflower"
b = [0.0, 0.1]
x = [0.9, 0.2, 0.7]         # a 3-pixel "image"
