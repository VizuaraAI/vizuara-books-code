"""
The Modern Software Developer
Chapter 10: Building Your First Claude Skill
Section: Coding Agents & Claude Code

Read this chapter: https://books.vizuara.ai/read/modern-software-developer/building-your-first-skill

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import sys, csv, pathlib

folder = pathlib.Path(sys.argv[1])
for path in sorted(folder.glob("*.csv")):
    with open(path) as f:
        rows = list(csv.reader(f))
    header, body = rows[0], rows[1:]
    print(f"{path.name}: {len(body)} rows, {len(header)} cols "
          f"({', '.join(header)})")
