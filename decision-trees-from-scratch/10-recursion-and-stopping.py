"""
Build Decision Trees from Scratch
Chapter 10: Recursion and Stopping Rules
Section: Classification Trees

Read this chapter: https://books.vizuara.ai/read/decision-trees-from-scratch/recursion-and-stopping

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def grow(rows, depth=0):
    # 1. base cases: should this slice just become a leaf?
    if should_stop(rows, depth):
        return Leaf(prediction=majority_class(rows))

    # 2. greedy step: find the single best (feature, threshold)
    feature, threshold = best_split(rows)

    # 3. partition the rows into the two branches
    left_rows  = rows[rows[:, feature] <= threshold]
    right_rows = rows[rows[:, feature] >  threshold]

    # 4. recurse on each child, one level deeper — SAME function
    return Node(feature, threshold,
                left  = grow(left_rows,  depth + 1),
                right = grow(right_rows, depth + 1))
