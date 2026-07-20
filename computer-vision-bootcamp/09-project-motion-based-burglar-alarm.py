"""
Computer Vision Bootcamp
Chapter 9: Project: A Motion-Based Burglar Alarm
Section: OpenCV and Classical Image Processing

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/project-motion-based-burglar-alarm

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import cv2

cap = cv2.VideoCapture(0)          # 0 = default webcam
ret, first = cap.read()
prev_gray = cv2.GaussianBlur(
    cv2.cvtColor(first, cv2.COLOR_BGR2GRAY), (21, 21), 0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 1. preprocess: gray -> blur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # 2. difference from the previous frame, then threshold
    diff = cv2.absdiff(prev_gray, gray)
    _, mask = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    # 3. find moving blobs
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion = False
    for c in contours:
        if cv2.contourArea(c) < 500:      # ignore specks
            continue
        motion = True
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if motion:
        cv2.putText(frame, "MOTION", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        print("ALARM: motion detected")

    cv2.imshow("alarm", frame)
    prev_gray = gray                       # today's frame is tomorrow's reference
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
