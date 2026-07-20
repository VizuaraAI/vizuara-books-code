"""
NLP & Computer Vision Mastery
Chapter 15: What Is Transfer Learning?
Section: Generalization and Transfer Learning

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/what-is-transfer-learning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from tensorflow.keras.applications import VGG16
from tensorflow.keras import layers, models

# 1. Pretrained backbone, ImageNet weights, no classifier head
base = VGG16(weights="imagenet", include_top=False,
             input_shape=(224, 224, 3))

# 2. Freeze it — its 138M weights will not update
base.trainable = False

# 3. Attach a fresh head sized for 5 flower classes
model = models.Sequential([
    base,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation="relu"),
    layers.Dense(5, activation="softmax"),
])
