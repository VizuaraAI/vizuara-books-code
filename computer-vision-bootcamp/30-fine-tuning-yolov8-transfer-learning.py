"""
Computer Vision Bootcamp
Chapter 30: Fine-Tuning YOLOv8 with Transfer Learning
Section: Real-Time Detection with YOLO

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/fine-tuning-yolov8-transfer-learning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from ultralytics import YOLO

model = YOLO("yolov8n.pt")          # start from COCO-pretrained weights

model.train(
    data="data.yaml",
    epochs=50,                      # passes over the training set
    imgsz=640,                      # images resized to 640×640
    batch=16,                       # images per gradient step
)

# --- block 2 ---
from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")   # your fine-tuned model

results = model("test_car.jpg")[0]

for box in results.boxes:
    x1, y1, x2, y2 = box.xyxy[0]           # corner coords, back in pixels
    cls_id = int(box.cls[0])               # 0
    conf   = float(box.conf[0])            # e.g. 0.91
    print(model.names[cls_id], conf)       # -> license_plate 0.91
