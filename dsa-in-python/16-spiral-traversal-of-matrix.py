"""
Data Structures & Algorithms in Python
Chapter 16: Spiral Traversal of a Matrix
Section: Arrays & Matrices

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/spiral-traversal-of-matrix

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
M = [[ 1,  2,  3,  4],
     [ 5,  6,  7,  8],
     [ 9, 10, 11, 12]]

# --- block 2 ---
def spiral_order(M):
    if not M or not M[0]:
        return []
    result = []
    top, bottom = 0, len(M) - 1
    left, right = 0, len(M[0]) - 1

    while top <= bottom and left <= right:
        for c in range(left, right + 1):      # edge 1: top row, left → right
            result.append(M[top][c])
        top += 1

        for r in range(top, bottom + 1):      # edge 2: right col, top → bottom
            result.append(M[r][right])
        right -= 1

        if top <= bottom:                     # edge 3: bottom row, right → left
            for c in range(right, left - 1, -1):
                result.append(M[bottom][c])
            bottom -= 1

        if left <= right:                     # edge 4: left col, bottom → top
            for r in range(bottom, top - 1, -1):
                result.append(M[r][left])
            left += 1

    return result

# --- block 3 ---
R = [[1, 2, 3]]
