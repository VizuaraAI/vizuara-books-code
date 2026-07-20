"""
Data Structures & Algorithms in Python
Chapter 41: Valid Parentheses
Section: Stacks & Queues

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/valid-parentheses

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def is_valid(s: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}   # closer -> its opener
    stack = []
    for ch in s:
        if ch in pairs:                       # ch is a closer
            # stack must be non-empty AND its top must be the match
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:                                 # ch is an opener
            stack.append(ch)
    return not stack                          # valid only if nothing left open
