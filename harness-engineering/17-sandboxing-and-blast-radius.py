"""
Harness Engineering
Chapter 17: Sandboxing & the blast-radius problem
Section: Tools & the Execution Environment

Read this chapter: https://books.vizuara.ai/read/harness-engineering/sandboxing-and-blast-radius

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo: imports & stubs (added to make this file runnable) ---
# 1. modules the chapter uses but does not import in its own blocks.
import subprocess

# 3. names this chapter refers to but the book never defines. They are
#    stubbed - honestly - so the file imports and static-checks; the
#    reader supplies the real thing.
args = None              # TODO: this block is a fragment of run_tool's body; args is its parameter
SEATBELT_PROFILE = None  # TODO: the macOS sandbox-exec profile string
CLEAN_ENV = None         # TODO: the env dict with secrets stripped out
# --- end companion-repo additions ---

# --- block 1 ---
r = subprocess.run(args["cmd"], shell=True, capture_output=True, text=True)

# --- block 2 ---
import pathlib

ROOT = pathlib.Path("/Users/you/project").resolve()

def safe_path(p: str) -> pathlib.Path:
    # resolve() collapses .. and follows symlinks to the real target
    full = (ROOT / p).resolve()
    if ROOT not in full.parents and full != ROOT:
        raise PermissionError(f"path escapes working dir: {p}")
    return full

# --- block 3 ---
def run_bash_sandboxed(cmd: str) -> str:
    return subprocess.run(
        [
            "sandbox-exec", "-p", SEATBELT_PROFILE,  # fs-confined to ROOT
            "bash", "-c", cmd,
        ],
        capture_output=True, text=True,
        # env stripped of secrets; no AWS_*, no API keys inherited
        env=CLEAN_ENV,
        timeout=120,                                  # runaway guard
    ).stdout
