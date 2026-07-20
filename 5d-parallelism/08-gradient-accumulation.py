"""
5D Parallelism for Large Model Training
Chapter 8: Gradient Accumulation
Section: Data Parallelism

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/gradient-accumulation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
K = 64                     # accumulation steps: global_batch / micro_batch = 512 / 8
optimizer.zero_grad()

for step in range(num_steps):
    for k in range(K):                       # inner loop: K micro-batches
        micro = next(micro_batch_iter)       # b = 8 examples
        loss = model(micro).loss / K         # <-- the /K that makes the sum a true average
        loss.backward()                      # gradients ADD into .grad (PyTorch accumulates)

    optimizer.step()                         # one step over the whole global batch
    optimizer.zero_grad()                    # only NOW do we clear the buffer
