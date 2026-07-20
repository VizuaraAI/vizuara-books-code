"""
Modern Robot Learning
Chapter 21: Fusing VAEs with Transformers for Robotics
Section: Transformer Architecture from Scratch

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/fusing-vaes-with-transformers-for-robotics

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# each adapter: a single learned Linear layer to width d = 512
joint_token  = W_joint @ joint_state   # (512, 6)  @ (6,)  -> (512,)
latent_token = W_latent @ z            # (512, 32) @ (32,) -> (512,)
