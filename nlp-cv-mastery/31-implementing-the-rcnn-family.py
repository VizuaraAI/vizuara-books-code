"""
NLP & Computer Vision Mastery
Chapter 31: Implementing the R-CNN Family
Section: Object Detection and Segmentation

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/implementing-the-rcnn-family

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added to make this file runnable) ---
# The chapter calls read_image() but the import line is not repeated in its
# own code blocks. This is torchvision's own loader.
from torchvision.io import read_image

# --- block 1 ---
import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.models.detection import FasterRCNN_ResNet50_FPN_Weights

weights = FasterRCNN_ResNet50_FPN_Weights.DEFAULT   # COCO-trained, 91 classes
model = fasterrcnn_resnet50_fpn(weights=weights)
model.eval()                                        # inference mode: no RPN sampling, no dropout

img = weights.transforms()(read_image("dog.jpg"))   # the model's OWN preprocessing
with torch.no_grad():
    out = model([img])[0]                            # list in, list out — take image 0

print(out.keys())   # dict_keys(['boxes', 'labels', 'scores'])

# --- block 2 ---
from torchvision.ops import nms

keep = out["scores"] >= 0.5                      # boolean mask
boxes, labels, scores = out["boxes"][keep], out["labels"][keep], out["scores"][keep]

keep = nms(boxes, scores, iou_threshold=0.5)     # returns indices to keep
boxes, labels, scores = boxes[keep], labels[keep], scores[keep]

# --- block 3 ---
from torchvision.models.detection import maskrcnn_resnet50_fpn, MaskRCNN_ResNet50_FPN_Weights

weights = MaskRCNN_ResNet50_FPN_Weights.DEFAULT
model = maskrcnn_resnet50_fpn(weights=weights).eval()
out = model([img])[0]
print(out.keys())   # dict_keys(['boxes', 'labels', 'scores', 'masks'])

# --- block 4 ---
binary_masks = out["masks"][keep] > 0.5   # (M, 1, H, W) of True/False, one crisp mask per kept object

# --- block 5 ---
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor

model = fasterrcnn_resnet50_fpn(weights="DEFAULT")   # COCO weights, kept
in_features = model.roi_heads.box_predictor.cls_score.in_features  # = 1024
model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes=4)  # 3 classes + background

# --- block 6 ---
COCO = weights.meta["categories"]            # id → human-readable name, e.g. COCO[18] == "dog"
for box, label, score in zip(boxes, labels, scores):
    x1, y1, x2, y2 = box.int().tolist()
    print(f"{COCO[label]:8s}  {score:.2f}  ({x1},{y1})→({x2},{y2})")
