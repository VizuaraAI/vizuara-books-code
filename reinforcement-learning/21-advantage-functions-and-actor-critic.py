"""
Reinforcement Learning
Chapter 21: Advantage Functions and Actor-Critic
Section: Policy Gradient Methods from Scratch

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/advantage-functions-and-actor-critic

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
grad = grad_log_pi(a | s) * (G_t - V(s))

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# for each step (s, a, r, s_next) in the episode:
#     # critic evaluates
#     delta = r + gamma * V_w(s_next) - V_w(s)      # advantage estimate = TD error
#
#     # critic learns: reduce its own prediction error
#     w += beta * delta * grad_w(V_w(s))            # regression toward r + gamma*V(s_next)
#
#     # actor learns: push policy in direction of positive advantage
#     theta += alpha * delta * grad_theta(log pi_theta(a | s))
