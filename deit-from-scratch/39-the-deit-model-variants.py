"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 39: The DeiT Model Variants
Section: Putting It Together

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/the-deit-model-variants

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def pick_deit(latency_budget_ms, accuracy_floor_pct, distillation=True):
    # distillation lifts every variant a few points for ~free at inference,
    # so turn it on unless you have a reason not to.
    if latency_budget_ms < 5:          # edge / mobile, hard real-time
        return "DeiT-Ti"              # ~5M params, ~72% (higher with distill)
    if accuracy_floor_pct <= 80:       # the common case
        return "DeiT-S"              # ~22M, the knee of the curve
    return "DeiT-B"                  # ~86M, when you need the last ~2 points
