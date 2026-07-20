"""
Build a Diffusion Language Model from Scratch
Chapter 8: Diffusion for Image Generation
Section: The Diffusion Idea

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/diffusion-for-image-generation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

x = 0.80                      # the real pixel brightness
beta = 0.02                   # how much noise this step injects
for step in range(3):
    noise = np.random.randn() # a draw from a standard bell curve
    x = np.sqrt(1 - beta) * x + np.sqrt(beta) * noise
    print(round(x, 3))
