"""
RLHF from Scratch
Chapter 10: The Problem of Subjective Rewards
Section: Reward Models

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/the-problem-of-subjective-rewards

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def reward_math(response, answer):
    return 1.0 if extract_number(response) == answer else 0.0
