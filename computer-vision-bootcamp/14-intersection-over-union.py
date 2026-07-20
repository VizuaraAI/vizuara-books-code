"""
Computer Vision Bootcamp
Chapter 14: Intersection over Union (IoU)
Section: Object Detection: The R-CNN Family

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/intersection-over-union

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def iou(boxP, boxG):
    # each box is (x1, y1, x2, y2): top-left and bottom-right corners
    xL = max(boxP[0], boxG[0])
    yT = max(boxP[1], boxG[1])
    xR = min(boxP[2], boxG[2])
    yB = min(boxP[3], boxG[3])

    # clamp at 0 so non-overlapping boxes give intersection area 0
    inter_w = max(0, xR - xL)
    inter_h = max(0, yB - yT)
    inter   = inter_w * inter_h

    areaP = (boxP[2] - boxP[0]) * (boxP[3] - boxP[1])
    areaG = (boxG[2] - boxG[0]) * (boxG[3] - boxG[1])
    union = areaP + areaG - inter          # inclusion–exclusion

    return inter / union if union > 0 else 0.0

# our worked example
print(iou((80, 80, 180, 180), (50, 50, 150, 150)))   # -> 0.3245...
