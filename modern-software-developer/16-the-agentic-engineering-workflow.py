"""
The Modern Software Developer
Chapter 16: The Agentic Engineering Workflow
Section: PRD-Driven Agentic Engineering

Read this chapter: https://books.vizuara.ai/read/modern-software-developer/the-agentic-engineering-workflow

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def test_streak_resets_after_missed_day():
    h = Habit("drink water")
    h.mark_done(day=1)
    h.mark_done(day=3)          # skipped day 2
    assert h.streak() == 1      # not 2 — the miss reset it
