"""
Transformers for Vision & Multimodal LLMs
Chapter 15: Training ViT and Its Data Hunger
Section: The Vision Transformer

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/training-vit-and-data-hunger

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# The ViT recipe that actually works: pretrain on huge data, fine-tune on your task.
import timm

# 1. DON'T do this from scratch on a small dataset — it underperforms a CNN.
# model = VisionTransformer(...)  # random init, train on ImageNet-1k -> loses

# 2. DO this: load weights already pretrained on huge data (ImageNet-21k / JFT-scale),
#    then fine-tune on your small target dataset.
model = timm.create_model(
    "vit_base_patch16_224.augreg_in21k",  # pretrained on ImageNet-21k (~14M imgs)
    pretrained=True,
    num_classes=37,                        # e.g. your 37-class pet dataset
)
# now fine-tune `model` on your few thousand images — this transfers and wins.
