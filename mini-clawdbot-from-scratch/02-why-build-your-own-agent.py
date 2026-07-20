"""
Build a Mini ClawdBot from Scratch
Chapter 2: Why Build Your Own Agent?
Section: The ClawdBot Story

Read this chapter: https://books.vizuara.ai/read/mini-clawdbot-from-scratch/why-build-your-own-agent

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
# messages = [system_prompt, user_message]
# while True:
#     reply = llm(messages, tools=all_tools)   # think
#     if not reply.tool_calls:                 # no tool wanted? we're done
#         return reply.text
#     for call in reply.tool_calls:            # act
#         result = run_tool(call.name, call.args)
#         messages.append(result)              # observe, then loop
