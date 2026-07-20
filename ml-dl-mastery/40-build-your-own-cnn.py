"""
Machine Learning & Deep Learning Mastery
Chapter 40: Build Your Own CNN Application
Section: CNNs & Decision Trees

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/build-your-own-cnn

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not book code) ---
# The chapter uses these names without defining them. Placeholders so the file runs.
train_loader = None  # TODO: a torch DataLoader yielding (images, labels) batches

# --- block 1 ---
import torch.nn as nn

class SmallCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding=1),   # (3,32,32)  -> (32,32,32)
            nn.ReLU(),
            nn.MaxPool2d(2),                               # -> (32,16,16)
            nn.Conv2d(32, 64, kernel_size=3, padding=1),   # -> (64,16,16)
            nn.ReLU(),
            nn.MaxPool2d(2),                               # -> (64,8,8)
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),                                  # -> 4096
            nn.Linear(64 * 8 * 8, 128),
            nn.ReLU(),
            nn.Linear(128, 10),                            # -> 10 class scores
        )

    def forward(self, x):
        x = self.features(x)
        return self.classifier(x)

# --- block 2 ---
import torch
from torch import optim

# The chapter builds this from CIFAR-10 via torchvision; it is a dataset
# handle you supply, so it is stubbed here rather than invented.
# TODO: see https://books.vizuara.ai/read/ml-dl-mastery/build-your-own-cnn

device = "cuda" if torch.cuda.is_available() else "cpu"
model = SmallCNN().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(10):
    model.train()
    for images, labels in train_loader:               # each batch: (64,3,32,32), (64,)
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()                          # clear last step's gradients
        logits = model(images)                         # forward: -> (64,10)
        loss = criterion(logits, labels)               # cross-entropy
        loss.backward()                                # backprop: fill .grad on every weight
        optimizer.step()                               # Adam updates the weights
