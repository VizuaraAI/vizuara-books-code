"""
Reinforcement Learning
Chapter 33: Project: Turn an SLM into a Reasoning Model
Section: Build a Reasoning Model with GRPO

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/project-turn-an-slm-into-a-reasoning-model

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import re

def correctness_reward(completion: str, ground_truth: str) -> float:
    match = re.search(r"####\s*(-?[\d,]+)", completion)
    if match is None:
        return 0.0
    pred = match.group(1).replace(",", "")
    return 2.0 if pred == ground_truth else 0.0

# --- block 2 ---
def format_reward(completion: str) -> float:
    has_think = bool(re.search(r"<think>.*?</think>", completion, re.DOTALL))
    has_answer = "####" in completion
    return 0.5 * has_think + 0.5 * has_answer

# --- block 3 ---
import numpy as np
# total reward (correctness + format) for G = 8 completions to ONE prompt
r = np.array([3.0, 3.0, 0.5, 0.5, 1.0, 0.5, 0.0, 0.5])
adv = (r - r.mean()) / (r.std() + 1e-8)

# --- block 4 ---
from trl import GRPOConfig, GRPOTrainer

def reward_fn(completions, ground_truth, **kw):
    return [correctness_reward(c, g) + format_reward(c)
            for c, g in zip(completions, ground_truth)]

config = GRPOConfig(
    num_generations=8,        # G: group size per prompt
    max_completion_length=512, # room to actually think
    beta=0.04,                # KL penalty strength
    learning_rate=1e-6,       # small — we are nudging, not retraining
)

trainer = GRPOTrainer(
    model="Qwen/Qwen2.5-0.5B-Instruct",
    reward_funcs=reward_fn,
    args=config,
    train_dataset=gsm8k_train,
)
trainer.train()
