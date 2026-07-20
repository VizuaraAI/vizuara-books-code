"""
Deep Learning Fundamentals
Chapter 26: Learning rate decay
Section: Optimizers

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/learning-rate-decay

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
class Optimizer_SGD:
    def __init__(self, learning_rate=1.0, decay=0.0):
        self.learning_rate = learning_rate   # lr_0, the starting stride
        self.current_lr    = learning_rate   # the stride we actually use this step
        self.decay         = decay
        self.iterations    = 0               # our `step` counter

    # call this ONCE before updating the layers each step
    def pre_update(self):
        if self.decay:
            self.current_lr = self.learning_rate / (1 + self.decay * self.iterations)

    def update(self, layer):
        # the same downhill step as before — just using current_lr
        layer.weights += -self.current_lr * layer.dweights
        layer.biases  += -self.current_lr * layer.dbiases

    # call this ONCE after the updates to advance the schedule
    def post_update(self):
        self.iterations += 1
