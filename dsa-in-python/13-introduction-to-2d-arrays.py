"""
Data Structures & Algorithms in Python
Chapter 13: Introduction to 2D Arrays
Section: Arrays & Matrices

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/introduction-to-2d-arrays

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
grid = [
    [ 5,  8,  1,  3],   # row 0
    [ 9,  2,  7,  4],   # row 1
    [ 6,  0,  8,  1],   # row 2
]

# --- block 2 ---
# NOTE: this block is prose in the book, not runnable code.
# It is the row-major index formula stated in symbols (r, c and cols are
# mathematical symbols here, not bound variables), so it is kept verbatim
# but commented out.
# flat = r * cols + c        # cols = number of columns = 4 here

# --- block 3 ---
grid = [[0] * 4] * 3        # WRONG: three references to the SAME row
grid[0][0] = 9
print(grid)                 # [[9,0,0,0], [9,0,0,0], [9,0,0,0]] — all rows changed!

# --- block 4 ---
rows, cols = 3, 4
grid = [[0] * cols for _ in range(rows)]   # RIGHT: a fresh row per iteration

# --- block 5 ---
for r in range(rows):           # for each row, top to bottom
    for c in range(cols):       # for each column, left to right
        print(grid[r][c])       # touches flat indices 0,1,2,...,11 in order
