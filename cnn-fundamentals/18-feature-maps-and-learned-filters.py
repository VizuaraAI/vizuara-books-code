"""
Convolutional Neural Networks Fundamentals
Chapter 18: Feature Maps and Learned Filters
Section: Filtering and Convolution

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/feature-maps-and-learned-filters

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch.nn as nn

# input tensor shape: (N, 1, 28, 28)  = (batch, channels, H, W)
conv1 = nn.Conv2d(in_channels=1,  out_channels=8,  kernel_size=3, padding=1)
conv2 = nn.Conv2d(in_channels=8,  out_channels=16, kernel_size=3, padding=1)

# after conv1 + ReLU: (N, 8, 28, 28)   → 8 feature maps  (8 filters)
# after conv2 + ReLU: (N, 16, 28, 28)  → 16 feature maps (16 filters)
