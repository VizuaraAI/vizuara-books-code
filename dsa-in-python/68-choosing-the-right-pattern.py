"""
Data Structures & Algorithms in Python
Chapter 68: Choosing the Right Pattern
Section: Greedy Algorithms & Capstone

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/choosing-the-right-pattern

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def longest_unique(s):
    seen = set()
    left = 0
    best = 0
    for right, ch in enumerate(s):
        while ch in seen:            # shrink until the window is valid again
            seen.remove(s[left])
            left += 1
        seen.add(ch)
        best = max(best, right - left + 1)
    return best

longest_unique("abcabcbb")   # -> 3  (the window "abc")
