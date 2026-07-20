"""
Convolutional Neural Networks Fundamentals
Chapter 13: Introduction to Convolutional Neural Networks
Section: Why Convolutional Neural Networks

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/introduction-to-cnns

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
image = [[10, 10, 0, 0],
         [10, 10, 0, 0],
         [10, 10, 0, 0],
         [10, 10, 0, 0]]      # bright-left / dark-right: a vertical edge

kernel = [[-1, 0, 1],
          [-2, 0, 2],
          [-1, 0, 1]]         # vertical Sobel: fires on left→right brightness change
