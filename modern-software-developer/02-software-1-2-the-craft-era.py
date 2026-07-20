"""
The Modern Software Developer
Chapter 2: Software 1.2: The Hand-Coded Craft Era
Section: The New Era of Software Development

Read this chapter: https://books.vizuara.ai/read/modern-software-developer/software-1-2-the-craft-era

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def validate_email(address: str) -> tuple[bool, str]:
    if "@" not in address:
        return False, "Missing an @ sign — that's not an email."
    local, _, domain = address.partition("@")
    if not local or "." not in domain:
        return False, "That doesn't look like a complete address."
    return True, ""
