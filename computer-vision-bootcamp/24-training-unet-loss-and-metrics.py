"""
Computer Vision Bootcamp
Chapter 24: Training U-Net: Loss and Metrics
Section: Semantic Segmentation with U-Net

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/training-unet-loss-and-metrics

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def dice_loss(probs, target, smooth=1.0):
    # probs: (N, H, W) foreground probability in [0,1]; target: (N, H, W) in {0,1}
    inter = (probs * target).sum(dim=(1, 2))
    denom = probs.sum(dim=(1, 2)) + target.sum(dim=(1, 2))
    dice = (2 * inter + smooth) / (denom + smooth)
    return (1 - dice).mean()
