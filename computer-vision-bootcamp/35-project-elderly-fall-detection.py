"""
Computer Vision Bootcamp
Chapter 35: Project: Elderly Fall Detection
Section: Data, Roboflow, and Shipping Apps

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/project-elderly-fall-detection

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from ultralytics import YOLO

model = YOLO("best.pt")            # our fine-tuned two-class detector
results = model(frame)            # frame is one BGR image from OpenCV

for box in results[0].boxes:
    cls  = int(box.cls[0])         # 0 = person_standing, 1 = person_fallen
    conf = float(box.conf[0])      # confidence in [0, 1]
    x1, y1, x2, y2 = box.xyxy[0]   # pixel corners of the box

# --- block 2 ---
FPS = 30
FALL_SECONDS = 2.0
FALL_THRESHOLD = int(FPS * FALL_SECONDS)   # 60 frames

fallen_count = 0        # consecutive-ish fallen frames
alerted = False         # have we already raised THIS fall?

def update(frame_is_fallen: bool) -> bool:
    global fallen_count, alerted
    if frame_is_fallen:
        fallen_count += 1
    else:
        fallen_count = max(0, fallen_count - 1)   # debounce: decay, don't reset

    if fallen_count >= FALL_THRESHOLD and not alerted:
        alerted = True
        return True        # fire the alert exactly once
    if fallen_count == 0:
        alerted = False    # person recovered → re-arm for next time
    return False

# --- block 3 ---
def frame_is_fallen(results, conf_floor=0.5) -> bool:
    for box in results[0].boxes:
        if int(box.cls[0]) == 1 and float(box.conf[0]) >= conf_floor:
            return True
    return False

# --- block 4 ---
import streamlit as st
import cv2
from ultralytics import YOLO

st.title("Elderly Fall Detection")
model = YOLO("best.pt")
video_slot  = st.empty()     # we repaint this each frame
alert_slot  = st.empty()     # stays empty until a fall

cap = cv2.VideoCapture(st.file_uploader("Upload a clip") or 0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    fell = update(frame_is_fallen(results))      # our temporal logic
    annotated = results[0].plot()                # YOLO draws the boxes for us

    rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)   # BGR→RGB for display!
    video_slot.image(rgb, channels="RGB")

    if fell:
        alert_slot.error("🔔 FALL DETECTED — person down > 2s")
