"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 33: The Training Recipe
Section: Training DeiT

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/the-training-recipe

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from torch.optim import AdamW
from torch.optim.lr_scheduler import LinearLR, CosineAnnealingLR, SequentialLR

batch_size = 1024
peak_lr = 5e-4 * (batch_size / 512)          # = 1e-3 at batch 1024
epochs, warmup_epochs = 300, 5

optimizer = AdamW(model.parameters(), lr=peak_lr, weight_decay=0.05)

warmup = LinearLR(optimizer, start_factor=1e-3, total_iters=warmup_epochs)
cosine = CosineAnnealingLR(optimizer, T_max=epochs - warmup_epochs, eta_min=1e-5)
scheduler = SequentialLR(optimizer, [warmup, cosine], milestones=[warmup_epochs])
