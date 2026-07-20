"""
Claude Certified Architect (CCAF)
Chapter 13: Resilient Enum-Plus-Other Schemas
Section: Guaranteed Structured Output (Domain 4)

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/resilient-enum-schemas

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
tools = [{
    "name": "classify_ticket",
    "description": "Classify a support ticket into one category.",
    "input_schema": {
        "type": "object",
        "properties": {
            "category": {
                "type": "string",
                "enum": ["billing", "bug_report", "feature_request"]
            }
        },
        "required": ["category"]
    }
}]

# --- block 2 ---
tools = [{
    "name": "classify_ticket",
    "description": (
        "Classify a support ticket. If it does not clearly fit "
        "billing, bug_report, or feature_request, set category to "
        "'other' and describe the real category in category_other."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "category": {
                "type": "string",
                "enum": ["billing", "bug_report",
                         "feature_request", "other"]
            },
            "category_other": {
                "type": ["string", "null"],
                "description": "Free-text category when category='other', else null."
            }
        },
        "required": ["category", "category_other"]
    }
}]
