"""
Harness Engineering
Chapter 16: Permission gates & approval modes
Section: Tools & the Execution Environment

Read this chapter: https://books.vizuara.ai/read/harness-engineering/permission-gates-and-approval-modes

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo: imports & stubs (added to make this file runnable) ---
# 2. names the BOOK defines in another chapter. context.py holds those
#    definitions copied verbatim from the chapter that introduces them.
from context import run_tool

# 3. names this chapter refers to but the book never defines. They are
#    stubbed - honestly - so the file imports and static-checks; the
#    reader supplies the real thing.
is_hard_denied = None  # TODO: the always-on deny list, checked in every mode
# --- end companion-repo additions ---

# --- block 1 ---
def check_permission(name, args):
    # 1. read-only tools are always safe — auto-allow
    if name in SAFE_TOOLS:                 # read_file, list_dir, grep …
        return "allow"

    # 2. some things are never OK, no matter who asks
    if name == "run_bash" and is_dangerous(args["cmd"]):
        return "deny"                      # rm -rf /, curl|bash, fork bombs

    # 3. everything else: stop and ask the human
    return "ask"

SAFE_TOOLS = {"read_file", "list_dir", "grep"}

def is_dangerous(cmd):
    patterns = ["rm -rf /", ":(){", "curl", "| sh", "| bash", "> /dev/sd"]
    return any(p in cmd for p in patterns)

# --- block 2 ---
def guarded_run_tool(name, args):
    verdict = check_permission(name, args)

    if verdict == "deny":
        return "BLOCKED: this action is not permitted."

    if verdict == "ask":
        print(f"\nClaude wants to run: {name}({args})")
        answer = input("  [y]es / [a]lways / [n]o: ").strip().lower()
        if answer == "a":
            SAFE_TOOLS.add(name)           # remember this choice for the session
        elif answer != "y":
            return "User declined. Do not retry; ask what they'd prefer."

    return run_tool(name, args)            # the real execution from Ch. 4

# --- block 3 ---
# the same policy, expressed as data instead of code
PERMISSIONS = {
    "allow": ["read_file", "list_dir", "grep", "run_bash(npm test:*)"],
    "deny":  ["run_bash(rm -rf /*)", "read_file(**/.env)", "run_bash(*curl*|*)"],
    # anything matching neither list falls through to "ask"
}

# --- block 4 ---
def check_permission(name, args, mode="ask"):
    if name in SAFE_TOOLS:
        return "allow"
    if is_hard_denied(name, args):
        return "deny"                      # <-- fires in EVERY mode, always

    if mode == "plan":
        return "deny"                      # read-only: refuse all mutations
    if mode == "auto":
        return "allow"                     # trust the agent, skip the prompt
    return "ask"                           # the sane default
