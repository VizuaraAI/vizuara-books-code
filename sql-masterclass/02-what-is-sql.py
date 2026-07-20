"""
SQL Masterclass
Chapter 2: What Is SQL? Declarative Queries vs Imperative Code
Section: Getting Started

Read this chapter: https://books.vizuara.ai/read/sql-masterclass/what-is-sql

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
result = []
for film in films:                 # 1. walk every row myself
    if film["rental_rate"] > 3.00: # 2. test each one
        result.append(film["title"])
result.sort()                      # 3. order the survivors
