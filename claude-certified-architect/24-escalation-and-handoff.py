"""
Claude Certified Architect (CCAF)
Chapter 24: Escalation and Handoff Protocols
Section: Agentic Architecture and Orchestration (Domain 1)

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/escalation-and-handoff

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
handoff_tool = {
    "name": "handoff",
    "description": "Package the task so the next owner can resume, not restart.",
    "input_schema": {
        "type": "object",
        "properties": {
            "goal":            {"type": "string"},
            "state":           {"type": "string"},
            "ruled_out":       {"type": "array", "items": {"type": "string"}},
            "next_step":       {"type": "string"},
            "reason":          {"type": "string"},   # why control is changing hands
            "confidence":      {"type": "number", "minimum": 0, "maximum": 1},
            "artifacts":       {"type": "array", "items": {"type": "string"}},
            "needs_human":     {"type": "boolean"},   # escalation flag
        },
        "required": ["goal", "state", "ruled_out", "next_step", "reason",
                     "confidence", "needs_human"],
    },
}
