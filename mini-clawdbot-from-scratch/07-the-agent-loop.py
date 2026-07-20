"""
Build a Mini ClawdBot from Scratch
Chapter 7: The Agent Loop
Section: Foundations of an AI Agent

Read this chapter: https://books.vizuara.ai/read/mini-clawdbot-from-scratch/the-agent-loop

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def run_agent(messages, tools):
    while True:                                  # the loop
        response = call_llm(messages, tools)     # THINK
        messages.append(response.message)        # record what the model said

        if not response.tool_calls:              # STOP CONDITION
            return response.text                 # no tool asked → we're done

        for call in response.tool_calls:         # ACT
            result = run_tool(call.name, call.args)
            messages.append(tool_message(call.id, result))   # OBSERVE
        # loop back to THINK, now with a longer messages array
