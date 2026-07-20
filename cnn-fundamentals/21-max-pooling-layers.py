"""
Convolutional Neural Networks Fundamentals
Chapter 21: Max Pooling Layers
Section: The Layers of a CNN

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/max-pooling-layers

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch

# --- block 1 ---
import torch.nn as nn

pool = nn.MaxPool2d(kernel_size=2, stride=2)   # the default downsampler

# feature maps from a conv+ReLU block: (batch=1, channels=64, 32, 32)
x = torch.rand(1, 64, 32, 32)
y = pool(x)          # -> (1, 64, 16, 16): H and W halved, 64 channels untouched
