"""
NLP & Computer Vision Mastery
Chapter 32: U-Net: Encoder-Decoder Segmentation
Section: Object Detection and Segmentation

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/unet-encoder-decoder-segmentation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# First double-conv block: 3 -> 64 -> 64, using same padding
conv1 = (3 * 3 * 3   + 1) * 64   # = 28 * 64   = 1,792
conv2 = (3 * 3 * 64  + 1) * 64   # = 577 * 64  = 36,928
block1 = conv1 + conv2           # = 38,720 parameters
