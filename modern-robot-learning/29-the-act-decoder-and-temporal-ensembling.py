"""
Modern Robot Learning
Chapter 29: The ACT Decoder and Temporal Ensembling
Section: The ACT Policy

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/the-act-decoder-and-temporal-ensembling

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

preds  = np.array([31.0, 30.4, 29.2])   # newest → oldest guesses for timestep 8
ages   = np.array([0, 1, 2])            # how many steps old each prediction is
m      = 0.1                            # decay: bigger = trust the newest more

w = np.exp(-m * ages)                   # raw exponential weights
w = w / w.sum()                         # normalize to sum to 1
action = float(w @ preds)               # weighted average → the command we send
print(round(action, 2))                 # 30.26
