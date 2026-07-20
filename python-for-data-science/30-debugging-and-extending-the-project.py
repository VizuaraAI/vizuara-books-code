"""
Python for Data Science
Chapter 30: Debugging and Extending the Project
Section: Project: Computer Vision with OpenCV & MediaPipe

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/debugging-and-extending-the-project

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- carried over from an earlier chapter (see context.py) ---
# `hands` is the MediaPipe detector built in chapter 28.
from context import hands

# --- block 1 ---
import cv2
cap = cv2.VideoCapture(0)     # 0 = the default camera
ret, frame = cap.read()       # ret = did we get a frame? frame = the pixels

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# ret, frame = cap.read()
# if not ret:
#     print("No frame — camera busy, wrong index, or permission denied.")
#     break

# --- block 3 ---
for i in range(4):
    test = cv2.VideoCapture(i)
    ok, _ = test.read()
    print(f"index {i}: {'works' if ok else 'nothing'}")
    test.release()

# --- block 4 ---
rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
results = hands.process(rgb)     # MediaPipe sees correct colors

# --- block 5 ---
tips    = [8, 12, 16, 20]      # index, middle, ring, pinky tips
knuckles = [6, 10, 14, 18]     # the joint just below each tip
lm = results.multi_hand_landmarks[0].landmark   # 21 landmarks, one hand

count = 0
for tip, knuckle in zip(tips, knuckles):
    if lm[tip].y < lm[knuckle].y:   # tip above knuckle → finger is up
        count += 1

# --- block 6 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# cv2.putText(frame, f"Fingers: {count}", (10, 40),
#             cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
# cv2.imshow("Hand", frame)
# if cv2.waitKey(1) & 0xFF == ord("q"):   # 'q' to quit cleanly
#     break
