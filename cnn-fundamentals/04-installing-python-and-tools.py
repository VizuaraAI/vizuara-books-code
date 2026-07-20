"""
Convolutional Neural Networks Fundamentals
Chapter 4: Setting Up Python and Your Tools
Section: Getting Started

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/installing-python-and-tools

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np
import torch

print("numpy:", np.__version__)          # e.g. 2.1.3
print("torch:", torch.__version__)        # e.g. 2.5.1
print("CUDA available:", torch.cuda.is_available())   # True only if you have an NVIDIA GPU

# --- block 2 ---
import torch
import torch.nn.functional as F

# a 4x4 image: left half dark (0), right half bright (10) — a vertical edge down the middle
image = torch.tensor([[0., 0., 10., 10.],
                      [0., 0., 10., 10.],
                      [0., 0., 10., 10.],
                      [0., 0., 10., 10.]])

# vertical Sobel kernel: responds to a left-to-right brightness change
kernel = torch.tensor([[-1., 0., 1.],
                       [-2., 0., 2.],
                       [-1., 0., 1.]])

# conv2d wants shape (N, C, H, W); add batch and channel dims
out = F.conv2d(image.reshape(1, 1, 4, 4), kernel.reshape(1, 1, 3, 3))
print(out)     # tensor([[[[40., 40.], [40., 40.]]]])
