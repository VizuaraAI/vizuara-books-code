"""
Machine Learning & Deep Learning Mastery
Chapter 42: Let Us Start Building a Decision Tree
Section: CNNs & Decision Trees

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/growing-a-decision-tree

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# grow() below is the skeleton of the algorithm; the chapter describes its
# helpers in prose and leaves them to you. best_split() and a gini impurity
# arrive later, in chapters 43 and 45, under different names and signatures,
# so nothing here is imported from an earlier chapter.
# TODO: see https://books.vizuara.ai/read/ml-dl-mastery/growing-a-decision-tree
impurity = None    # TODO: you supply this - impurity of a list of labels (ch 43: gini)
majority = None    # TODO: you supply this - the most common label in a list
best_split = None  # TODO: you supply this - returns (feature, value, gain); cf. ch 45
Leaf = None        # TODO: you supply this - a leaf node holding a prediction
Node = None        # TODO: you supply this - an internal node: question + two children

# --- block 1 ---
def grow(rows, depth=0, max_depth=5, min_samples_split=2):
    labels = [r.label for r in rows]

    # base cases: a stopping rule fires -> make a leaf
    if impurity(labels) == 0 \
       or depth == max_depth \
       or len(rows) < min_samples_split:
        return Leaf(prediction=majority(labels))

    # 1. find the split with the lowest weighted child impurity
    feature, value, gain = best_split(rows)

    # 4. no split actually helps -> leaf
    if gain <= 0:
        return Leaf(prediction=majority(labels))

    # 2. partition the rows on that question
    left  = [r for r in rows if r[feature] == value]
    right = [r for r in rows if r[feature] != value]

    # 3. recurse on each pile
    return Node(feature, value,
                left=grow(left,  depth + 1, max_depth, min_samples_split),
                right=grow(right, depth + 1, max_depth, min_samples_split))
