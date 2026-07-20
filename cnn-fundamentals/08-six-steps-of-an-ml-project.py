"""
Convolutional Neural Networks Fundamentals
Chapter 8: The Six Steps of an ML Project
Section: From Machine Learning to Deep Learning

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/six-steps-of-an-ml-project

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import torch

model = CNN()                                  # same architecture (the template)
model.load_state_dict(torch.load("cnn.pt"))    # fill the blanks with trained weights
model.eval()                                    # inference mode: no gradients, no dropout

with torch.no_grad():
    logits = model(new_scan)                    # one forward pass, shape (1, num_classes)
    probs  = torch.softmax(logits, dim=1)       # scores → a probability distribution
    label  = probs.argmax(dim=1)                # pick the most likely class
