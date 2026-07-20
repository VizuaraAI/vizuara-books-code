"""
Build a Vision Transformer (ViT) from Scratch
Chapter 30: Training ViT on a Small Dataset
Section: Training, Data, and Beyond

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/training-on-a-small-dataset

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch
import torch.nn as nn

# --- block 1 ---
model = ViT(img_size=32, patch_size=4, in_channels=3, num_classes=10,
            embed_dim=192, depth=6, num_heads=3, mlp_dim=768).to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4, weight_decay=0.05)

for epoch in range(num_epochs):
    model.train()
    for images, labels in train_loader:            # images: (B, 3, 32, 32)
        images, labels = images.to(device), labels.to(device)
        logits = model(images)                     # (B, 10)
        loss = criterion(logits, labels)           # a single scalar
        optimizer.zero_grad()
        loss.backward()                            # fill .grad on every parameter
        optimizer.step()                           # AdamW nudges the weights
