"""
NLP & Computer Vision Mastery
Chapter 23: Introduction to OpenCV
Section: OpenCV and Real-Time Vision

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/introduction-to-opencv

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import cv2

img = cv2.imread("flower.jpg")          # load from disk
print(type(img))                         # <class 'numpy.ndarray'>
print(img.shape)                         # (480, 640, 3)  -> H, W, channels
print(img.dtype)                         # uint8  -> values 0..255

# --- block 2 ---
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # BGR -> RGB for matplotlib / models

# --- block 3 ---
cv2.imshow("flower", img)     # opens a window titled "flower"
cv2.waitKey(0)                # wait for ANY key press, then continue
cv2.destroyAllWindows()       # close the window
cv2.imwrite("out.png", img)   # save the array back to a file

# --- block 4 ---
import cv2

cap = cv2.VideoCapture(0)                    # 0 = default webcam

while True:
    ret, frame = cap.read()                  # ret = did we get a frame?
    if not ret:                              # camera unplugged / stream ended
        break

    cv2.imshow("webcam", frame)              # show this one frame

    if cv2.waitKey(1) & 0xFF == ord("q"):    # 1 ms wait; quit on 'q'
        break

cap.release()                                # free the camera
cv2.destroyAllWindows()

# --- block 5 ---
# rectangle: image, top-left (x, y), bottom-right (x, y), color(BGR), thickness
cv2.rectangle(frame, (50, 40), (200, 180), (0, 255, 0), 2)     # green box

# circle: image, center (x, y), radius, color(BGR), thickness (-1 = filled)
cv2.circle(frame, (125, 110), 6, (0, 0, 255), -1)             # filled red dot

# text: image, string, bottom-left (x, y), font, scale, color(BGR), thickness
cv2.putText(frame, "rose 0.94", (50, 32),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

# --- block 6 ---
import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.rectangle(frame, (50, 40), (200, 180), (0, 255, 0), 2)
    cv2.putText(frame, "hello opencv", (50, 32),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("live", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
