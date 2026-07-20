"""
Data Structures & Algorithms in Python
Chapter 50: Remove the N-th Node from the End
Section: Linked Lists

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/remove-nth-node-from-end

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_nth_from_end(head, n):
    dummy = Node(0)          # sentinel before the head
    dummy.next = head
    fast = slow = dummy      # both start on the dummy

    # 1. open a gap of n by advancing fast n steps
    for _ in range(n):
        fast = fast.next

    # 2. slide both until fast is on the last real node
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    # 3. slow now sits just before the target — splice it out
    slow.next = slow.next.next

    return dummy.next        # new head (handles head deletion)
