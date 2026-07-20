"""
Generative AI Fundamentals
Chapter 26: Designing Reliable Agents
Section: Agents & LangChain

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/designing-reliable-agents

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def run_agent(question, tools, max_steps=8):
    messages = [{"role": "user", "content": question}]
    seen = {}                                     # (tool, args) -> count
    for step in range(max_steps):                 # GUARD 1: hard step cap
        reply = model(messages)
        if reply.is_final_answer:
            return {"answer": reply.answer, "steps": step + 1}
        sig = (reply.tool, reply.args)
        seen[sig] = seen.get(sig, 0) + 1
        if seen[sig] >= 3:                         # GUARD 2: loop detection
            return {"answer": "Stuck: repeated the same action 3×.",
                    "stopped": "loop"}
        result = tools[reply.tool].run(reply.args)
        messages.append(reply.text)
        messages.append(f"Observation: {result}")
    return {"answer": "Ran out of steps.", "stopped": "budget"}   # GUARD 1 fires

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# budget_tokens, spent = 20_000, 0
# # ... inside the loop, after each model call:
# spent += reply.input_tokens + reply.output_tokens
# if spent > budget_tokens:                     # GUARD 3: hard cost ceiling
#     return {"answer": "Stopped: token budget exceeded.", "stopped": "cost"}

# --- block 3 ---
result = run_tool(reply.tool, reply.args)   # wraps validate + try/except

def run_tool(name, args):
    if name not in tools:                              # bad tool name
        return f"Error: no tool '{name}'. Have: {list(tools)}."
    if not tools[name].validate(args):                 # bad arguments
        return f"Error: '{name}' rejected args {args}."
    try:
        return tools[name].run(args)                   # real call, guarded
    except Exception as e:
        return f"Error running {name}: {e}"            # crash → observation, not death
