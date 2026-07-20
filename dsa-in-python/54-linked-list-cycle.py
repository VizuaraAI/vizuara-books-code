"""
Data Structures & Algorithms in Python
Chapter 54: Detect a Cycle (Floyd's Algorithm)
Section: Linked Lists

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/linked-list-cycle

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:      # fast leads, so guard fast AND fast.next
        slow = slow.next          # tortoise: one step
        fast = fast.next.next     # hare: two steps
        if slow is fast:          # same node object → cycle
            return True
    return False                  # fast fell off the end → no cycle
