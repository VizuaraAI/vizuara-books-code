"""
Convolutional Neural Networks Fundamentals
Chapter 33: Turning It Into an Application
Section: Project: Brain Tumor Classifier

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/project-deploying-the-application

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
import torch.nn as nn

# 1. Reconstruct the SAME architecture we trained.
CLASS_NAMES = ["glioma", "meningioma", "no_tumor", "pituitary"]

def build_model(num_classes=4):
    return nn.Sequential(
        nn.Conv2d(3,  16, kernel_size=3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
        nn.Conv2d(16, 32, kernel_size=3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
        nn.Conv2d(32, 64, kernel_size=3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
        nn.Flatten(),
        nn.Linear(64 * 16 * 16, 128), nn.ReLU(),
        nn.Linear(128, num_classes),
    )

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = build_model(num_classes=len(CLASS_NAMES)).to(device)
model.load_state_dict(torch.load("brain_cnn.pth", map_location=device))
model.eval()   # <-- do not forget this line

# --- block 2 ---
from PIL import Image
import torchvision.transforms as T

# The SAME transform pipeline used for training/validation images.
preprocess = T.Compose([
    T.Resize((128, 128)),
    T.Grayscale(num_output_channels=3),   # MRIs are grey; force 3 channels to match Conv2d(3,...)
    T.ToTensor(),                          # HWC uint8 [0,255] -> CHW float [0.0,1.0]
    T.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]),
])

def load_scan(path):
    img = Image.open(path).convert("RGB")      # handle grayscale OR color files uniformly
    tensor = preprocess(img)                    # shape (3, 128, 128)
    return tensor.unsqueeze(0)                  # add batch dim -> (1, 3, 128, 128)

# --- block 3 ---
import torch.nn.functional as F

def predict(path):
    x = load_scan(path).to(device)
    with torch.no_grad():                       # no gradients needed at inference — faster, less memory
        logits = model(x)                        # shape (1, 4)
        probs  = F.softmax(logits, dim=1)[0]     # shape (4,), sums to 1.0
    idx        = int(probs.argmax())
    label      = CLASS_NAMES[idx]
    confidence = float(probs[idx])
    return label, confidence, probs

label, conf, probs = predict("new_patient_scan.jpg")
print(f"Prediction: {label}  (confidence {conf:.1%})")
# Prediction: glioma  (confidence 94.2%)

# --- block 4 ---
def predict_with_guardrail(path, threshold=0.60):
    label, conf, probs = predict(path)
    if conf < threshold:
        return f"UNCERTAIN (top guess {label} at {conf:.1%}) — refer to a specialist"
    return f"{label} (confidence {conf:.1%})"

# --- block 5 ---
import gradio as gr

def classify(image):                       # Gradio hands us a PIL image directly
    x = preprocess(image.convert("RGB")).unsqueeze(0).to(device)
    with torch.no_grad():
        probs = F.softmax(model(x), dim=1)[0]
    return {CLASS_NAMES[i]: float(probs[i]) for i in range(len(CLASS_NAMES))}

gr.Interface(fn=classify, inputs=gr.Image(type="pil"),
             outputs=gr.Label(num_top_classes=4),
             title="Brain MRI Classifier (educational demo)").launch()
