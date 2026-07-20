"""
Build a NanoVLM from Scratch
Chapter 29: Synthetic Data for Training
Section: Building the NanoVLM

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/synthetic-data-for-training

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np
import torch

SHAPES = ["circle", "square", "triangle", "star"]
COLORS = {"red": (1, 0, 0), "green": (0, 1, 0),
          "blue": (0, 0, 1), "yellow": (1, 1, 0)}

def make_pair(shape, color, size=32):
    canvas = np.zeros((size, size, 3), dtype=np.float32)   # black background, HWC
    rgb = COLORS[color]
    cy, cx, r = size // 2, size // 2, size // 4
    yy, xx = np.ogrid[:size, :size]
    if shape == "circle":
        mask = (yy - cy) ** 2 + (xx - cx) ** 2 <= r ** 2
    elif shape == "square":
        mask = (np.abs(yy - cy) <= r) & (np.abs(xx - cx) <= r)
    else:                                                   # triangle, star, ...
        mask = (np.abs(xx - cx) + np.abs(yy - cy)) <= r     # diamond stand-in
    canvas[mask] = rgb                                      # paint the shape

    image = torch.from_numpy(canvas).permute(2, 0, 1)      # HWC -> (C, H, W)
    caption = f"a {color} {shape}"
    return image, caption

# --- block 2 ---
from torch.utils.data import Dataset

class ShapesDataset(Dataset):
    def __init__(self, n_per_class=64):
        self.items = []
        for shape in SHAPES:
            for color in COLORS:
                for _ in range(n_per_class):        # many variants per concept
                    self.items.append((shape, color))

    def __len__(self):
        return len(self.items)

    def __getitem__(self, idx):
        shape, color = self.items[idx]
        return make_pair(shape, color)              # (image tensor, caption string)

# --- block 3 (COMMENTED OUT - out-of-context fragment) ---
# NOTE: this block is prose in the book, not runnable code.
# These four lines are an edit the chapter suggests you make INSIDE make_pair
# (block 1), between the `cy, cx, r = ...` line and the mask computation, to
# add jitter. Shown on their own they have no enclosing function, so
# concatenating the chapter's blocks in document order lands them in
# ShapesDataset's class body where cy, cx, r, canvas and size do not exist.
#     cy += np.random.randint(-6, 7)                 # jitter center
#     cx += np.random.randint(-6, 7)
#     r  += np.random.randint(-3, 4)                 # jitter size
#     canvas += 0.05 * np.random.randn(size, size, 3).astype(np.float32)  # pixel noise
