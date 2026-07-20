"""
Build Decision Trees from Scratch
Chapter 5: Starting to Build a Classification Tree
Section: Classification Trees

Read this chapter: https://books.vizuara.ai/read/decision-trees-from-scratch/starting-a-classification-tree

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
best_score = float("inf")      # lower impurity is better; start at +infinity
best_split = None

for feature in features:                       # weight, then age
    values = sorted(set(rows[:, feature]))     # unique values in THIS node
    for a, b in zip(values, values[1:]):       # adjacent pairs
        threshold = (a + b) / 2                # the midpoint candidate
        left  = rows[rows[:, feature] <= threshold]
        right = rows[rows[:, feature] >  threshold]
        score = weighted_gini(left, right)     # defined next chapter
        if score < best_score:
            best_score = score
            best_split = (feature, threshold)
