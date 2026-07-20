"""
Claude Certified Architect (CCAF)
Chapter 25: Error Propagation and Partial Results
Section: Agentic Architecture and Orchestration (Domain 1)

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/error-propagation-partial-results

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# results = await gather(*[run_subagent(topic) for topic in subtopics])
# report = synthesize(results)   # assumes every result is present and valid

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# async def run_leg(topic):
#     try:
#         findings = await run_subagent(topic)
#         return {"topic": topic, "ok": True, "findings": findings}
#     except Exception as e:
#         return {"topic": topic, "ok": False, "error": classify(e), "topic_hint": topic}
#
# legs = await gather(*[run_leg(t) for t in subtopics])   # never raises
# done  = [r for r in legs if r["ok"]]
# failed = [r for r in legs if not r["ok"]]

# --- block 3 ---
report = {
    "findings": synthesize([r["findings"] for r in done]),
    "coverage": {"requested": len(subtopics), "returned": len(done)},
    "gaps": [{"topic": r["topic_hint"], "reason": r["error"]} for r in failed],
    "confidence": len(done) / len(subtopics),   # 4/5 = 0.8
}
