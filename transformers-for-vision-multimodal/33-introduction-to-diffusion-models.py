"""
Transformers for Vision & Multimodal LLMs
Chapter 33: Introduction to Diffusion Models
Section: Generative Vision — Autoencoders to Diffusion

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/introduction-to-diffusion-models

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# one forward step: x_{t-1}  ->  x_t
x_t = sqrt(1 - beta_t) * x_prev + sqrt(beta_t) * noise   # noise ~ N(0, I)

# --- block 2 ---
x_t = sqrt(alpha_bar_t) * x_0 + sqrt(1 - alpha_bar_t) * noise   # noise ~ N(0, I)

# --- block 3 ---
# one training step (DDPM, simplified loss)
t     = randint(1, T)                                   # random timestep
eps   = randn_like(x0)                                  # the true noise
x_t   = sqrt(alpha_bar[t]) * x0 + sqrt(1 - alpha_bar[t]) * eps
loss  = mse(model(x_t, t), eps)                         # predict the noise

# --- block 4 ---
# one sampling step: x_t -> x_{t-1}
eps_hat = model(x_t, t)
mean    = (x_t - beta[t]/sqrt(1 - alpha_bar[t]) * eps_hat) / sqrt(alpha[t])
x_prev  = mean + sqrt(beta[t]) * randn_like(x_t)   # no added noise on the final step t=1
