"""
Computer Vision Bootcamp
Chapter 23: U-Net Architecture and Skip Connections
Section: Semantic Segmentation with U-Net

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/unet-architecture-and-skip-connections

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

class UpBlock(nn.Module):
    def __init__(self, in_ch, skip_ch, out_ch):
        super().__init__()
        # double the spatial size, halve the decoder channels
        self.up = nn.ConvTranspose2d(in_ch, in_ch // 2, kernel_size=2, stride=2)
        # after concat the channel count is (in_ch//2 + skip_ch)
        self.conv = nn.Sequential(
            nn.Conv2d(in_ch // 2 + skip_ch, out_ch, 3, padding=1), nn.ReLU(),
            nn.Conv2d(out_ch, out_ch, 3, padding=1), nn.ReLU(),
        )

    def forward(self, x, skip):
        x = self.up(x)                      # e.g. 32×32×512  ->  64×64×256
        x = torch.cat([skip, x], dim=1)     # concat the encoder copy on the channel axis
        return self.conv(x)                 # fuse "where" + "what", squeeze channels back down
