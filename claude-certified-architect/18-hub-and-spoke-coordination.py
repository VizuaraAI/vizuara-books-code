"""
Claude Certified Architect (CCAF)
Chapter 18: Hub-and-Spoke Coordination
Section: Agentic Architecture and Orchestration (Domain 1)

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/hub-and-spoke-coordination

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# The coordinator's single response fans out five subagents at once.
companies = ["Acme", "Bolt", "Cove", "Dyne", "Echo"]

for name in companies:
    Task(
        description=f"Extract 10-seat pricing for {name}",
        prompt=(
            f"Visit {name}'s pricing page. Return JSON: "
            f'{{"company": "{name}", "monthly_usd_10_seats": <number|null>, '
            f'"source_url": <string>}}. '
            f"If 10-seat pricing is not listed, return null for the price."
        ),
    )
# All five Task calls issued in ONE coordinator response => they run in parallel.
