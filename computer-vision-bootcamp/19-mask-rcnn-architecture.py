"""
Computer Vision Bootcamp
Chapter 19: The Mask R-CNN Architecture
Section: Instance Segmentation with Mask R-CNN

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/mask-rcnn-architecture

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
from torchvision.models.detection import maskrcnn_resnet50_fpn

model = maskrcnn_resnet50_fpn(weights="DEFAULT")  # ResNet-50 + FPN backbone, 80 COCO classes
model.eval()

with torch.no_grad():
    outputs = model([image_tensor])   # image_tensor: (3, H, W), float in [0,1]

out = outputs[0]
out["boxes"]    # (N, 4)          one refined box per detection
out["labels"]   # (N,)           class id, 1..80
out["scores"]   # (N,)           detection confidence
out["masks"]    # (N, 1, H, W)   one full-size soft mask per detection, values in [0,1]
