"""
Reinforcement Learning
Chapter 26: Project: An SLM That Writes Positive Stories
Section: RLHF from Scratch

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/project-an-slm-that-writes-positive-stories

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from transformers import pipeline
sentiment = pipeline("sentiment-analysis",
                     model="distilbert-base-uncased-finetuned-sst-2-english")

def reward(story: str) -> float:
    out = sentiment(story, truncation=True)[0]
    # score is P(label); flip sign for NEGATIVE so positive text scores higher
    return out["score"] if out["label"] == "POSITIVE" else -out["score"]

# --- block 2 ---
for prompts in dataloader:                      # each batch = 4 copies of "Once upon a time"
    responses = policy.generate(prompts,        # (1) sample 4 stories, 40 tokens each
                                max_new_tokens=40)
    stories   = [p + r for p, r in zip(prompts, responses)]
    rewards   = [reward(s) for s in stories]     # (2) score → e.g. [0.98, 0.11, -0.87, 0.95]
    ppo_trainer.step(prompts, responses, rewards) # (3)+(4) KL leash, advantage, clipped update
