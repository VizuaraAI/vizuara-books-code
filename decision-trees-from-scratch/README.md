# Build Decision Trees from Scratch - companion code

Runnable code extracted from every chapter of [Build Decision Trees from Scratch](https://books.vizuara.ai/read/decision-trees-from-scratch), in reading order.

These files are **generated** from the book text by `tools/build_companion_repo.py`. Do not hand-edit them.

17 of 23 chapters contain Python code (28 code blocks total).

| # | Chapter | File | Blocks | Added imports | Read online |
|---|---------|------|--------|---------------|-------------|
| 2 | The Anatomy of a Decision Tree | [`02-anatomy-of-a-decision-tree.py`](02-anatomy-of-a-decision-tree.py) | 1 | 0 | [link](https://books.vizuara.ai/read/decision-trees-from-scratch/anatomy-of-a-decision-tree) |
| 3 | Classification vs Regression Trees | [`03-classification-vs-regression-trees.py`](03-classification-vs-regression-trees.py) | 1 | 0 | [link](https://books.vizuara.ai/read/decision-trees-from-scratch/classification-vs-regression-trees) |
| 5 | Starting to Build a Classification Tree | [`05-starting-a-classification-tree.py`](05-starting-a-classification-tree.py) | 1 | 0 | [link](https://books.vizuara.ai/read/decision-trees-from-scratch/starting-a-classification-tree) |
| 7 | Gini Impurity: A Worked Example | [`07-gini-impurity-worked-example.py`](07-gini-impurity-worked-example.py) | 1 | 0 | [link](https://books.vizuara.ai/read/decision-trees-from-scratch/gini-impurity-worked-example) |
| 8 | Gini Impurity for Numerical Features | [`08-gini-for-numerical-features.py`](08-gini-for-numerical-features.py) | 1 | 0 | [link](https://books.vizuara.ai/read/decision-trees-from-scratch/gini-for-numerical-features) |
| 9 | Choosing the Best Split | [`09-choosing-the-best-split.py`](09-choosing-the-best-split.py) | 1 | 0 | [link](https://books.vizuara.ai/read/decision-trees-from-scratch/choosing-the-best-split) |
| 10 | Recursion and Stopping Rules | [`10-recursion-and-stopping.py`](10-recursion-and-stopping.py) | 1 | 0 | [link](https://books.vizuara.ai/read/decision-trees-from-scratch/recursion-and-stopping) |
| 11 | Finishing the Classification Tree | [`11-finishing-the-classification-tree.py`](11-finishing-the-classification-tree.py) | 1 | 0 | [link](https://books.vizuara.ai/read/decision-trees-from-scratch/finishing-the-classification-tree) |
| 13 | Code an Entire Classification Tree in Python | [`13-code-classification-tree-python.py`](13-code-classification-tree-python.py) | 6 | 0 | [link](https://books.vizuara.ai/read/decision-trees-from-scratch/code-classification-tree-python) |
| 15 | Variance and SSR as the Split Criterion | [`15-variance-as-a-split-criterion.py`](15-variance-as-a-split-criterion.py) | 1 | 0 | [link](https://books.vizuara.ai/read/decision-trees-from-scratch/variance-as-a-split-criterion) |
| 16 | Building the First Regression Split | [`16-starting-a-regression-tree.py`](16-starting-a-regression-tree.py) | 1 | 0 | [link](https://books.vizuara.ai/read/decision-trees-from-scratch/starting-a-regression-tree) |
| 17 | Finishing the Regression Tree | [`17-finishing-the-regression-tree.py`](17-finishing-the-regression-tree.py) | 1 | 0 | [link](https://books.vizuara.ai/read/decision-trees-from-scratch/finishing-the-regression-tree) |
| 18 | Regression Trees with Multiple Features | [`18-regression-trees-multiple-features.py`](18-regression-trees-multiple-features.py) | 1 | 0 | [link](https://books.vizuara.ai/read/decision-trees-from-scratch/regression-trees-multiple-features) |
| 19 | Code an Entire Regression Tree in Python | [`19-code-regression-tree-python.py`](19-code-regression-tree-python.py) | 6 | 0 | [link](https://books.vizuara.ai/read/decision-trees-from-scratch/code-regression-tree-python) |
| 20 | Capstone: Fit and Read a Regression Tree | [`20-regression-tree-capstone.py`](20-regression-tree-capstone.py) | 2 | 0 | [link](https://books.vizuara.ai/read/decision-trees-from-scratch/regression-tree-capstone) |
| 21 | Recap: Two Trees, One Algorithm | [`21-classification-vs-regression-recap.py`](21-classification-vs-regression-recap.py) | 1 | 0 | [link](https://books.vizuara.ai/read/decision-trees-from-scratch/classification-vs-regression-recap) |
| 23 | From One Tree to Forests and Boosting | [`23-from-trees-to-forests.py`](23-from-trees-to-forests.py) | 1 | 0 | [link](https://books.vizuara.ai/read/decision-trees-from-scratch/from-trees-to-forests) |

## Notes

- Each file concatenates that chapter's Python blocks in document order, separated by `# --- block N ---` markers.
- Non-Python blocks (shell commands, sample output, JSON, plain text) are not included.
- Blocks are teaching excerpts. Many assume variables or imports introduced earlier in the chapter or in an earlier chapter, so an individual file is not guaranteed to run standalone.
- The only code the generator writes itself is the `# --- imports (added by the generator) ---` block: a canonical import line for a well-known alias (`np`, `torch`, `nn`, ...) that the chapter uses as a module but never imports and never assigns. Nothing else is added, and no book code is rewritten.
- A block tagged `python` in the book that will not compile - prose, pseudo-code, or a fragment shown out of context - is kept verbatim but commented out, labelled `# --- block N (DOES NOT COMPILE - COMMENTED OUT) ---`.
