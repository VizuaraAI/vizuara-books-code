"""
AI Agents Bootcamp
Chapter 26: Coordination, Cost, and Failure Modes
Section: Multi-Agent Systems and Browser Agents

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/coordination-and-failure-modes

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
writer = None    # TODO: a writer agent, e.g. a crewai Agent (see Chapter 36).
critic = None    # TODO: a critic agent that reviews the draft.
task = ""        # TODO: the writing brief you hand the writer.
MAX_ROUNDS = 3   # the hard cap the book suggests in the comment below
# --- end fixups ---

# --- block 1 ---
draft = writer.run(task)
while True:                       # ← no exit condition
    critique = critic.run(draft)
    draft = writer.run(draft, critique)   # 2 LLM calls every lap, forever

# --- block 2 ---
draft = writer.run(task)
for round in range(MAX_ROUNDS):          # hard cap: e.g. 3
    critique = critic.run(draft)
    if critique.is_empty():              # content exit
        break
    draft = writer.run(draft, critique)
