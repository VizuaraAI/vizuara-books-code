"""
AI Agents Bootcamp
Chapter 8: Prompting: The Agent's Control Surface
Section: The Engine: Large Language Models

Read this chapter: https://books.vizuara.ai/read/ai-agents-bootcamp/prompting-the-agents-control-surface

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# Call A
messages = [
    {"role": "system", "content": "You are a terse assistant. Answer in one word."},
    {"role": "user",   "content": "What is the capital of France?"},
]
# → "Paris"

# Call B
messages = [
    {"role": "system", "content": "You are a patient geography tutor for 8-year-olds. "
                                   "Always explain with a fun fact."},
    {"role": "user",   "content": "What is the capital of France?"},
]
# → "The capital of France is Paris! Fun fact: it has a giant iron tower
#    called the Eiffel Tower that was once the tallest building on Earth. 🗼"
