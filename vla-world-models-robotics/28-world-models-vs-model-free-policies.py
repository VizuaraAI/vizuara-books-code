"""
Vision-Language-Action & World Models for Robotics
Chapter 28: World Models vs Model-Free Policies
Section: World Models

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/world-models-vs-model-free-policies

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# The cost/reliability trade-off of a K-step world-model plan, on a napkin.
actions   = 3       # left / straight / right
K         = 3       # planning horizon (steps of imagination)
step_acc  = 0.95    # per-step accuracy of the learned dynamics model

rollouts        = actions ** K          # 27 imagined trajectories
forward_passes  = rollouts * K          # 81 calls to p(z'|z,a) per decision
trust_horizon   = step_acc ** K         # ~0.857 chance the rollout is reliable

# model-free policy, for contrast:
mf_forward_passes = 1                   # one reflex pass, always
