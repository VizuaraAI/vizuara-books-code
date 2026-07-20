"""
Generative AI Fundamentals
Chapter 21: What Is an LLM Agent?
Section: Agents & LangChain

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/what-is-an-llm-agent

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def run_agent(user_question, tools, max_steps=6):
    messages = [{"role": "user", "content": user_question}]
    for _ in range(max_steps):              # the loop — this is the agent
        reply = model(messages)             # THOUGHT + (ACTION or FINAL ANSWER)
        if reply.is_final_answer:
            return reply.answer             # model chose to answer → stop
        result = tools[reply.tool].run(reply.args)   # OBSERVATION: run it for real
        messages.append(reply.text)                  # remember what it decided
        messages.append(f"Observation: {result}")    # feed the real result back
    return "Stopped: hit the step limit."   # a guardrail against infinite loops
