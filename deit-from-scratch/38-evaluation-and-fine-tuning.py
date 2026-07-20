"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 38: Evaluation and Fine-Tuning
Section: Training DeiT

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/evaluation-and-fine-tuning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

@torch.no_grad()                       # no autograd graph -> big batches, fast
def evaluate(model, loader, device):
    model.eval()                       # drop-path & dropout OFF
    correct, total = 0, 0
    for images, targets in loader:
        images, targets = images.to(device), targets.to(device)
        logits = model(images)         # inference branch fuses the two heads
        preds  = logits.argmax(dim=1)  # (B,) predicted class per image
        correct += (preds == targets).sum().item()
        total   += targets.size(0)
    return 100.0 * correct / total     # top-1 in percent

# --- block 2 ---
import torch
import torch.nn.functional as F

def interpolate_pos_embed(pos_embed, old_grid=14, new_grid=24, num_special=2):
    # pos_embed: (1, num_special + old_grid**2, D)   e.g. (1, 198, D)
    D = pos_embed.shape[-1]
    special = pos_embed[:, :num_special]             # (1, 2, D)  CLS + distill — untouched
    patches = pos_embed[:, num_special:]             # (1, 196, D) the spatial grid

    patches = patches.reshape(1, old_grid, old_grid, D)   # (1, 14, 14, D)
    patches = patches.permute(0, 3, 1, 2)                 # (1, D, 14, 14) -> NCHW for interp
    patches = F.interpolate(patches, size=(new_grid, new_grid),
                            mode='bicubic', align_corners=False)   # (1, D, 24, 24)
    patches = patches.permute(0, 2, 3, 1).reshape(1, new_grid * new_grid, D)  # (1, 576, D)

    return torch.cat([special, patches], dim=1)      # (1, 2 + 576, D) = (1, 578, D)
