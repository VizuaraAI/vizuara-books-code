"""
AI Agents Bootcamp
Chapter 11: ReAct: Interleaving Reasoning and Acting
Section: Reasoning, Tools, and the Agent Loop

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/the-react-pattern

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
from context import parse_action   # Chapter 14 defines this parser verbatim
# --- end fixups ---

# --- block 1 ---
def react(question, tools, model, max_steps=8):
    transcript = f"Question: {question}\n"
    for step in range(max_steps):
        # 1. THINK + PROPOSE: model continues the transcript with a
        #    Thought and one Action line, then we stop it.
        text = model(transcript + f"Thought {step+1}:", stop=["Observation"])
        transcript += f"Thought {step+1}:{text}"

        action, arg = parse_action(text)      # 2. PARSE the "name(arg)" line
        if action == "finish":                # 3. STOP when the model is done
            return arg

        result = tools[action](arg)           # 4. ACT: run the real tool HERE
        transcript += f"\nObservation {step+1}: {result}\n"   # 5. OBSERVE
    return "No answer within step budget."
