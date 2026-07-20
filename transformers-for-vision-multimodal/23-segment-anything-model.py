"""
Transformers for Vision & Multimodal LLMs
Chapter 23: The Segment Anything Model (SAM)
Section: Hierarchical & Dense Vision Transformers

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/segment-anything-model

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from segment_anything import sam_model_registry, SamPredictor
import numpy as np

sam = sam_model_registry["vit_h"](checkpoint="sam_vit_h.pth")
predictor = SamPredictor(sam)

predictor.set_image(image)          # runs the HEAVY encoder ONCE; caches 64×64×256 embedding

# now every prompt is cheap — no re-encoding
masks, scores, _ = predictor.predict(
    point_coords=np.array([[612, 340]]),   # one click at (x, y)
    point_labels=np.array([1]),            # 1 = foreground, 0 = background
    multimask_output=True,                 # return the 3 nested masks
)
best = masks[scores.argmax()]              # keep the most confident mask
