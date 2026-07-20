"""
Computer Vision Bootcamp
Chapter 5: Reading Images and Video
Section: OpenCV and Classical Image Processing

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/reading-images-and-video

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import cv2

img = cv2.imread("cat.jpg")
print(type(img), img.shape, img.dtype)
# <class 'numpy.ndarray'> (720, 1280, 3) uint8

# --- block 2 ---
import matplotlib.pyplot as plt

img = cv2.imread("cat.jpg")               # BGR
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # now RGB for anything non-OpenCV
plt.imshow(img_rgb)                        # colors correct

# --- block 3 ---
cap = cv2.VideoCapture(0)        # 0 = default webcam; or a path: "clip.mp4"

while True:
    ret, frame = cap.read()      # ret: did we get a frame? frame: the array
    if not ret:
        break                    # webcam failed, or file ended
    cv2.imshow("live", frame)    # frame is BGR — imshow is happy
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break                    # quit when the user presses 'q'

cap.release()                    # let go of the camera
cv2.destroyAllWindows()

# --- block 4 ---
cap = cv2.VideoCapture("clip.mp4")
w   = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 1280
h   = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))   # 720
fps = cap.get(cv2.CAP_PROP_FPS)                 # 30.0
n   = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))    # 900  (~30 s clip)

# --- block 5 ---
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # <- your processing goes here
    cv2.imshow("gray feed", gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
