"""
Build a Vision Transformer (ViT) from Scratch
Chapter 32: Fine-Tuning Pretrained ViTs
Section: Training, Data, and Beyond

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/fine-tuning-pretrained-vits

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch, torch.nn as nn

model = load_pretrained_vit_base()          # our ViT class, weights loaded
model.head = nn.Linear(768, num_classes=5)  # swap the head for our 5 classes

for p in model.parameters():                # optional: freeze the backbone
    p.requires_grad = False
for p in model.head.parameters():           # ...but train the new head
    p.requires_grad = True

# --- block 2 ---
import torch.nn.functional as F

def interpolate_pos_embed(pos_embed, old_grid, new_grid, D):
    # pos_embed: (1, 1 + old_grid**2, D). old_grid=14, new_grid=24.
    cls_pe   = pos_embed[:, :1]            # (1, 1, D) — the class-token slot
    patch_pe = pos_embed[:, 1:]            # (1, 196, D) — the 14x14 grid, flattened

    patch_pe = patch_pe.reshape(1, old_grid, old_grid, D).permute(0, 3, 1, 2)
    patch_pe = F.interpolate(patch_pe, size=(new_grid, new_grid),
                             mode="bicubic", align_corners=False)   # (1, D, 24, 24)
    patch_pe = patch_pe.permute(0, 2, 3, 1).reshape(1, new_grid * new_grid, D)

    return torch.cat([cls_pe, patch_pe], dim=1)   # (1, 577, D)
