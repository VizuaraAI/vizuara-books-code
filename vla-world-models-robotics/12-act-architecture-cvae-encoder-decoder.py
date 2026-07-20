"""
Vision-Language-Action & World Models for Robotics
Chapter 12: ACT Architecture: A Conditional VAE
Section: Building the Action Chunking Transformer

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/act-architecture-cvae-encoder-decoder

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
mu     = [ 0.81, -0.12,  0.44,  0.05]   # (d_z=4,)  "this is a left-ish style"
logvar = [-2.3,  -2.1,  -2.4,  -2.0]    # small variance → confident
eps    = [ 0.11,  0.02, -0.30,  0.44]   # ε ~ N(0, 1)
# z = mu + exp(0.5*logvar) * eps
z      = [ 0.84, -0.11,  0.35,  0.21]   # the style code fed to the decoder
