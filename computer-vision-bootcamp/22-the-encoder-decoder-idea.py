"""
Computer Vision Bootcamp
Chapter 22: The Encoder-Decoder Idea
Section: Semantic Segmentation with U-Net

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/the-encoder-decoder-idea

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch.nn as nn

class TinyEncoderDecoder(nn.Module):
    def __init__(self, in_ch=1, num_classes=4):
        super().__init__()
        # ENCODER: halve space (pool), grow channels
        self.enc = nn.Sequential(
            nn.Conv2d(in_ch, 64, 3, padding=1), nn.ReLU(),
            nn.MaxPool2d(2),                              # 256 -> 128
            nn.Conv2d(64, 128, 3, padding=1), nn.ReLU(),
            nn.MaxPool2d(2),                              # 128 -> 64
        )
        # DECODER: grow space (transposed conv), shrink channels
        self.dec = nn.Sequential(
            nn.ConvTranspose2d(128, 64, 2, stride=2), nn.ReLU(),   # 64 -> 128
            nn.ConvTranspose2d(64, 32, 2, stride=2),  nn.ReLU(),   # 128 -> 256
            nn.Conv2d(32, num_classes, 1),           # 1x1 conv -> per-pixel class scores
        )

    def forward(self, x):
        z = self.enc(x)      # (B, 128, 64, 64)  <- the bottleneck
        return self.dec(z)   # (B, num_classes, 256, 256)
