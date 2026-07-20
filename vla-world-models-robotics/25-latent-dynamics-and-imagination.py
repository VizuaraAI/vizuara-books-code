"""
Vision-Language-Action & World Models for Robotics
Chapter 25: Latent Dynamics and Imagination
Section: World Models

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/latent-dynamics-and-imagination

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
z_t = [ 0.9, -0.3, 0.1, 0.6 ]   # 4-number summary of "cone ahead, slightly left, car centered"

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# z_next = f([0.9, -0.3, 0.1, 0.6], a_t = -0.5)
#        = [ 0.7, -0.6, 0.1, 0.55 ]   # obstacle a bit closer, now more to the right of us
