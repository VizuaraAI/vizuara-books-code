"""
Vision-Language-Action & World Models for Robotics
Chapter 7: What Is a Vision-Language-Action Model?
Section: Introduction to Vision-Language-Action

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/what-is-a-vla-model

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def to_token(x, lo=-1.0, hi=1.0, n_bins=256):
    # clamp x into [lo, hi], then find which of 256 bins it lands in
    x = max(lo, min(hi, x))
    frac = (x - lo) / (hi - lo)          # 0.0 .. 1.0
    return min(int(frac * n_bins), n_bins - 1)   # an integer 0 .. 255
