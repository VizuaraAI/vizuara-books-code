"""
AI Agents Bootcamp
Chapter 23: Multi-Agent Architectures: Managers and Workers
Section: Multi-Agent Systems and Browser Agents

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/multi-agent-architectures

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
plan = None        # TODO: the manager's planning step - Chapter 24 builds a real
#                    one (`make_plan`).
synthesize = None  # TODO: the manager's synthesis step - Chapter 24 builds a real
#                    one, inline in `run_team`.
# --- end fixups ---

# --- block 1 ---
def orchestrator(request, workers):
    # 1. manager decides which workers to call and with what brief
    subtasks = plan(request)          # {"flights": "...", "hotel": "...", "food": "..."}

    # 2. delegate — each worker is an agent, but called like a function
    results = {}
    for name, brief in subtasks.items():
        results[name] = workers[name].run(brief)   # independent agent, own context

    # 3. synthesize the pieces into one answer
    return synthesize(request, results)
