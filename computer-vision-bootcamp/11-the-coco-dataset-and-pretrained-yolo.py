"""
Computer Vision Bootcamp
Chapter 11: The COCO Dataset and Pretrained YOLO
Section: OpenCV Meets Deep Learning

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/the-coco-dataset-and-pretrained-yolo

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from ultralytics import YOLO

model = YOLO("yolov8n.pt")   # downloads the ~6 MB checkpoint on first call, then caches it

# --- block 2 ---
import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()          # frame: (480, 640, 3), BGR, uint8
    if not ret:
        break

    results = model(frame)[0]        # run detection on ONE frame

    for box in results.boxes:
        x1, y1, x2, y2 = box.xyxy[0]                 # corner coords, floats
        cls_id = int(box.cls[0])                     # e.g. 16
        conf   = float(box.conf[0])                  # e.g. 0.87
        label  = f"{model.names[cls_id]} {conf:.2f}" # -> "dog 0.87"

        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(frame, label, (int(x1), int(y1) - 8),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("YOLOv8", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
