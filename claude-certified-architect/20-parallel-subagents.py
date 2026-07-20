"""
Claude Certified Architect (CCAF)
Chapter 20: Running Subagents in Parallel
Section: Agentic Architecture and Orchestration (Domain 1)

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/parallel-subagents

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# The coordinator, in ONE response, emits N independent Task calls.
competitors = ["Acme", "Globex", "Initech",
               "Umbra", "Hooli", "Stark"]

# Each Task is fully self-contained — the subagent sees ONLY this prompt.
tasks = [
    Task(
        subagent_type="researcher",
        prompt=(
            f"Profile the competitor '{c}'. "
            f"Return ONLY: {{name, one_line, top_3_products, "
            f"pricing_model, sources:[url]}}. "
            f"If a field is unknown, return null — do not guess."
        ),
    )
    for c in competitors
]
# All six go out together; the runtime runs them concurrently
# and returns all six tool_result blocks in the next turn.
