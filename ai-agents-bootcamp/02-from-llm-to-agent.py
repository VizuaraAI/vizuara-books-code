"""
AI Agents Bootcamp
Chapter 2: From LLM to Agent
Section: What Is an AI Agent?

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/from-llm-to-agent

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
from context import parse_action   # Chapter 14 defines this parser verbatim

SYSTEM_PROMPT = ""  # TODO: the agent's system prompt. The chapter describes it in
#                     prose rather than printing it - see the chapter link above.
# --- end fixups ---

# --- block 1 ---
def run_agent(user_goal, tools, model, max_steps=8):
    # `tools` maps a name -> a plain Python function.
    history = SYSTEM_PROMPT + f"\nUser: {user_goal}\n"

    for step in range(max_steps):          # 1. THE LOOP
        reply = model(history)             # 2. the model thinks + proposes ONE action
        history += reply

        if "Answer:" in reply:             # the model decided it's done
            return reply.split("Answer:")[-1].strip()

        name, arg = parse_action(reply)    # 3. did it ask to ACT? e.g. calculator("4817*2913")
        result = tools[name](arg)          # 4. WE run the tool, outside the model
        history += f"\nObservation: {result}\n"   # 5. OBSERVE: feed the result back in

    return "stopped: hit step limit"
