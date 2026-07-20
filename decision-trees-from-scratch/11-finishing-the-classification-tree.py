"""
Build Decision Trees from Scratch
Chapter 11: Finishing the Classification Tree
Section: Classification Trees

Read this chapter: https://books.vizuara.ai/read/decision-trees-from-scratch/finishing-the-classification-tree

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def predict_one(node, row):
    # Walk from this node down to a leaf, then return its stored class.
    while node.prediction is None:          # None means "internal node"
        if row[node.feature] <= node.threshold:
            node = node.left                # test True  → go left
        else:
            node = node.right               # test False → go right
    return node.prediction                  # reached a leaf: read the vote

def predict(tree_root, X):
    return [predict_one(tree_root, row) for row in X]
