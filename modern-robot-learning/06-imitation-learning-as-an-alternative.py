"""
Modern Robot Learning
Chapter 6: Imitation Learning as an Alternative
Section: Foundations of Robot Learning

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/imitation-learning-as-an-alternative

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# behavioral cloning: one gradient step
pred_action = policy(obs)                 # π_θ(o), shape (action_dim,)
loss = ((pred_action - expert_action) ** 2).mean()   # MSE to what the human did
loss.backward()                           # standard supervised backprop
optimizer.step()
