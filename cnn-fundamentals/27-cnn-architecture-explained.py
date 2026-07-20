"""
Convolutional Neural Networks Fundamentals
Chapter 27: CNN Architecture Explained
Section: Training a CNN

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/cnn-architecture-explained

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch.nn as nn

model = nn.Sequential(
    nn.Conv2d(3,  16, kernel_size=3, padding=1),  nn.ReLU(),  # stage 1
    nn.MaxPool2d(2),                                            # ÷2
    nn.Conv2d(16, 32, kernel_size=3, padding=1),  nn.ReLU(),  # stage 2
    nn.MaxPool2d(2),                                            # ÷2
    nn.Conv2d(32, 64, kernel_size=3, padding=1),  nn.ReLU(),  # stage 3
    nn.MaxPool2d(2),                                            # ÷2
    nn.Flatten(),
    nn.Linear(64 * 4 * 4, 128),  nn.ReLU(),
    nn.Linear(128, 10),                                        # class scores (logits)
)
