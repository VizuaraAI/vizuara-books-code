"""
Generative AI Fundamentals
Chapter 23: Code Your First LLM Agent
Section: Agents & LangChain

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/code-your-first-llm-agent

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def calculator(expr: str) -> str:
    # eval is fine ONLY for a trusted, digits-and-operators sandbox
    return str(eval(expr, {"__builtins__": {}}, {}))

def weather(city: str) -> str:
    fake = {"Reykjavik": "3°C, light snow", "Chennai": "34°C, humid"}
    return fake.get(city.strip(), "unknown city")

TOOLS = {"calc": calculator, "weather": weather}

# --- block 2 ---
SYSTEM = """Answer the question. You may use tools.
On each step write EITHER:
  Thought: <reasoning>
  Action: <calc|weather>[<input>]
OR, when you are done:
  Thought: <reasoning>
  Final Answer: <answer>
After an Action, wait — I will reply with an Observation."""

# --- block 3 ---
import re

def run_agent(question, model, max_steps=6):
    transcript = f"Question: {question}\n"
    for step in range(max_steps):
        reply = model(SYSTEM + "\n" + transcript)   # 1. call the LLM
        transcript += reply + "\n"
        if "Final Answer:" in reply:                 # 2. done?
            return reply.split("Final Answer:")[-1].strip()
        m = re.search(r"Action:\s*(\w+)\[(.*?)\]", reply)  # 3. tool call?
        if not m:
            transcript += "Observation: no valid action.\n"
            continue
        name, arg = m.group(1), m.group(2)
        result = TOOLS[name](arg)                    # 4. RUN the tool
        transcript += f"Observation: {result}\n"     # 5. feed result back
    return "stopped: hit max_steps"

# --- block 4 ---
from langchain.agents import tool, create_react_agent, AgentExecutor

@tool
def calc(expr: str) -> str:
    "Evaluate a math expression."
    return str(eval(expr, {"__builtins__": {}}, {}))

# tools=[calc, weather] → create_react_agent(llm, tools, prompt)
# AgentExecutor(agent=..., tools=..., max_iterations=6).invoke({"input": q})
