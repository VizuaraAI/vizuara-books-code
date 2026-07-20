"""
Writing Journal & Conference Papers
Chapter 22: Finding the Thread of Your Paper
Section: Reading the Literature

Read this chapter: https://books.vizuara.ai/read/writing-research-papers/finding-the-thread-of-your-paper

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# You are NOT sorting papers by date or author.
# You are sorting your OWN clusters into an argument.

clusters = group_papers_by(role)          # define / apply / limit / fix / survey
arc      = order(clusters, by="problem -> gap -> solution")

thread = []
for stage in arc:                          # each stage becomes a body section
    claim   = one_sentence_summary(stage)  # "PINNs break down in turbulent regimes"
    support = [p for p in papers if p.cluster == stage]   # citations that substantiate it
    thread.append((claim, support))        # a claim, backed by papers = a section
