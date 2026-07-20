"""
Data Structures & Algorithms in Python
Chapter 30: Longest Substring Without Repeating Characters
Section: Two Pointers & Sliding Window

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/longest-substring-without-repeating

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def length_of_longest_substring(s: str) -> int:
    seen = set()          # characters currently inside the window
    left = 0
    best = 0
    for right in range(len(s)):
        # shrink from the left until s[right] is safe to add
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        best = max(best, right - left + 1)   # current window length
    return best

# --- block 2 ---
def length_of_longest_substring(s: str) -> int:
    last = {}             # char -> most recent index seen
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1        # jump past the old copy
        last[ch] = right
        best = max(best, right - left + 1)
    return best
