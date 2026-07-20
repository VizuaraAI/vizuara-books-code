"""
Build Decision Trees from Scratch
Chapter 17: Finishing the Regression Tree
Section: Regression Trees

Read this chapter: https://books.vizuara.ai/read/decision-trees-from-scratch/finishing-the-regression-tree

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def grow(rows, y, depth=0):
    # base cases: should this slice just become a leaf?
    if should_stop(rows, y, depth):
        return Leaf(prediction=y.mean())        # regression leaf = MEAN

    feature, threshold = best_split(rows, y)    # SSR-minimizing split
    left  = rows[:, feature] <= threshold
    right = ~left
    return Node(feature, threshold,
                left  = grow(rows[left],  y[left],  depth + 1),
                right = grow(rows[right], y[right], depth + 1))
