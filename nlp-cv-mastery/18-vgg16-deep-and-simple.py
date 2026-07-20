"""
NLP & Computer Vision Mastery
Chapter 18: VGG16: Deep and Simple
Section: Modern CNN Architectures

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/vgg16-deep-and-simple

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch.nn as nn

# VGG16 config: numbers = conv out-channels, 'M' = 2x2 maxpool
cfg = [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 'M',
       512, 512, 512, 'M', 512, 512, 512, 'M']

def make_features(cfg, in_channels=3):
    layers = []
    for v in cfg:
        if v == 'M':
            layers += [nn.MaxPool2d(kernel_size=2, stride=2)]
        else:
            layers += [nn.Conv2d(in_channels, v, kernel_size=3, padding=1),
                       nn.ReLU(inplace=True)]
            in_channels = v
    return nn.Sequential(*layers)

classifier = nn.Sequential(
    nn.Linear(512 * 7 * 7, 4096), nn.ReLU(True), nn.Dropout(),
    nn.Linear(4096, 4096),        nn.ReLU(True), nn.Dropout(),
    nn.Linear(4096, 1000),
)
