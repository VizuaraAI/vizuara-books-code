"""
Computer Vision Bootcamp
Chapter 26: Project: Crack Detection and Hugging Face Hosting
Section: Semantic Segmentation with U-Net

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/project-crack-detection-and-hf-hosting

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import cv2, numpy as np, torch
from torch.utils.data import Dataset

class CrackDataset(Dataset):
    def __init__(self, img_paths, mask_paths, size=256):
        self.img_paths, self.mask_paths, self.size = img_paths, mask_paths, size

    def __len__(self):
        return len(self.img_paths)

    def __getitem__(self, i):
        img  = cv2.imread(self.img_paths[i])              # BGR, uint8, (H,W,3)
        img  = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)       # <-- do not forget this
        img  = cv2.resize(img, (self.size, self.size))
        mask = cv2.imread(self.mask_paths[i], cv2.IMREAD_GRAYSCALE)
        mask = cv2.resize(mask, (self.size, self.size),
                          interpolation=cv2.INTER_NEAREST) # keep labels crisp

        x = torch.from_numpy(img).permute(2, 0, 1).float() / 255.0   # (3,256,256) in [0,1]
        y = torch.from_numpy((mask > 0).astype("float32"))[None]      # (1,256,256) in {0,1}
        return x, y

# --- block 2 ---
import torch, torch.nn as nn
from torch.utils.data import DataLoader

model = build_unet(in_ch=3, out_ch=1).to("cuda")     # your U-Net or SMP's
loader = DataLoader(train_ds, batch_size=8, shuffle=True)
opt = torch.optim.Adam(model.parameters(), lr=1e-4)
bce = nn.BCEWithLogitsLoss()

def dice_loss(logits, target, eps=1.0):
    p = torch.sigmoid(logits)
    inter = (p * target).sum(dim=(2, 3))
    union = p.sum(dim=(2, 3)) + target.sum(dim=(2, 3))
    dice = (2 * inter + eps) / (union + eps)
    return 1 - dice.mean()

for epoch in range(30):
    model.train()
    for x, y in loader:
        x, y = x.to("cuda"), y.to("cuda")
        logits = model(x)                     # (B,1,256,256) raw scores
        loss = bce(logits, y) + dice_loss(logits, y)   # combo loss
        opt.zero_grad(); loss.backward(); opt.step()

# --- block 3 ---
@torch.no_grad()
def predict_mask(img_rgb, model, size=256):
    h0, w0 = img_rgb.shape[:2]
    x = cv2.resize(img_rgb, (size, size))
    x = torch.from_numpy(x).permute(2, 0, 1).float().div(255)[None].to("cuda")
    prob = torch.sigmoid(model(x))[0, 0].cpu().numpy()   # (256,256) in [0,1]
    mask = (prob > 0.5).astype("uint8") * 255            # hard 0/255 stencil
    return cv2.resize(mask, (w0, h0), interpolation=cv2.INTER_NEAREST)  # back to original

# --- block 4 ---
import gradio as gr, torch, cv2, numpy as np

model = build_unet(in_ch=3, out_ch=1)
model.load_state_dict(torch.load("unet_crack.pth", map_location="cpu"))
model.eval()

def infer(image):                       # Gradio gives an RGB numpy array
    mask = predict_mask(image, model)   # (H,W) uint8 0/255
    overlay = image.copy()
    overlay[mask > 0] = [255, 0, 0]     # paint cracks red
    return cv2.addWeighted(overlay, 0.5, image, 0.5, 0)

demo = gr.Interface(fn=infer,
                    inputs=gr.Image(type="numpy"),
                    outputs=gr.Image(type="numpy"),
                    title="Concrete Crack Segmenter",
                    examples=["examples/bridge.jpg"])
demo.launch()
