"""
Build a Diffusion Language Model from Scratch
Chapter 9: The Noising and Denoising Loop
Section: The Diffusion Idea

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/noising-and-denoising

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# one training step (schematic)
x0 = sample_real_data()              # a clean example
t  = random_step()                   # pick a random corruption level
x_t = forward_corrupt(x0, t)         # FIXED recipe — free, no gradients
prediction = denoiser(x_t, t)        # the LEARNED network's guess
loss = mse(prediction, target(x0))   # how wrong was the correction?
loss.backward()                      # update ONLY the denoiser
