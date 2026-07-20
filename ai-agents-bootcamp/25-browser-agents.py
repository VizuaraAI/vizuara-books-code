"""
AI Agents Bootcamp
Chapter 25: Browser Agents: Giving Agents Eyes and Hands
Section: Multi-Agent Systems and Browser Agents

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/browser-agents

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
from context import parse_action   # Chapter 14 defines this parser verbatim

build_map = None      # TODO: turns a live page into a labelled a11y map or a
#                       marked screenshot. Depends on your browser driver.
run_in_browser = None  # TODO: performs a real click/type/scroll on the page.
history = []          # TODO: the running record of past steps. The chapter's
#                       excerpt passes it to the model but never appends to it.
# --- end fixups ---

# --- block 1 ---
def browser_agent(task, page, model, max_steps=15):
    for step in range(max_steps):
        obs = build_map(page)          # 1. a11y tree OR marked screenshot → labels
        text = model(task, obs, history)          # 2. THINK: model reads the map
        action, args = parse_action(text)         # 3. e.g. ("click", [2])

        if action == "finish":
            return args[0]

        run_in_browser(page, action, args)        # 4. ACT: real click/type/scroll
        # 5. the page has now CHANGED — next loop rebuilds the map from scratch
    return "Gave up: step budget exhausted."
