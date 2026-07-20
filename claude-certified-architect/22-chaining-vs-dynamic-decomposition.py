"""
Claude Certified Architect (CCAF)
Chapter 22: Prompt Chaining vs Dynamic Decomposition
Section: Agentic Architecture and Orchestration (Domain 1)

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/chaining-vs-dynamic-decomposition

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# PROMPT CHAINING — the steps are literally your code
category = classify(email)                 # call 1: narrow prompt
severity = assess_severity(email, category)  # call 2: uses call 1's output
reply    = draft_reply(email, category, severity)  # call 3
record   = {"category": category, "severity": severity, "reply": reply}

# --- block 2 ---
# DYNAMIC DECOMPOSITION — the model decides the steps
messages = [{"role": "user", "content": whole_job}]
while True:
    resp = client.messages.create(model=MODEL, tools=TOOLS, messages=messages)
    messages.append({"role": "assistant", "content": resp.content})
    if resp.stop_reason == "end_turn":     # the model decided it's done
        break
    run_tools_and_append(resp, messages)   # it asked for a tool; you run it, loop again
