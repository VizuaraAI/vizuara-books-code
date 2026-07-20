"""
Build Decision Trees from Scratch
Chapter 23: From One Tree to Forests and Boosting
Section: Wrap-Up and Interview Prep

Read this chapter: https://books.vizuara.ai/read/decision-trees-from-scratch/from-trees-to-forests

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# Gradient boosting, the core loop, on one sample with true value y = 50
pred = 40.0          # tree 0: just the mean
eta  = 0.1           # learning rate (shrinkage)

residual = 50 - pred          # = 10.0   -> what tree 1 must learn
tree1_out = 9.0               # tree 1 predicts ~9 for this residual
pred += eta * tree1_out       # 40 + 0.1*9 = 40.9

residual = 50 - pred          # = 9.1    -> smaller! now tree 2's target
tree2_out = 8.0
pred += eta * tree2_out       # 40.9 + 0.1*8 = 41.7
# ... hundreds of trees later, pred creeps toward 50
