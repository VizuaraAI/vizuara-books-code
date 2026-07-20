"""
Build a Vision Transformer (ViT) from Scratch
Chapter 29: Loss, Optimizer, and the Training Loop
Section: Training, Data, and Beyond

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/loss-optimizer-training-loop

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# loss = -log(p_correct) = -log(0.659) = 0.417

# --- block 2 ---
import torch, torch.nn as nn

criterion = nn.CrossEntropyLoss()
logits = model(images)          # (B, num_classes) — raw scores
loss   = criterion(logits, labels)   # labels: (B,) int64 class indices

# --- block 3 ---
optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=3e-4,          # a sane ViT starting point
    weight_decay=0.05,
    betas=(0.9, 0.999),
)

# --- block 4 ---
for epoch in range(num_epochs):
    model.train()
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()              # 1. clear last step's gradients
        logits = model(images)             # 2. forward: predict
        loss   = criterion(logits, labels) # 3. score the prediction
        loss.backward()                    # 4. backward: fill .grad
        optimizer.step()                   # 5. update the weights
        scheduler.step()                   # advance the lr schedule
