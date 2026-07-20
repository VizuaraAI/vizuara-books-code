"""
Data Structures & Algorithms in Python
Chapter 51: Rotate a Linked List
Section: Linked Lists

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/rotate-a-linked-list

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# --- block 2 ---
def rotate_right(head, k):
    # Edge cases: empty list or single node — nothing to rotate.
    if head is None or head.next is None:
        return head

    # 1. Measure the length n and grab the tail in one pass.
    n = 1
    tail = head
    while tail.next:
        tail = tail.next
        n += 1

    # 2. Reduce k. If it lands on 0, the list is unchanged.
    k = k % n
    if k == 0:
        return head

    # 3. Close the list into a ring.
    tail.next = head

    # 4. Walk (n - k) steps from head to reach the NEW tail.
    steps_to_new_tail = n - k
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next

    # 5. The new head is right after the new tail; break the ring.
    new_head = new_tail.next
    new_tail.next = None
    return new_head
