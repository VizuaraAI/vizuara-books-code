"""
Deep Learning Fundamentals
Chapter 38: What we built, and where to go next
Section: Hands-On Projects

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/what-we-built-and-where-next

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- placeholders the reader supplies ---
# This closing chapter sketches the same training loop in a framework's shape
# (autograd, optimizer.step()). Nothing here is constructed by the book; the
# names are the sketch's own.
# See https://books.vizuara.ai/read/deep-learning-fundamentals/what-we-built-and-where-next
epochs    = 100   # TODO: your training length
model     = None  # TODO: your network - the book's Dense/ReLU chain, or a framework model
loss_fn   = None  # TODO: your loss - the book's cross-entropy, or a framework loss
optimizer = None  # TODO: your optimizer - chapters 25-30, or a framework optimizer
X         = None  # TODO: your features
y         = None  # TODO: your labels

# --- block 1 ---
for epoch in range(epochs):
    y_pred = model(X)                 # forward  (your Dense.forward chain)
    loss = loss_fn(y_pred, y)         # loss     (your cross-entropy)
    optimizer.zero_grad()
    loss.backward()                   # backward (autograd replaces all your backward() code)
    optimizer.step()                  # update   (your optimizer.update_params)
