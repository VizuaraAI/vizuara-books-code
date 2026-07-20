"""
Machine Learning & Deep Learning Mastery
Chapter 45: Project: Code a Decision Tree from Scratch
Section: CNNs & Decision Trees

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/code-a-decision-tree-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# majority_label() and majority_leaf() are used by blocks 3 and 5 but the book
# never prints them, so they are stubbed rather than invented.
# TODO: see https://books.vizuara.ai/read/ml-dl-mastery/code-a-decision-tree-from-scratch
majority_label = None  # TODO: you supply this - most common label among rows
majority_leaf = None   # TODO: you supply this - majority prediction of a subtree's leaves

# AUTHORING BUG: best_split() in block 2 divides by `n`, which it never binds
# (in context it means len(rows)). Stubbed at module scope so the file checks
# clean; the fix belongs in the book, not here.
n = None  # TODO: authoring bug - see the note above

# --- block 1 ---
# (weight, color_score) -> label
data = [
    (150, 1, "apple"),  (170, 1, "apple"),  (140, 0, "apple"),
    (160, 1, "apple"),  (155, 0, "apple"),
    (8,   1, "cherry"), (6,   1, "cherry"), (9,   0, "cherry"),
    (7,   1, "cherry"), (10,  1, "cherry"),
]

# --- block 2 ---
def gini(rows):
    n = len(rows)
    if n == 0:
        return 0.0
    counts = {}
    for *_feats, label in rows:
        counts[label] = counts.get(label, 0) + 1
    return 1.0 - sum((c / n) ** 2 for c in counts.values())

def best_split(rows):
    best = {"gini": float("inf"), "feature": None, "threshold": None}
    n_features = len(rows[0]) - 1          # last entry is the label
    for f in range(n_features):
        values = sorted(set(r[f] for r in rows))
        # candidate thresholds = midpoints between adjacent sorted values
        thresholds = [(a + b) / 2 for a, b in zip(values, values[1:])]
        for t in thresholds:
            left  = [r for r in rows if r[f] <= t]
            right = [r for r in rows if r[f] >  t]
            if not left or not right:
                continue
            n_l, n_r = len(left), len(right)
            weighted = (n_l * gini(left) + n_r * gini(right)) / n
            if weighted < best["gini"]:
                best = {"gini": weighted, "feature": f, "threshold": t}
    return best

# --- block 3 ---
def build_tree(rows, depth=0, max_depth=None):
    node_gini = gini(rows)
    # stopping rules -> make a leaf
    if node_gini == 0 or (max_depth is not None and depth >= max_depth):
        return {"leaf": True, "prediction": majority_label(rows), "n": len(rows)}

    split = best_split(rows)
    if split["feature"] is None or split["gini"] >= node_gini:
        return {"leaf": True, "prediction": majority_label(rows), "n": len(rows)}

    f, t = split["feature"], split["threshold"]
    left  = [r for r in rows if r[f] <= t]
    right = [r for r in rows if r[f] >  t]
    return {
        "leaf": False, "feature": f, "threshold": t,
        "left":  build_tree(left,  depth + 1, max_depth),
        "right": build_tree(right, depth + 1, max_depth),
    }

# --- block 4 ---
def predict(node, x):
    while not node["leaf"]:
        node = node["left"] if x[node["feature"]] <= node["threshold"] else node["right"]
    return node["prediction"]

# --- block 5 ---
def prune(node, val_rows):
    if node["leaf"]:
        return node
    # recurse first: prune children bottom-up
    f, t = node["feature"], node["threshold"]
    left_val  = [r for r in val_rows if r[f] <= t]
    right_val = [r for r in val_rows if r[f] >  t]
    node["left"]  = prune(node["left"],  left_val)
    node["right"] = prune(node["right"], right_val)

    # would collapsing this node into a leaf hurt validation accuracy?
    leaf_pred = majority_leaf(node)      # majority prediction of the subtree's leaves
    subtree_correct = sum(predict(node, r) == r[-1] for r in val_rows)
    leaf_correct    = sum(leaf_pred        == r[-1] for r in val_rows)
    if leaf_correct >= subtree_correct:
        return {"leaf": True, "prediction": leaf_pred, "n": len(val_rows)}
    return node
