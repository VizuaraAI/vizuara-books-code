"""
Build Decision Trees from Scratch
Chapter 2: The Anatomy of a Decision Tree
Section: Foundations

Read this chapter: https://books.vizuara.ai/read/decision-trees-from-scratch/anatomy-of-a-decision-tree

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def grow(node_data):
    # 1. base case: should this become a leaf?
    if should_stop(node_data):
        return Leaf(prediction=summarize(node_data))

    # 2. greedy step: find the single best (feature, threshold)
    feature, threshold = best_split(node_data)

    # 3. split the rows into the two branches
    left_rows  = node_data[node_data[feature] <= threshold]
    right_rows = node_data[node_data[feature] >  threshold]

    # 4. recurse on each child — same function, smaller data
    return Node(feature, threshold,
                left  = grow(left_rows),
                right = grow(right_rows))
