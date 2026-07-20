"""
Claude Certified Architect (CCAF)
Chapter 44: Confidence Scoring and Human-Review Routing
Section: Context Engineering and Reliability (Domain 5)

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/confidence-scoring-and-human-review

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def score(passes, self_conf, validation_ok, hit_other):
    # passes: list of extracted values from N independent runs
    agreement = passes.count(mode(passes)) / len(passes)   # e.g. 3/3 = 1.0
    conf = 0.5 * agreement + 0.3 * validation_ok + 0.2 * self_conf
    if hit_other or not validation_ok:
        conf = min(conf, 0.4)     # hard cap: never "high" if a check failed
    return conf
