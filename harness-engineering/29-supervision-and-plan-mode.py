"""
Harness Engineering
Chapter 29: Supervision & plan mode
Section: Durability, Recovery & Orchestration

Read this chapter: https://books.vizuara.ai/read/harness-engineering/supervision-and-plan-mode

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo: imports & stubs (added to make this file runnable) ---
# 3. names this chapter refers to but the book never defines. They are
#    stubbed - honestly - so the file imports and static-checks; the
#    reader supplies the real thing.
run_in_parallel = None    # TODO: map a function over ready steps concurrently
dispatch_subagent = None  # TODO: start a sub-agent for one plan step (Ch. 28)
synthesize = None         # TODO: supervisor writes the final answer from step summaries
# --- end companion-repo additions ---

# --- block 1 ---
PLAN_SCHEMA = {
    "type": "object",
    "properties": {
        "goal": {"type": "string"},
        "steps": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id":          {"type": "string"},
                    "description": {"type": "string"},
                    "agent_type":  {"type": "string"},   # which sub-agent runs it
                    "depends_on":  {"type": "array", "items": {"type": "string"}},
                    "read_only":   {"type": "boolean"},
                },
                "required": ["id", "description", "agent_type", "depends_on"],
            },
        },
    },
    "required": ["goal", "steps"],
}

# --- block 2 ---
def execute_plan(plan, approved_by_human):
    if not approved_by_human:
        return "plan rejected — nothing executed"

    done = {}                                   # step id -> summary it returned
    remaining = list(plan["steps"])

    while remaining:
        # a step is runnable once all its dependencies have finished
        ready = [s for s in remaining
                 if all(dep in done for dep in s["depends_on"])]

        # dispatch every ready step AT ONCE — they don't depend on each other
        results = run_in_parallel(
            lambda s: dispatch_subagent(s["agent_type"], s["description"]),
            ready,
        )
        for step, summary in zip(ready, results):
            done[step["id"]] = summary          # only the summary comes back
            remaining.remove(step)

    return synthesize(plan["goal"], done)       # supervisor writes the final answer
