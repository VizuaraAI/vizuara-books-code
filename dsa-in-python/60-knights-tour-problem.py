"""
Data Structures & Algorithms in Python
Chapter 60: Follow the Knight: The Knight's Tour
Section: Recursion & Backtracking

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/knights-tour-problem

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
MOVES = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
         ( 1, -2), ( 1, 2), ( 2, -1), ( 2, 1)]

# --- block 2 ---
def knights_tour(n=5, start=(0, 0)):
    board = [[-1] * n for _ in range(n)]
    sr, sc = start
    board[sr][sc] = 0                    # first square is move number 0

    def in_bounds(r, c):
        return 0 <= r < n and 0 <= c < n

    def solve(r, c, count):
        if count == n * n:               # base case: every square numbered
            return True
        for dr, dc in MOVES:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc) and board[nr][nc] == -1:
                board[nr][nc] = count     # (1) TRY: tentatively step here
                if solve(nr, nc, count + 1):   # (2) RECURSE: finish from there
                    return True
                board[nr][nc] = -1        # (3) UNDO: erase, try next candidate
        return False                      # exhausted all 8 → dead end

    return board if solve(sr, sc, 1) else None
