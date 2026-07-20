"""
Data Structures & Algorithms in Python
Chapter 49: Introduction to the Linked List
Section: Linked Lists

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/introduction-to-linked-lists

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
class Node:
    def __init__(self, val):
        self.val = val        # the data this node holds
        self.next = None      # reference to the next Node (or None at the end)

# --- block 2 ---
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
# head.next.next.next is None → end of list

# --- block 3 ---
new_node = Node(15)
new_node.next = head.next   # 15 → 20  (grab the rest of the list)
head.next = new_node        # 10 → 15  (splice it in)
# list is now 10 → 15 → 20 → 30

# --- block 4 ---
def length(head):
    count = 0
    cur = head
    while cur is not None:   # stop exactly when we run off the end
        count += 1
        cur = cur.next
    return count

# --- block 5 ---
def get(head, index):
    cur = head
    for _ in range(index):       # follow .next `index` times
        cur = cur.next
    return cur.val
