"""
Data Structures & Algorithms in Python
Chapter 15: Print a Matrix in Snake Pattern
Section: Arrays & Matrices

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/print-matrix-snake-pattern

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
grid = [
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12],
]

# --- block 2 ---
def snake_order(grid):
    result = []
    for r, row in enumerate(grid):
        if r % 2 == 0:
            result.extend(row)          # even row: left-to-right
        else:
            result.extend(row[::-1])    # odd row: reversed copy, right-to-left
    return result

# --- block 3 ---
def snake_order_indexed(grid):
    if not grid:
        return []
    rows, cols = len(grid), len(grid[0])
    result = []
    for r in range(rows):
        if r % 2 == 0:
            for c in range(cols):            # 0 → cols-1
                result.append(grid[r][c])
        else:
            for c in range(cols - 1, -1, -1):  # cols-1 → 0
                result.append(grid[r][c])
    return result
