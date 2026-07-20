"""
Convolutional Neural Networks Fundamentals
Chapter 32: Evaluating and Interpreting Results
Section: Project: Brain Tumor Classifier

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/project-evaluating-the-model

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch

# --- block 1 ---
model.eval()                 # switch BatchNorm/Dropout to inference mode
correct, total = 0, 0
with torch.no_grad():        # don't build the autograd graph — we're not training
    for images, labels in test_loader:
        logits = model(images)              # shape (batch, 2): scores for [no_tumor, tumor]
        preds  = logits.argmax(dim=1)       # pick the higher-scoring class
        correct += (preds == labels).sum().item()
        total   += labels.size(0)

accuracy = correct / total
print(f"test accuracy: {accuracy:.1%}")     # e.g. 0.905 -> "90.5%"

# --- block 2 ---
probs = torch.softmax(logits, dim=1)[:, 1]   # P(tumor) for each scan, a number in [0, 1]
preds = (probs > 0.30).long()                # flag at 0.30 instead of the default 0.50
