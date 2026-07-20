"""
The Modern Software Developer
Chapter 34: The Full Pipeline, End to End
Section: Putting It Together & What's Next

Read this chapter: https://books.vizuara.ai/read/modern-software-developer/the-full-pipeline-recap

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# test_streak.py — written BEFORE the implementation
from datetime import date
from streak import streak

def test_three_consecutive_days():
    days = [date(2026, 7, 4), date(2026, 7, 5), date(2026, 7, 6)]
    assert streak(days, today=date(2026, 7, 6)) == 3

def test_gap_breaks_the_streak():
    days = [date(2026, 7, 1), date(2026, 7, 5), date(2026, 7, 6)]
    assert streak(days, today=date(2026, 7, 6)) == 2   # the gap resets it

# --- block 2 ---
# streak.py
from datetime import date, timedelta

def streak(days, today):
    have = set(days)
    count, cursor = 0, today
    while cursor in have:          # walk backwards while each day is present
        count += 1
        cursor -= timedelta(days=1)
    return count
