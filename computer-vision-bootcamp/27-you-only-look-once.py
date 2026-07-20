"""
Computer Vision Bootcamp
Chapter 27: You Only Look Once
Section: Real-Time Detection with YOLO

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/you-only-look-once

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# raw: the (7, 7, 30) tensor from one forward pass
boxes = []
for cell in grid:                      # 49 cells
    for b in cell.boxes:               # B = 2 boxes per cell
        for cls in classes:            # C = 20 classes
            score = b.confidence * cell.class_prob[cls]   # class-specific score
            if score > 0.25:
                boxes.append((b.xywh, cls, score))

detections = non_max_suppression(boxes, iou_threshold=0.5)  # drop duplicates
