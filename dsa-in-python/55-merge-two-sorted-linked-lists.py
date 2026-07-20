"""
Data Structures & Algorithms in Python
Chapter 55: Merge Two Sorted Linked Lists
Section: Linked Lists

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/merge-two-sorted-linked-lists

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# --- block 2 ---
def merge_two_lists(a, b):
    dummy = ListNode()      # sentinel; real list will start at dummy.next
    tail = dummy            # tail always points at the last node built so far

    while a and b:          # while BOTH lists still have nodes
        if a.val <= b.val:  # <= keeps the merge STABLE (ties keep A's node first)
            tail.next = a   # splice A's front onto the result
            a = a.next      # advance A
        else:
            tail.next = b
            b = b.next
        tail = tail.next    # move the tail forward — same line every time

    tail.next = a if a else b   # one list is empty; staple the other's remainder
    return dummy.next           # skip the sentinel, return the real head

# --- block 3 ---
def merge_two_lists(a, b):
    if not a: return b          # base case: A empty → answer is B
    if not b: return a          # base case: B empty → answer is A
    if a.val <= b.val:
        a.next = merge_two_lists(a.next, b)   # keep A's front, merge the rest
        return a
    else:
        b.next = merge_two_lists(a, b.next)   # keep B's front, merge the rest
        return b
