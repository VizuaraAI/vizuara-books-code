"""
Vision-Language-Action & World Models for Robotics
Chapter 6: Setting Up Your Environment
Section: Foundations: Perception, Language, Action

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/environment-setup-and-prerequisites

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch
print(torch.__version__)                 # e.g. 2.x.x+cu121
print(torch.cuda.is_available())         # must print True to train on GPU
print(torch.cuda.get_device_name(0))     # e.g. "NVIDIA RTX A4000"
