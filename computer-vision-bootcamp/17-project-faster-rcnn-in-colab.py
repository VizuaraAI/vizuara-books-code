"""
Computer Vision Bootcamp
Chapter 17: Project: Faster R-CNN in Colab
Section: Object Detection: The R-CNN Family

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/project-faster-rcnn-in-colab

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn

device = "cuda" if torch.cuda.is_available() else "cpu"
model = fasterrcnn_resnet50_fpn(weights="DEFAULT")   # ResNet-50 + FPN, COCO-pretrained
model.eval().to(device)                              # eval mode is not optional — see below

# --- block 2 ---
from torchvision.io import read_image

img = read_image("street.jpg").float() / 255.0      # (3, H, W) in [0,1]
with torch.no_grad():
    preds = model([img.to(device)])                 # a list — one dict per image

# --- block 3 ---
keep = preds[0]["scores"] > 0.5
boxes  = preds[0]["boxes"][keep]
labels = preds[0]["labels"][keep]

# --- block 4 ---
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor

num_classes = 2   # 1 real class ("wheelchair") + 1 background class
in_features = model.roi_heads.box_predictor.cls_score.in_features
model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

# --- block 5 ---
target = {
    "boxes":  torch.tensor([[ 34,  50, 120, 210],     # wheelchair #1 corners (pixels)
                            [200, 60, 300, 240]]),     # wheelchair #2
    "labels": torch.tensor([1, 1]),                    # both are class 1 (not 0 = background)
}

# --- block 6 ---
model.train()
optimizer = torch.optim.SGD(model.parameters(), lr=0.005, momentum=0.9, weight_decay=5e-4)

for images, targets in data_loader:                     # from our collate_fn
    images  = [img.to(device) for img in images]
    targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

    loss_dict = model(images, targets)                  # TRAIN mode → returns losses
    loss = sum(loss_dict.values())                      # combine all heads' losses

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
