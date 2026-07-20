"""
NLP & Computer Vision Mastery
Chapter 12: Overfitting and the Bias-Variance Tradeoff
Section: Generalization and Transfer Learning

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/overfitting-and-the-bias-variance-tradeoff

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added to make this file runnable) ---
# The chapter logs to Weights & Biases, introduced in chapter 11, so the
# import line is not repeated here.
import wandb

# --- context (added to make this file runnable) ---
from context import model, train_loader, val_loader, train_one_epoch, evaluate

# How many passes over the data to run.
# TODO: pick your own; chapter 11's config uses 15.
# See https://books.vizuara.ai/read/nlp-cv-mastery/tracking-experiments-wandb
epochs = 15

# --- block 1 ---
# after each epoch, log BOTH losses — the gap is the diagnosis
for epoch in range(epochs):
    train_loss = train_one_epoch(model, train_loader)   # images the model studies
    val_loss   = evaluate(model, val_loader)            # held-out images
    gap = val_loss - train_loss
    wandb.log({"train_loss": train_loss,
               "val_loss": val_loss,
               "gen_gap": gap})                          # watch this number
    print(f"epoch {epoch}: train {train_loss:.3f} | val {val_loss:.3f} | gap {gap:+.3f}")
