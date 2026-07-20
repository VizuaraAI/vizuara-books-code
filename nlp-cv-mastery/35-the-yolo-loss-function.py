"""
NLP & Computer Vision Mastery
Chapter 35: The YOLO Loss Function
Section: YOLO and Building Real Projects

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/the-yolo-loss-function

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import math

# both boxes are 10 px too wide
small_true, small_pred = 20, 30      # a 20px box, predicted 30px  -> +50%
big_true,   big_pred   = 400, 410    # a 400px box, predicted 410px -> +2.5%

# plain squared error on width: identical penalty, blind to scale
plain_small = (small_pred - small_true) ** 2          # 100
plain_big   = (big_pred   - big_true)   ** 2          # 100

# square-root squared error: small box now hurts far more
sqrt_small = (math.sqrt(small_pred) - math.sqrt(small_true)) ** 2   # ~0.60
sqrt_big   = (math.sqrt(big_pred)   - math.sqrt(big_true))   ** 2   # ~0.062
