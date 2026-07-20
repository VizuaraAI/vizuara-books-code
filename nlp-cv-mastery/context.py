"""
NLP & Computer Vision Mastery - shared context for the companion code.

Read the book: https://books.vizuara.ai/read/nlp-cv-mastery

WHAT THIS FILE IS
-----------------
Several chapters write a training loop that calls helpers the book never
spells out in a code block - `train_one_epoch(...)`, `evaluate(...)`, and the
`model` / `train_loader` / `val_loader` handles they operate on. In the book
these are deliberately left to the reader: chapter 11, for example, literally
writes `train_one_epoch(...)` with an ellipsis for the arguments.

This module holds ONE honest placeholder per such name so the chapter files
import cleanly instead of repeating the same stub five times.

WHAT THIS FILE IS NOT
---------------------
It is NOT book code. Nothing here was extracted from a chapter, and nothing
here is a working implementation. Every value below is a stub. Replace them
with your own model, data loaders, and train/eval functions before running
any chapter file.
"""

# The network being trained. The book uses whichever architecture the current
# chapter is about (a small Sequential net, a fine-tuned AlexNet, a U-Net...).
# TODO: assign your own model, e.g. the classifier built in chapter 14.
# See https://books.vizuara.ai/read/nlp-cv-mastery/dropout-augmentation-early-stopping
model = None

# Batched iterators over the training / validation splits. In the book these
# are torch DataLoaders yielding (images, labels) or (images, masks).
# TODO: build these from your own dataset.
# See https://books.vizuara.ai/read/nlp-cv-mastery/finetuning-alexnet-in-code
train_loader = None
val_loader = None


def train_one_epoch(*args, **kwargs):
    """One pass over the training data.

    TODO: the reader supplies this. It should loop over `train_loader`, run
    forward/backward/step, and return the epoch's training loss (chapter 11
    also unpacks an accuracy, i.e. `train_loss, train_acc = train_one_epoch(...)`).
    See https://books.vizuara.ai/read/nlp-cv-mastery/tracking-experiments-wandb
    """
    raise NotImplementedError("Supply your own training step - see the chapter.")


def evaluate(*args, **kwargs):
    """One pass over the held-out data, with no gradient updates.

    TODO: the reader supplies this. It should return the validation loss
    (chapter 11 also unpacks an accuracy, i.e. `val_loss, val_acc = evaluate(...)`).
    See https://books.vizuara.ai/read/nlp-cv-mastery/tracking-experiments-wandb
    """
    raise NotImplementedError("Supply your own evaluation step - see the chapter.")
