"""
Data Structures & Algorithms in Python
Chapter 53: Find the Middle of a Linked List
Section: Linked Lists

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/find-middle-of-linked-list

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

def middle_two_pass(head):
    n = 0
    node = head
    while node:                 # pass 1: count
        n += 1
        node = node.next
    node = head
    for _ in range(n // 2):     # pass 2: walk to the middle
        node = node.next
    return node

# --- block 2 ---
def middle_one_pass(head):
    slow = fast = head
    while fast and fast.next:   # can the hare still take two steps?
        slow = slow.next        # tortoise: +1
        fast = fast.next.next   # hare: +2
    return slow

# --- block 3 ---
def first_middle(head):
    slow = fast = head
    while fast.next and fast.next.next:   # look one node further ahead
        slow = slow.next
        fast = fast.next.next
    return slow                            # returns node 2 on 1→2→3→4
