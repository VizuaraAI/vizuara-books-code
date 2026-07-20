"""
Reinforcement Learning
Chapter 29: Project: A Reddit Post Summarizer
Section: RLHF from Scratch

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/project-a-reddit-post-summarizer

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch

# --- block 1 ---
# rw, rl are the reward-model scalars for the winning / losing summary
loss = -torch.log(torch.sigmoid(rw - rl)).mean()

# --- block 2 ---
# per-token reward: reward-model score MINUS a leash to the reference model
reward_t = reward_model_score_at_end - beta * kl(policy_logprob, ref_logprob)
