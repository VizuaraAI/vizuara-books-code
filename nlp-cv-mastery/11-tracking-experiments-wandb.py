"""
NLP & Computer Vision Mastery
Chapter 11: Tracking Experiments with Weights & Biases
Section: From Linear Models to Deep Networks

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/tracking-experiments-wandb

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- context (added to make this file runnable) ---
# The chapter calls these with a literal ellipsis - train_one_epoch(...) -
# because the reader supplies them.
from context import train_one_epoch, evaluate

# --- block 1 ---
import wandb

# 1. start a run — this stamps a config and opens a logging channel
wandb.init(
    project="flowers-5class",
    config={
        "learning_rate": 1e-3,
        "hidden_units": 128,
        "dropout": 0.2,
        "batch_size": 32,
        "epochs": 15,
    },
)

# 2. in your training loop, log a dict of metrics per epoch
for epoch in range(15):
    train_loss, train_acc = train_one_epoch(...)
    val_loss,   val_acc   = evaluate(...)
    wandb.log({
        "train_loss": train_loss,
        "val_loss":   val_loss,
        "train_acc":  train_acc,
        "val_acc":    val_acc,
    })

# 3. close the run so the last data flushes
wandb.finish()
