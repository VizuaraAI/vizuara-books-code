"""
NLP & Computer Vision Mastery
Chapter 26: Real-Time Detection and Tracking with YOLOv8
Section: OpenCV and Real-Time Vision

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/opencv-yolov8-detection-tracking

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import cv2

cap = cv2.VideoCapture(0)          # 0 = default webcam; or a file path / RTSP URL
while cap.isOpened():
    ok, frame = cap.read()          # frame: (H, W, 3) uint8, in BGR order
    if not ok:
        break
    cv2.imshow("live", frame)       # draw the frame in a window
    if cv2.waitKey(1) == ord("q"):  # 1 ms wait; quit on 'q'
        break
cap.release()
cv2.destroyAllWindows()

# --- block 2 ---
from ultralytics import YOLO

model = YOLO("yolov8n.pt")          # downloads the checkpoint on first run
results = model(frame)              # runs detection on one BGR frame
boxes = results[0].boxes            # xyxy coords, confidences, class ids

# --- block 3 ---
seg = YOLO("yolov8n-seg.pt")
results = seg(frame)
masks = results[0].masks          # per-object binary masks (polygons + pixel maps)

# --- block 4 ---
results = model.track(frame, persist=True)   # persist=True: keep IDs across frames
for box in results[0].boxes:
    track_id = int(box.id)                    # stable integer id, e.g. 7

# --- block 5 ---
import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
        break
    results = model.track(frame, persist=True)   # detect + assign ids
    annotated = results[0].plot()                # boxes, labels, ids drawn for you
    cv2.imshow("YOLOv8 tracking", annotated)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
