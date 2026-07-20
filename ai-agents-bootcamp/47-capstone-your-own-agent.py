"""
AI Agents Bootcamp
Chapter 47: Capstone: Design and Ship Your Own Agent
Section: From Agents to Products

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/capstone-your-own-agent

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
out = None  # TODO: block 2 below is a REVISION of `summarize_row`; it elides the
#             model call with `...`, so `out` is the response object created in
#             block 1.
# --- end fixups ---

# --- block 1 ---
import requests, re
from openai import OpenAI

client = OpenAI()  # or a free Gemini / HF key — see the setup chapter

def fetch_abstract(url: str) -> str:          # the ONE tool
    arxiv_id = re.search(r"(\d{4}\.\d{5})", url).group(1)
    r = requests.get(f"https://arxiv.org/abs/{arxiv_id}")
    return re.search(r'"og:description" content="(.*?)"', r.text).group(1)

def summarize_row(title_hint, abstract) -> str:
    prompt = (f"Abstract:\n{abstract}\n\n"
              "Return ONE line: | <title> | <what's new in <=15 words> | <easy|medium|hard> |")
    out = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return out.choices[0].message.content.strip()

def summarize(urls):                           # the fixed loop
    rows = ["| Paper | What's new | Level |", "|---|---|---|"]
    for u in urls:
        rows.append(summarize_row(u, fetch_abstract(u)))
    return "\n".join(rows)

# --- block 2 ---
def summarize_row(title_hint, abstract) -> str:
    ...
    text = out.choices[0].message.content.strip()
    match = re.search(r"\|.*\|.*\|.*\|", text)   # grab the table row, drop the chatter
    return match.group(0) if match else f"| {title_hint} | (parse failed) | ? |"
