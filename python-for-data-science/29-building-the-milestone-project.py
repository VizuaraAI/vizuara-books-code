"""
Python for Data Science
Chapter 29: Building the Milestone Project
Section: Project: Computer Vision with OpenCV & MediaPipe

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/building-the-milestone-project

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import cv2

cap = cv2.VideoCapture(0)          # 0 = default webcam
while True:
    ret, frame = cap.read()        # ret is False if the grab failed
    if not ret:
        break
    cv2.imshow("Finger Counter", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):  # 1 ms wait; q quits
        break
cap.release()
cv2.destroyAllWindows()

# --- block 2 ---
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1)   # track one hand, keep it simple

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)   # BGR → RGB, every frame
    result = hands.process(rgb)                     # the actual detection

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Finger Counter", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

# --- block 3 ---
def count_fingers(hand_landmarks):
    tips = [8, 12, 16, 20]     # index, middle, ring, pinky fingertips
    pips = [6, 10, 14, 18]     # the knuckle two joints below each tip
    lm = hand_landmarks.landmark
    count = 0
    for tip, pip in zip(tips, pips):
        if lm[tip].y < lm[pip].y:   # tip above knuckle → finger up
            count += 1
    return count

# --- block 4 ---
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers = count_fingers(hand_landmarks)
            cv2.putText(frame, f"Fingers: {fingers}", (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
