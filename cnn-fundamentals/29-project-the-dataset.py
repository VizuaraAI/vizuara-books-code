"""
Convolutional Neural Networks Fundamentals
Chapter 29: The Dataset and the Problem
Section: Project: Brain Tumor Classifier

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/project-the-dataset

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 1. The transform pipeline, applied to every image on load.
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),  # MRIs are grayscale → 1 channel
    transforms.Resize((128, 128)),                # every image ends 128×128
    transforms.ToTensor(),                        # HWC uint8 → CHW float in [0,1]
    transforms.Normalize(mean=[0.5], std=[0.5]),  # rescale [0,1] → [-1,1], centered
])

# 2. ImageFolder reads labels from subfolder names, applies the transform.
train_ds = datasets.ImageFolder("brain_mri/train", transform=transform)
val_ds   = datasets.ImageFolder("brain_mri/val",   transform=transform)

# 3. DataLoader batches and shuffles.
train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)
val_loader   = DataLoader(val_ds,   batch_size=32, shuffle=False)

print(train_ds.classes)          # ['no', 'yes']  → class 0, class 1
images, labels = next(iter(train_loader))
print(images.shape, labels.shape)  # torch.Size([32, 1, 128, 128]) torch.Size([32])
