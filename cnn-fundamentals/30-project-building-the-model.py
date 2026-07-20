"""
Convolutional Neural Networks Fundamentals
Chapter 30: Building the CNN in Python
Section: Project: Brain Tumor Classifier

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/project-building-the-model

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch.nn as nn
import torch.nn.functional as F

class TumorCNN(nn.Module):
    def __init__(self, num_classes=2):
        super().__init__()
        # feature extractor: 3 conv blocks, channels 1 -> 16 -> 32 -> 64
        self.conv1 = nn.Conv2d(1,  16, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.pool  = nn.MaxPool2d(2)          # one pool, reused 3x (no weights)

        # dense head: flatten 64*16*16 -> 128 -> num_classes
        self.fc1 = nn.Linear(64 * 16 * 16, 128)
        self.fc2 = nn.Linear(128, num_classes)

    def forward(self, x):                      # x: (N, 1, 128, 128)
        x = self.pool(F.relu(self.conv1(x)))   # -> (N, 16, 64, 64)
        x = self.pool(F.relu(self.conv2(x)))   # -> (N, 32, 32, 32)
        x = self.pool(F.relu(self.conv3(x)))   # -> (N, 64, 16, 16)
        x = x.flatten(1)                       # -> (N, 16384)
        x = F.relu(self.fc1(x))                # -> (N, 128)
        x = self.fc2(x)                        # -> (N, 2)  logits, NO softmax
        return x

# --- block 2 ---
import torch

model = TumorCNN(num_classes=2)
dummy = torch.randn(4, 1, 128, 128)   # a fake batch of 4 grayscale scans
out = model(dummy)
print(out.shape)                      # torch.Size([4, 2])

# --- block 3 ---
total = sum(p.numel() for p in model.parameters())
print(f"{total:,} parameters")        # 2,120,834 parameters
