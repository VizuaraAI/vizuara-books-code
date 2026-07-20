"""
RLHF from Scratch
Chapter 30: Aligning the SLM with a Reward Signal
Section: Building It From Scratch

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/aligning-the-slm-with-a-reward-signal

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from transformers import pipeline

sentiment = pipeline("sentiment-analysis", model="...distilbert-sst2...")

def reward_fn(story: str) -> float:
    out = sentiment(story)[0]                 # {'label': 'POSITIVE'/'NEGATIVE', 'score': p}
    p = out["score"]
    return p if out["label"] == "POSITIVE" else 1.0 - p
