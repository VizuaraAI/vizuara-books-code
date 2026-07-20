"""
Data Structures & Algorithms in Python
Chapter 52: Reverse a Linked List
Section: Linked Lists

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/reverse-a-linked-list

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

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next     # 1. remember the rest of the list
        curr.next = prev    # 2. flip this node's arrow backward
        prev = curr         # 3. prev advances onto the flipped node
        curr = nxt          # 4. curr advances to the saved next
    return prev             # curr is None; prev is the new head

# --- block 2 ---
def reverse_list_recursive(head):
    if head is None or head.next is None:
        return head                     # base case: empty or single node
    new_head = reverse_list_recursive(head.next)
    head.next.next = head               # make the next node point back at us
    head.next = None                    # and sever our old forward arrow
    return new_head                     # same new head bubbles all the way up
