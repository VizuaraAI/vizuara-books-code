"""
Build a Mini ClawdBot from Scratch
Chapter 1: What is ClawdBot?
Section: The ClawdBot Story

Read this chapter: https://books.vizuara.ai/read/mini-clawdbot-from-scratch/what-is-clawdbot

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
messages = [system_prompt, memory, rag_context, *history, user_question]

while True:
    reply = llm(messages, tools=all_tools)   # think
    if not reply.tool_calls:
        break                                 # no tool wanted → we're done
    for call in reply.tool_calls:
        result = run_tool(call)               # act
        messages.append(result)               # observe
    # loop back and let the model reason with the new results
