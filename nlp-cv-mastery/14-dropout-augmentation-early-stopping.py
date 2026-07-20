"""
NLP & Computer Vision Mastery
Chapter 14: Dropout, Augmentation, and Early Stopping
Section: Generalization and Transfer Learning

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/dropout-augmentation-early-stopping

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch

# --- context (added to make this file runnable) ---
# Block 3's early-stopping loop trains and scores a model the chapter assumes
# you already have. (Block 1 builds a `classifier`, not a full `model`.)
from context import model, val_loader, train_one_epoch, evaluate

# --- block 1 ---
import torch.nn as nn

classifier = nn.Sequential(
    nn.Linear(2048, 512),
    nn.ReLU(),
    nn.Dropout(p=0.5),   # zero 50% of these 512 activations each training step
    nn.Linear(512, 5),   # 5 flower classes
)

# --- block 2 ---
from torchvision import transforms

train_tf = transforms.Compose([
    transforms.RandomResizedCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(15),
    transforms.ColorJitter(brightness=0.2, contrast=0.2),
    transforms.ToTensor(),
])

# validation: NO randomness — just resize + center crop
val_tf = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
])

# --- block 3 ---
best_val, patience, wait = float("inf"), 5, 0
for epoch in range(50):
    train_one_epoch(model)
    val = evaluate(model, val_loader)
    if val < best_val:
        best_val, wait = val, 0
        torch.save(model.state_dict(), "best.pt")   # checkpoint the best
    else:
        wait += 1
        if wait >= patience:
            break                                    # stop early
model.load_state_dict(torch.load("best.pt"))         # restore best weights
