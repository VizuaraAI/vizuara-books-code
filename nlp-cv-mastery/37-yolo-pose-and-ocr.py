"""
NLP & Computer Vision Mastery
Chapter 37: YOLO with Pose Estimation and OCR
Section: YOLO and Building Real Projects

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/yolo-pose-and-ocr

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- context (added to make this file runnable) ---
# The fall-detection rule applied to the 33 pose landmarks. The chapter
# describes the idea but leaves the geometry to you; chapter 39's capstone
# builds on it.
# TODO: supply your own predicate, taking the landmark list and returning bool.
# See https://books.vizuara.ai/read/nlp-cv-mastery/capstone-fall-detection
is_fallen = None

# --- block 1 ---
import cv2, mediapipe as mp

pose = mp.solutions.pose.Pose()

def landmarks_for_crop(crop_bgr):
    # MediaPipe wants RGB; OpenCV hands you BGR
    rgb = cv2.cvtColor(crop_bgr, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb)
    if not result.pose_landmarks:
        return None
    # 33 landmarks, each with normalized x, y in [0, 1]
    return [(lm.x, lm.y) for lm in result.pose_landmarks.landmark]

# --- block 2 ---
import easyocr

reader = easyocr.Reader(['en'])   # load the English model once, up top

def read_text(crop_bgr):
    rgb = cv2.cvtColor(crop_bgr, cv2.COLOR_BGR2RGB)
    results = reader.readtext(rgb)
    # keep only confident reads
    return [text for (_box, text, conf) in results if conf > 0.5]

# --- block 3 ---
from ultralytics import YOLO
model = YOLO("yolov8n.pt")          # the nano detector

cap = cv2.VideoCapture(0)
while True:
    ok, frame = cap.read()
    if not ok:
        break
    for box in model(frame)[0].boxes:          # YOLO: one pass, many boxes
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        crop = frame[y1:y2, x1:x2]             # region of interest
        cls  = model.names[int(box.cls)]
        if cls == "person":
            pts = landmarks_for_crop(crop)     # → 33 joints or None
            if pts and is_fallen(pts):
                cv2.putText(frame, "FALL", (x1, y1-10), 0, 1, (0,0,255), 2)
        elif cls in ("sign", "license_plate"):
            for text in read_text(crop):       # → strings
                cv2.putText(frame, text, (x1, y1-10), 0, 1, (0,255,0), 2)
    cv2.imshow("aware", frame)
    if cv2.waitKey(1) == ord("q"):
        break
