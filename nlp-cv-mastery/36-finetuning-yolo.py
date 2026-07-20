"""
NLP & Computer Vision Mastery
Chapter 36: Fine-tuning YOLO on Custom Data
Section: YOLO and Building Real Projects

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/finetuning-yolo

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from ultralytics import YOLO

model = YOLO("yolov8n.pt")          # load pretrained nano weights
model.train(
    data="helmet-dataset/data.yaml",
    epochs=50,
    imgsz=640,                       # images resized to 640×640
    batch=16,
)
metrics = model.val()                # evaluate on the val split
