"""
AI Agents Bootcamp
Chapter 14: Build a ReAct Agent From Scratch
Section: Reasoning, Tools, and the Agent Loop

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/build-a-react-agent-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def calc(expression: str) -> str:
    """Evaluate a basic arithmetic expression, e.g. '48 * 12'."""
    allowed = set("0123456789+-*/(). ")
    if not set(expression) <= allowed:          # reject anything but arithmetic
        return "Error: expression contains illegal characters."
    return str(eval(expression))                # toy-only; see the sidenote

POP = {"france": 68_000_000, "japan": 125_000_000}
def population(country: str) -> str:
    """Look up a country's population."""
    return str(POP.get(country.strip().lower(), "unknown country"))

TOOLS = {"calc": calc, "population": population}

# --- block 2 ---
import re

ACTION_RE = re.compile(r'Action\s*\d*:\s*(\w+)\("(.*)"\)')

def parse_action(text: str):
    """Find the last 'Action N: name("arg")' line and split it."""
    match = None
    for match in ACTION_RE.finditer(text):
        pass                        # keep the LAST match, in case of stray lines
    if match is None:
        return None, None
    return match.group(1), match.group(2)   # ('calc', '48 * 12')

# --- block 3 ---
SYSTEM = """Answer the question by reasoning in steps. Each step, write:
Thought <n>: <your reasoning>
Action <n>: <tool>("<argument>")
Then STOP and wait for an Observation.
Available tools:
- calc("<arithmetic>")      e.g. calc("48 * 12")
- population("<country>")   e.g. population("France")
When you have the final answer, write:
Action <n>: finish("<the answer>")"""

def run_agent(question, model, max_steps=6):
    buffer = f"{SYSTEM}\n\nQuestion: {question}\n"
    for step in range(1, max_steps + 1):
        # 1. THINK + PROPOSE — model continues the buffer, we cut it at Observation
        reply = model(buffer + f"Thought {step}:", stop=["Observation"])
        buffer += f"Thought {step}:{reply}"

        name, arg = parse_action(reply)          # 2. PARSE the action line
        if name == "finish":                     # 3. STOP — model says it's done
            return arg
        if name is None or name not in TOOLS:    # 4. RECOVER from a bad action
            obs = f"Error: could not parse a valid Action. Use tool(\"arg\")."
        else:
            obs = TOOLS[name](arg)               # 5. ACT — run the real tool HERE
        buffer += f"\nObservation {step}: {obs}\n"   # 6. OBSERVE — report back
    return "Stopped: hit the step budget without finishing."
