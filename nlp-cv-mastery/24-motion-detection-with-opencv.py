"""
NLP & Computer Vision Mastery
Chapter 24: Motion Detection with OpenCV
Section: OpenCV and Real-Time Vision

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/motion-detection-with-opencv

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import cv2

cap = cv2.VideoCapture(0)          # 0 = default webcam
ret, prev = cap.read()
prev_gray = cv2.GaussianBlur(cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY), (21, 21), 0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.GaussianBlur(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), (21, 21), 0)

    diff   = cv2.absdiff(prev_gray, gray)              # step 1: subtract
    thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]   # step 2: threshold
    thresh = cv2.dilate(thresh, None, iterations=2)    # step 3: close gaps

    # step 4: find the moving blobs and box them
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv2.contourArea(c) < 500:      # ignore specks
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("motion", frame)
    prev_gray = gray                      # today's frame is tomorrow's "previous"
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
