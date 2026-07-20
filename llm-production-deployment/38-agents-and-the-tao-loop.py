"""
LLM Production & Deployment
Chapter 38: Agents & the TAO Loop
Section: Agents & Memory

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/agents-and-the-tao-loop

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
system_prompt = None  # TODO: renders the tool descriptions into a system message.
user = None           # TODO: wraps the goal as a user message.
observation = None    # TODO: wraps a tool result as an observation message.
# --- end fixups ---

# --- block 1 ---
def run_agent(goal, tools, model, max_steps=6):
    context = [system_prompt(tools), user(goal)]   # tools described here
    for _ in range(max_steps):
        out = model(context)                        # one Thought + Action
        if out.is_final_answer:
            return out.answer                       # loop exit condition
        result = tools[out.tool_name](**out.args)   # ACT: run the chosen tool
        context.append(out)                         # record the action
        context.append(observation(result))         # OBSERVE: feed result back
    return "stopped: hit max_steps"                 # safety cap
