"""
Convolutional Neural Networks Fundamentals
Chapter 31: Training the Model
Section: Project: Brain Tumor Classifier

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/project-training-the-model

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

model     = BrainTumorCNN()                                  # from the previous chapter
criterion = nn.CrossEntropyLoss()                            # softmax + log, fused; wants LOGITS
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)   # η = 0.001, adaptive per-weight

# --- block 2 ---
num_epochs = 10

for epoch in range(num_epochs):
    model.train()                                # tell layers we are training
    running_loss, correct, total = 0.0, 0, 0

    for images, labels in train_loader:          # one mini-batch at a time
        optimizer.zero_grad()                    # 5 (moved to the top): wipe old grads
        logits = model(images)                   # 1. forward → (32, num_classes)
        loss   = criterion(logits, labels)       # 2. score against the truth
        loss.backward()                          # 3. fill every .grad via backprop
        optimizer.step()                         # 4. w ← w − η·∇L for every weight

        running_loss += loss.item() * images.size(0)
        preds    = logits.argmax(dim=1)          # predicted class = biggest logit
        correct += (preds == labels).sum().item()
        total   += labels.size(0)

    epoch_loss = running_loss / total
    epoch_acc  = correct / total
    print(f"epoch {epoch+1:2d}  loss {epoch_loss:.4f}  acc {epoch_acc:.3f}")
