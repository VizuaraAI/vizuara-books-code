"""
AI Agents Bootcamp
Chapter 5: Setup: API Keys and Your Environment
Section: What Is an AI Agent?

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/setup-keys-and-environment

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from google.colab import userdata
import os

# read the secret out of Colab's vault into a normal env var
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# !pip -q install google-generativeai
#
# import os, google.generativeai as genai
#
# genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
# model = genai.GenerativeModel("gemini-1.5-flash")
# resp = model.generate_content("In one sentence, what is an AI agent?")
# print(resp.text)
