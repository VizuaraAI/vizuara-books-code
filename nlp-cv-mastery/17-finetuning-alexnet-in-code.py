"""
NLP & Computer Vision Mastery
Chapter 17: Fine-tuning AlexNet in Code
Section: Generalization and Transfer Learning

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/finetuning-alexnet-in-code

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- context (added to make this file runnable) ---
# Block 3 iterates a DataLoader the chapter assumes you have already built.
from context import train_loader

# --- block 1 ---
import torch.nn as nn
from torchvision import models

# 1. Load AlexNet with its pretrained ImageNet weights
alexnet = models.alexnet(weights=models.AlexNet_Weights.IMAGENET1K_V1)

# 2. FREEZE everything — no gradients, no updates
for param in alexnet.parameters():
    param.requires_grad = False

# 3. Replace the head: the last layer is classifier[6], a Linear(4096 -> 1000)
alexnet.classifier[6] = nn.Linear(4096, 5)   # 5 flower classes, requires_grad=True by default

# --- block 2 ---
import torch

criterion = nn.CrossEntropyLoss()   # softmax + categorical cross-entropy, fused

# Give the optimizer ONLY the parameters that still require grad — the new head
trainable = [p for p in alexnet.parameters() if p.requires_grad]
optimizer = torch.optim.Adam(trainable, lr=1e-3)

# --- block 3 ---
for epoch in range(30):
    alexnet.train()
    for images, labels in train_loader:      # batches of (224×224×3 images, class ids 0–4)
        optimizer.zero_grad()                # clear last batch's gradients
        logits = alexnet(images)             # forward: (batch, 5) raw scores
        loss = criterion(logits, labels)     # softmax + cross-entropy
        loss.backward()                      # backward: gradients ONLY reach the head
        optimizer.step()                     # update the 20,485 head weights
