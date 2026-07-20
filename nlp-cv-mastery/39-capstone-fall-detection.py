"""
NLP & Computer Vision Mastery
Chapter 39: Capstone: Building a Detection App with Roboflow
Section: YOLO and Building Real Projects

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/capstone-fall-detection

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from ultralytics import YOLO

model = YOLO("yolov8n.pt")           # pretrained nano, class 0 = person
model.train(
    data="hallway-person/data.yaml",
    epochs=50,
    imgsz=640,
)

# --- block 2 ---
prev_y = None

def is_fall(box, prev_y, fps=30):
    x, y, w, h = box
    aspect = w / h
    y_center = y + h / 2
    dropping_fast = (
        prev_y is not None
        and (y_center - prev_y) > 25   # pixels dropped since last frame
    )
    return aspect > 1.0 and dropping_fast, y_center

# --- block 3 ---
import cv2
from ultralytics import YOLO

model = YOLO("hallway-person/best.pt")   # our fine-tuned weights
cap = cv2.VideoCapture(0)                # 0 = webcam, or a video file path
prev_y = None

while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
        break
    results = model(frame, classes=[0])  # class 0 = person only
    for box in results[0].boxes.xywh:    # each detected person
        fall, prev_y = is_fall(box.tolist(), prev_y)
        color = (0, 0, 255) if fall else (0, 255, 0)   # BGR: red vs green
        # ...draw the box + label "FALL!" on the frame in `color`...
    cv2.imshow("Fall Detection", frame)
    if cv2.waitKey(1) == ord("q"):
        break
