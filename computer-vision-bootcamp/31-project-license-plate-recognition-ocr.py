"""
Computer Vision Bootcamp
Chapter 31: Project: License Plate Recognition with OCR
Section: Real-Time Detection with YOLO

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/project-license-plate-recognition-ocr

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import cv2

# plate = the YOLO crop (BGR)
gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)

# Otsu picks the cutoff automatically from the pixel histogram
_, binary = cv2.threshold(
    gray, 0, 255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)
# binary is now pure 0/255: black characters on white

# --- block 2 ---
import re

PLATE_RE = re.compile(r"^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$")

def clean(ocr_fragments):
    raw = "".join(ocr_fragments).upper().replace(" ", "")
    return raw if PLATE_RE.match(raw) else None

# --- block 3 ---
from collections import Counter

# reads_per_car[track_id] = ["MH12DE1433", "MH12OE1433", ...]
def vote(reads):
    if not reads:
        return None
    winner, count = Counter(reads).most_common(1)[0]
    return winner   # optionally require count >= 3 for confidence
