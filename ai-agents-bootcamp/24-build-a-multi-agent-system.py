"""
AI Agents Bootcamp
Chapter 24: Build a Multi-Agent System
Section: Multi-Agent Systems and Browser Agents

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/build-a-multi-agent-system

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
from context import parse_action   # "the same regex parser as before" (Chapter 14)
# --- end fixups ---

# --- block 1 ---
POP = {"france": 68_000_000, "japan": 125_000_000}
def population(country: str) -> str:
    """Look up a country's population."""
    return str(POP.get(country.strip().lower(), "unknown country"))

def research_worker(brief: str, model) -> str:
    """A focused agent: given a research brief, return the facts as text."""
    prompt = (
        "You are a research assistant. Use ONLY the population tool to get "
        "facts. When done, write: ANSWER: <the facts in one line>.\n"
        f"Tool: population(\"<country>\")\n\nBrief: {brief}\n"
    )
    for _ in range(4):                              # a small step budget
        reply = model(prompt, stop=["Observation:"])
        prompt += reply
        if "ANSWER:" in reply:
            return reply.split("ANSWER:", 1)[1].strip()
        name, arg = parse_action(reply)             # same regex parser as before
        obs = population(arg) if name == "population" else "Error: unknown tool."
        prompt += f"\nObservation: {obs}\n"
    return "research inconclusive"

# --- block 2 ---
def writer_worker(brief: str, model) -> str:
    """A focused agent: given a writing brief, return two sentences of prose."""
    prompt = (
        "You are a travel copywriter. Write EXACTLY two vivid sentences. "
        f"Do not add facts beyond the brief.\n\nBrief: {brief}"
    )
    return model(prompt).strip()

# --- block 3 ---
import json

def make_plan(request: str, model) -> list[dict]:
    """Manager step 1: turn a messy request into an ordered list of subtasks."""
    prompt = (
        "Break the user's request into subtasks for a team. Reply with ONLY a "
        "JSON list. Each item: {\"worker\": \"research\"|\"writer\", \"brief\": \"...\"}.\n"
        "The research worker gets facts; the writer worker writes prose from facts.\n\n"
        f"Request: {request}"
    )
    return json.loads(model(prompt))

# --- block 4 ---
WORKERS = {"research": research_worker, "writer": writer_worker}

def run_team(request: str, model) -> str:
    plan = make_plan(request, model)                 # 1. PLAN the delegation
    results = []
    for step in plan:                                # 2. DELEGATE, in order
        worker = WORKERS.get(step["worker"])
        if worker is None:                           # 3. RECOVER from a bad plan
            results.append(f"[skipped unknown worker: {step['worker']}]")
            continue
        brief = step["brief"]
        if results:                                  # pass prior results forward
            brief += "\n\nKnown so far:\n" + "\n".join(results)
        results.append(worker(brief, model))         # 4. run the worker as a "tool"

    synthesis_prompt = (                             # 5. SYNTHESISE into one answer
        "Combine these worker outputs into a single, direct answer to the user. "
        "Do not mention the workers.\n\n"
        f"User asked: {request}\n\nWorker outputs:\n" + "\n---\n".join(results)
    )
    return model(synthesis_prompt).strip()
