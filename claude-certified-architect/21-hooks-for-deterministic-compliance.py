"""
Claude Certified Architect (CCAF)
Chapter 21: Hooks for Deterministic Compliance
Section: Agentic Architecture and Orchestration (Domain 1)

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/hooks-for-deterministic-compliance

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# .claude/hooks/block_destructive.py  — runs on every Bash tool call
import json, sys

data = json.load(sys.stdin)              # the pending tool call
cmd  = data["tool_input"].get("command", "")

BANNED = ["rm -rf", "git push --force", ":(){", "mkfs"]
hit = next((b for b in BANNED if b in cmd), None)

if hit:
    print(json.dumps({
        "decision": "block",
        "reason": f"Blocked by policy: command contains '{hit}'."
    }))
    sys.exit(0)
# no output + exit 0  => allow the call through
