"""
Computer Vision Bootcamp
Chapter 37: Capstone: Ship Your Own Vision System
Section: Putting It All Together

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/capstone-ship-your-own-vision-system

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")               # 80 COCO classes, no training needed
frame = cv2.imread("lot.jpg")            # BGR by default — remember that
results = model(frame)                    # ONE forward pass = all boxes

cars = [b for b in results[0].boxes if model.names[int(b.cls)] == "car"]
print(f"cars in lot: {len(cars)}")

# --- block 2 ---
from collections import deque
import statistics, cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)          # 0 = default webcam / camera feed
window = deque(maxlen=5)           # last 5 counts for the vote

i = 0
while True:
    ret, frame = cap.read()
    if not ret:                    # dropped/garbage frame — skip, don't crash
        continue
    if i % 60 == 0:                # ~1 detection every 2s at 30 FPS
        r = model(frame, verbose=False)[0]
        n = sum(model.names[int(b.cls)] == "car" for b in r.boxes)
        window.append(n)
    stable = statistics.median(window) if window else 0
    i += 1

# --- block 3 ---
import streamlit as st
from ultralytics import YOLO
import numpy as np, cv2

@st.cache_resource                 # load the model ONCE, not per click
def load(): return YOLO("yolov8n.pt")

st.title("Parking-Lot Occupancy Counter")
f = st.file_uploader("Upload a lot photo", type=["jpg", "png"])
if f:
    img = cv2.imdecode(np.frombuffer(f.read(), np.uint8), cv2.IMREAD_COLOR)
    r = load()(img)[0]
    n = sum(load().names[int(b.cls)] == "car" for b in r.boxes)
    st.image(r.plot()[:, :, ::-1], caption=f"{n} cars detected")  # BGR→RGB
