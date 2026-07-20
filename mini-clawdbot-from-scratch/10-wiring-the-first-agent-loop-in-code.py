"""
Build a Mini ClawdBot from Scratch
Chapter 10: Wiring the First Agent Loop in Code
Section: Foundations of an AI Agent

Read this chapter: https://books.vizuara.ai/read/mini-clawdbot-from-scratch/wiring-the-first-agent-loop-in-code

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def run_agent(user_message, tools, tool_impls, system_prompt):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user",   "content": user_message},
    ]

    while True:                                   # the agent loop
        response = llm.chat(messages, tools=tools)   # 1. THINK: call the model
        messages.append(response.message)            #    remember what it said

        if not response.message.tool_calls:          # no tool wanted?
            return response.message.content          #    → we're done, return text

        for call in response.message.tool_calls:     # 2. ACT: run each requested tool
            fn = tool_impls[call.name]
            result = fn(**call.arguments)            #    execute the REAL function
            messages.append({                        # 3. OBSERVE: feed the result back
                "role": "tool",
                "tool_call_id": call.id,
                "content": str(result),
            })
        # loop back around → the model sees the results and decides what's next

# --- block 2 ---
try:
    result = fn(**call.arguments)
except Exception as e:
    result = f"Error: {e}"      # hand the failure back, don't crash the loop
