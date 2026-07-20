"""
Computer Vision Bootcamp
Chapter 12: Project: Real-Time Object Counting on Video
Section: OpenCV Meets Deep Learning

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/project-real-time-object-counting

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from ultralytics import YOLO

model = YOLO("yolov8n.pt")               # 80 COCO classes, pretrained
results = model.track(frame, persist=True, classes=[2])  # class 2 = "car"
for box in results[0].boxes:
    track_id = int(box.id)                # the persistent name — the whole point
    x1, y1, x2, y2 = box.xyxy[0]          # pixel corners of the box

# --- block 2 ---
line_y = 300
counted = set()          # track IDs we've already tallied
prev_cy = {}             # last frame's center-y per track ID
count = 0

for box in results[0].boxes:
    tid = int(box.id)
    x1, y1, x2, y2 = box.xyxy[0]
    cy = (y1 + y2) / 2                       # center row of the box
    if tid in prev_cy and tid not in counted:
        was_above = prev_cy[tid] < line_y
        now_below = cy >= line_y
        if was_above and now_below:          # sign flipped downward
            count += 1
            counted.add(tid)                 # never count this ID again
    prev_cy[tid] = cy
