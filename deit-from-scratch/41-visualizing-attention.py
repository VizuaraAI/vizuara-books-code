"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 41: Visualizing Attention
Section: Putting It Together

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/visualizing-attention

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch.nn.functional as F

# --- block 1 ---
# attn: (num_heads, 198, 198) from the last block, one image
cls_attn = attn[:, 0, 2:]          # CLS row, drop CLS+distill cols -> (heads, 196)
cls_attn = cls_attn.mean(dim=0)    # average the heads -> (196,)
grid = cls_attn.reshape(14, 14)    # the patch grid -> (14, 14)

heatmap = F.interpolate(           # upsample to the 224x224 image
    grid[None, None], size=(224, 224), mode="bilinear"
)[0, 0]
