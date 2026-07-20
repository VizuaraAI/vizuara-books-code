"""
Harness Engineering
Chapter 14: The core tools: read, write, edit, bash, search
Section: Tools & the Execution Environment

Read this chapter: https://books.vizuara.ai/read/harness-engineering/the-core-file-and-shell-tools

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo: imports & stubs (added to make this file runnable) ---
# 1. modules the chapter uses but does not import in its own blocks.
import subprocess

# --- end companion-repo additions ---

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import pathlib

# --- block 1 ---
def read_file(path, offset=0, limit=2000):
    lines = pathlib.Path(path).read_text().splitlines()
    window = lines[offset : offset + limit]
    # number every line so the model can refer to exact locations
    numbered = [f"{offset+i+1:>6}\t{ln}" for i, ln in enumerate(window)]
    return "\n".join(numbered)

# --- block 2 ---
def search(pattern, path=".", glob=None):
    cmd = ["rg", "--line-number", "--no-heading", pattern, path]
    if glob:
        cmd += ["--glob", glob]
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.stdout[:8000] or "no matches"

# --- block 3 ---
def edit_file(path, old_string, new_string):
    p = pathlib.Path(path)
    text = p.read_text()
    count = text.count(old_string)
    if count == 0:
        return "ERROR: old_string not found — read the file and copy it exactly."
    if count > 1:
        return f"ERROR: old_string matches {count} places — add surrounding lines to make it unique."
    p.write_text(text.replace(old_string, new_string))
    return "ok — 1 replacement"

# --- block 4 ---
def run_bash(cmd, timeout=120):
    r = subprocess.run(cmd, shell=True, capture_output=True,
                       text=True, timeout=timeout)
    return (r.stdout + r.stderr)[:8000] or "(no output)"
