"""
RLHF from Scratch
Chapter 15: Evaluating and Trusting the Reward Model
Section: Reward Models

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/evaluating-and-trusting-the-reward-model

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def preference_accuracy(reward_model, eval_pairs):
    correct = 0
    for x, y_w, y_l in eval_pairs:
        r_w = reward_model(x, y_w)   # scalar for the chosen answer
        r_l = reward_model(x, y_l)   # scalar for the rejected answer
        if r_w > r_l:                # did we agree with the human?
            correct += 1
    return correct / len(eval_pairs)
