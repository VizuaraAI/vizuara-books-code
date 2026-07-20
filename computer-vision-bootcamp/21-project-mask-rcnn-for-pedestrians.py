"""
Computer Vision Bootcamp
Chapter 21: Project: Mask R-CNN for Pedestrians
Section: Instance Segmentation with Mask R-CNN

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/project-mask-rcnn-for-pedestrians

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch, cv2, numpy as np
from torchvision.models.detection import maskrcnn_resnet50_fpn

model = maskrcnn_resnet50_fpn(weights="DEFAULT")
model.eval()                              # inference mode — not optional

frame = cv2.imread("street.jpg")          # BGR, uint8, shape (H, W, 3)
rgb   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
tensor = torch.from_numpy(rgb).permute(2, 0, 1).float() / 255.0   # (3, H, W), [0,1]

with torch.no_grad():
    out = model([tensor])[0]              # a dict for image 0

# --- block 2 ---
PERSON, CONF, MASK_T = 1, 0.7, 0.5
colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0)]   # BGR, one per instance

overlay = frame.copy()
k = 0
for i in range(len(out["scores"])):
    if out["labels"][i] != PERSON or out["scores"][i] < CONF:
        continue
    m = out["masks"][i, 0].numpy() > MASK_T          # (H, W) bool stencil
    color = colors[k % len(colors)]
    overlay[m] = color                                # paint those pixels
    x1, y1, _, _ = out["boxes"][i].int().tolist()
    label = f"person {out['scores'][i]:.2f}"
    cv2.putText(overlay, label, (x1, y1 - 6),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
    k += 1

frame = cv2.addWeighted(overlay, 0.5, frame, 0.5, 0)   # 50% transparent blend

# --- block 3 ---
cap = cv2.VideoCapture("pedestrians.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
w   = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h   = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter("out.mp4",
            cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = segment_people(frame, model)     # the block from above
    writer.write(frame)

cap.release(); writer.release()
