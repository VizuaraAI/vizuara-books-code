"""
Claude Certified Architect (CCAF)
Chapter 26: Lab: Multi-Agent Research Pipeline
Section: Agentic Architecture and Orchestration (Domain 1)

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/lab-multi-agent-research-pipeline

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
question = "Is the Message Batches API worth using for a nightly report job?"

subtasks = [
    ("pricing",   "How does Batches API pricing compare to real-time?"),
    ("latency",   "What is the turnaround window for the Batches API?"),
    ("failures",  "What failure modes and retry semantics does it have?"),
]

# ONE coordinator response emits all three Task calls -> they run in parallel.
tasks = [
    Task(
        subagent_type="researcher",
        prompt=(
            f"RESEARCH QUESTION (for context): {question}\n"
            f"YOUR SLICE: {slice_q}\n"
            "Return ONLY claim-source pairs. Each claim must cite exactly one source. "
            "If you cannot verify a claim, set source to null and confidence to 'low'."
        ),
    )
    for _tag, slice_q in subtasks
]

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# results = gather(tasks)   # some may be Ok(findings), some Err(reason)
#
# report, failures = [], []
# for tag, r in zip(["pricing", "latency", "failures"], results):
#     if r.ok:
#         report.extend(r.findings)          # keep the good claims
#     else:
#         failures.append((tag, r.reason))   # record, do not raise
#
# return {
#     "findings": report,                    # partial but real
#     "degraded": bool(failures),            # tell the caller it is incomplete
#     "missing": [tag for tag, _ in failures],
# }
