"""
Foundations for AI & ML
Chapter 10: Conditional Probability and Bayes' Theorem
Section: Probability & Statistics

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/conditional-probability-and-bayes-theorem

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
p_sick        = 0.001          # prior
p_pos_if_sick = 0.99           # likelihood (sensitivity)
p_pos_if_well = 0.05           # false-positive rate

# law of total probability: the evidence P(+)
p_pos = p_pos_if_sick * p_sick + p_pos_if_well * (1 - p_sick)

# Bayes' theorem
p_sick_given_pos = (p_pos_if_sick * p_sick) / p_pos
print(round(p_sick_given_pos, 4))   # 0.0194
