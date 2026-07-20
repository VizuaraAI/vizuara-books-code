"""
Machine Learning Fundamentals
Chapter 1: What Is Machine Learning?
Section: Foundations of Machine Learning

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/what-is-machine-learning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def is_spam(email):
    if "free money" in email.text.lower():
        return True
    if email.num_links > 20:
        return True
    if "click here to claim" in email.text.lower():
        return True
    return False

# --- block 2 ---
for step in range(num_steps):
    z = X @ w + b            # scores for every training example
    loss, grad_w, grad_b = compute_loss(z, y)   # how wrong, and which way is downhill
    w = w - eta * grad_w     # take a small step downhill (eta = learning rate)
    b = b - eta * grad_b
# w and b now ARE the trained model
