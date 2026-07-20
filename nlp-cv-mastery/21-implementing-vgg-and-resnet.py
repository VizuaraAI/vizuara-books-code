"""
NLP & Computer Vision Mastery
Chapter 21: Implementing VGG and ResNet
Section: Modern CNN Architectures

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/implementing-vgg-and-resnet

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from tensorflow.keras.applications import VGG16
from tensorflow.keras import layers, models

base = VGG16(weights="imagenet",     # download pretrained conv backbone
             include_top=False,       # DROP the original 1000-class FC head
             input_shape=(224, 224, 3))
base.trainable = False               # FREEZE the backbone

model = models.Sequential([
    base,
    layers.GlobalAveragePooling2D(),  # collapse feature map to one vector
    layers.Dense(5, activation="softmax")  # our fresh 5-flower head
])

# --- block 2 ---
import torchvision.models as models

def count_params(model):
    total = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    return total, trainable

vgg = models.vgg16(weights="IMAGENET1K_V1")     # full net, with FC head
res = models.resnet50(weights="IMAGENET1K_V2")

print("VGG16   ", count_params(vgg))   # ~ (138_357_544, 138_357_544)
print("ResNet50", count_params(res))   # ~ ( 25_557_032,  25_557_032)
