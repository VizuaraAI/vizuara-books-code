"""
Data Structures & Algorithms in Python
Chapter 14: Transpose & Rotate a Matrix
Section: Arrays & Matrices

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/transpose-and-rotate-matrix

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def transpose(M):
    n = len(M)
    for i in range(n):
        for j in range(i + 1, n):        # upper triangle only: j > i
            M[i][j], M[j][i] = M[j][i], M[i][j]
    return M

# --- block 2 ---
def rotate_clockwise(M):
    n = len(M)
    # 1. transpose: swap across the main diagonal
    for i in range(n):
        for j in range(i + 1, n):
            M[i][j], M[j][i] = M[j][i], M[i][j]
    # 2. reverse each row in place
    for row in M:
        row.reverse()
    return M
