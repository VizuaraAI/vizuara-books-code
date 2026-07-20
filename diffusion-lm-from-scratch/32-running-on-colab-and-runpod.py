"""
Build a Diffusion Language Model from Scratch
Chapter 32: Running on Colab and RunPod
Section: Build It: Code the Diffusion LM

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/running-on-colab-and-runpod

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
print(torch.cuda.is_available())      # True  -> a GPU is attached
print(torch.cuda.get_device_name(0))  # 'Tesla T4'
device = "cuda" if torch.cuda.is_available() else "cpu"

# --- block 2 ---
from google.colab import drive
drive.mount('/content/drive')          # asks for auth once
CKPT_DIR = '/content/drive/MyDrive/diffusion-lm'   # this SURVIVES a disconnect

# --- block 3 ---
def save_checkpoint(step, model, optimizer, path):
    torch.save({
        "step": step,
        "model": model.state_dict(),        # the weights
        "optim": optimizer.state_dict(),    # Adam's moments — resume needs these!
    }, path)

# ...inside the loop, every N steps:
if step % 500 == 0:
    save_checkpoint(step, model, optimizer, f"{CKPT_DIR}/ckpt_{step}.pt")

# --- block 4 ---
ckpt = torch.load(f"{CKPT_DIR}/ckpt_2500.pt", map_location=device)
model.load_state_dict(ckpt["model"])
optimizer.load_state_dict(ckpt["optim"])
start_step = ckpt["step"]               # pick up exactly where we fell over

# --- block 5 ---
CKPT_DIR = "/workspace/diffusion-lm"   # a RunPod persistent volume path
# every torch.save / torch.load line above is UNCHANGED
