"""
Python for Data Science
Chapter 28: Hand Tracking with MediaPipe
Section: Project: Computer Vision with OpenCV & MediaPipe

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/hand-tracking-with-mediapipe

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw  = mp.solutions.drawing_utils

# Create the detector ONCE, outside the loop.
hands = mp_hands.Hands(
    max_num_hands=2,                 # detect up to two hands
    min_detection_confidence=0.5,    # how sure before it reports a hand
    min_tracking_confidence=0.5,     # how sure before it keeps tracking one
)

cap = cv2.VideoCapture(0)            # webcam index 0

while True:
    ret, frame = cap.read()          # frame is a NumPy array in BGR
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)   # BGR → RGB for MediaPipe
    results = hands.process(rgb)                    # run the model

    if results.multi_hand_landmarks:                # None if no hand found
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
            )

    cv2.imshow("Hand Tracking", frame)              # show the BGR frame
    if cv2.waitKey(1) & 0xFF == ord("q"):           # quit on 'q'
        break

cap.release()
cv2.destroyAllWindows()

# --- block 2 ---
h, w, _ = frame.shape                 # (height, width, channels)
for hand_landmarks in results.multi_hand_landmarks:
    tip = hand_landmarks.landmark[8]  # index fingertip
    px, py = int(tip.x * w), int(tip.y * h)   # normalized → pixels
    cv2.circle(frame, (px, py), 12, (0, 255, 0), -1)  # green dot
