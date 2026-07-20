"""
NLP & Computer Vision Mastery
Chapter 34: YOLO: You Only Look Once
Section: YOLO and Building Real Projects

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/yolo-you-only-look-once

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 (COMMENTED OUT) ---
# NOTE: this block is prose in the book, not runnable code.
# It is a pseudo-code sketch of the YOLO decode pipeline. Every name in it is
# undefined: `raw_pred`, `box_confidence` and `class_probs` are described only
# in a comment, and `decode_xywh` / `non_max_suppression` are named as steps
# but are never given anywhere in the book.
# raw_pred: (7, 7, 30) from one forward pass
# 1. per box, a class-specific score = box confidence × class prob
# scores = box_confidence[..., None] * class_probs   # (7, 7, B, C)
#
# 2. keep only boxes above a threshold, then Non-Max Suppression
# keep = scores.max(axis=-1) > 0.25                   # drop low-confidence cells
# boxes = decode_xywh(raw_pred[keep])                 # cell-relative → image coords
# final = non_max_suppression(boxes, iou_thresh=0.5)  # collapse duplicates
