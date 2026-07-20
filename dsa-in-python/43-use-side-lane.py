"""
Data Structures & Algorithms in Python
Chapter 43: Use Side Lane
Section: Stacks & Queues

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/use-side-lane

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def sort_stack(input_stack):
    aux = []                              # the side lane: kept sorted, largest on top
    while input_stack:
        temp = input_stack.pop()          # take the top of the input
        # evict every side-lane element bigger than temp, back onto the input
        while aux and aux[-1] > temp:
            input_stack.append(aux.pop())
        aux.append(temp)                  # temp now lands in its sorted spot
    return aux

# sort_stack([3, 1, 4, 2]) -> [1, 2, 3, 4]   (4 on top)
