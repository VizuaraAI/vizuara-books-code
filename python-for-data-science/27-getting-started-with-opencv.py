"""
Python for Data Science
Chapter 27: Getting Started with OpenCV
Section: Project: Computer Vision with OpenCV & MediaPipe

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/getting-started-with-opencv

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import cv2   # yes — the package is "opencv-python", the module is "cv2"

# --- block 2 ---
import cv2

img = cv2.imread("cat.jpg")
print(type(img))    # <class 'numpy.ndarray'>
print(img.shape)    # (426, 640, 3)

# --- block 3 ---
img = cv2.imread("cat.jpg")
if img is None:
    raise FileNotFoundError("cv2.imread returned None — check the path")

# --- block 4 ---
import matplotlib.pyplot as plt

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # BGR -> RGB
plt.imshow(img_rgb)   # now the colours are correct
plt.show()

# --- block 5 ---
cv2.imshow("Cat", img)   # BGR is correct HERE — imshow expects BGR
cv2.waitKey(0)           # 0 = wait forever until a key is pressed
cv2.destroyAllWindows()  # clean up the window

# --- block 6 ---
resized = cv2.resize(img, (320, 240))   # (width, height) — width FIRST
print(resized.shape)                     # (240, 320, 3)

# --- block 7 ---
gray = cv2.imread("cat.jpg", cv2.IMREAD_GRAYSCALE)
print(gray.shape)    # (426, 640)  — no third number!

# --- block 8 ---
cv2.imwrite("cat_small.png", resized)   # .png -> saved as PNG

# --- block 9 ---
cap = cv2.VideoCapture(0)   # 0 = default webcam

while True:
    ret, frame = cap.read()      # ret: did we get a frame? frame: the BGR image
    if not ret:
        break                    # camera unplugged or stream ended
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):   # press q to quit
        break

cap.release()                # ALWAYS free the camera
cv2.destroyAllWindows()
