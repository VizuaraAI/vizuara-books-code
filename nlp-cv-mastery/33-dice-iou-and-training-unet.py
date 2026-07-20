"""
NLP & Computer Vision Mastery
Chapter 33: DICE, IoU, and Training U-Net
Section: Object Detection and Segmentation

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/dice-iou-and-training-unet

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
from context import train_loader

# The U-Net architecture. Chapter 32 walks through its shape and counts its
# parameters, but the book never gives the class as a code block.
# TODO: supply your own U-Net module.
# See https://books.vizuara.ai/read/nlp-cv-mastery/unet-encoder-decoder-segmentation
UNet = None

# The pixel-wise binary cross-entropy term, applied to raw logits.
# TODO: supply your own, e.g. a loss object that takes (logits, targets).
# See https://books.vizuara.ai/read/nlp-cv-mastery/dice-iou-and-training-unet
bce = None

# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# IoU = |A ∩ B| / |A ∪ B|

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# DICE = 2·|A ∩ B| / (|A| + |B|)

# --- block 3 ---
def dice_loss(p, g, eps=1e-6):
    # p: predicted probabilities in [0,1], g: ground-truth {0,1}
    intersection = (p * g).sum()
    total = p.sum() + g.sum()
    dice = (2 * intersection + eps) / (total + eps)
    return 1 - dice          # loss: minimise 1 - DICE  ->  maximise DICE

# --- block 4 ---
model = UNet(in_channels=3, out_channels=1)      # RGB in, 1-channel mask out
opt   = torch.optim.Adam(model.parameters(), lr=1e-3)

for images, masks in train_loader:               # images (B,3,H,W), masks (B,1,H,W)
    logits = model(images)                        # raw scores, same H×W
    probs  = torch.sigmoid(logits)                # -> probabilities in [0,1]
    loss   = bce(logits, masks) + dice_loss(probs, masks)
    opt.zero_grad(); loss.backward(); opt.step()
