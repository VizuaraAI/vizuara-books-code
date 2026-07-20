"""
Prompt Engineering
Chapter 21: Role and Persona Prompting
Section: Text-to-Text Techniques

Read this chapter: https://books.vizuara.ai/read/prompt-engineering/role-and-persona-prompting

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
messages = [
    {"role": "system",
     "content": "You are a senior pediatric nurse. You explain clearly to "
                "worried parents, flag red-flag symptoms, and never give a "
                "dosage without saying to confirm with a doctor."},
    {"role": "user",
     "content": "My 3-year-old has a fever of 39C. What should I do?"},
]
