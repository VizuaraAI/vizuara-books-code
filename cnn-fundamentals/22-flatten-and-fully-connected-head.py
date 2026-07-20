"""
Convolutional Neural Networks Fundamentals
Chapter 22: Flatten and the Fully Connected Head
Section: The Layers of a CNN

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/flatten-and-fully-connected-head

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch.nn as nn

class Head(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.flatten = nn.Flatten()        # (N, 16, 7, 7) -> (N, 784)
        self.fc1     = nn.Linear(784, 64)  # 784*64 + 64 = 50,240 params
        self.relu    = nn.ReLU()
        self.fc2     = nn.Linear(64, num_classes)  # 64*10 + 10 = 650 params

    def forward(self, x):        # x: (N, 16, 7, 7) from the conv stack
        x = self.flatten(x)      # (N, 784)
        x = self.relu(self.fc1(x))   # (N, 64)
        x = self.fc2(x)          # (N, 10)  <- logits, no softmax here
        return x
