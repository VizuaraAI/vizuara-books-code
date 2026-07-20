"""
AI Agents Bootcamp
Chapter 16: Why Agent Frameworks Exist
Section: Frameworks I: LangChain and Smolagents

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/why-frameworks-exist

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
from context import parse_action   # Chapter 14 defines this parser verbatim

SYSTEM_PROMPT = ""  # TODO: the system prompt for your loop.
MAX_STEPS = 6       # TODO: your step budget. The book's own ReAct agent in
#                     Chapter 14 uses 6.
call_llm = None     # TODO: your one-call-to-the-model helper - Chapter 9 builds
#                     a real one.
# --- end fixups ---

# --- block 1 ---
def run_agent(question, tools):
    messages = [{"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question}]
    for step in range(MAX_STEPS):          # 1. the loop, capped so it can't run forever
        reply = call_llm(messages)          # 2. one model call
        action = parse_action(reply)        # 3. pull "Action: search[...]" out of free text
        if action is None:
            return reply                    # model gave a final answer
        result = tools[action.name](action.args)   # 4. run the tool
        messages.append({"role": "assistant", "content": reply})
        messages.append({"role": "user", "content": f"Observation: {result}"})  # 5. feed it back
    raise RuntimeError("agent did not finish")   # 6. what if it never stops?
