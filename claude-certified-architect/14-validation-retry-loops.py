"""
Claude Certified Architect (CCAF)
Chapter 14: Validation-Retry Loops With Error Feedback
Section: Guaranteed Structured Output (Domain 4)

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/validation-retry-loops

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# { "role": "user",      "content": "Extract the expense: 'Client dinner in Lisbon, €80'" }
# { "role": "assistant", "content": [ <the tool_use block Claude just produced> ] }
# { "role": "user",      "content": [ {
#       "type": "tool_result",
#       "tool_use_id": "toolu_01A...",          # must match the failed call
#       "is_error": True,
#       "content": "category: 'food' is not one of "
#                  "['travel','meals','lodging','other']. "
#                  "amount_usd must be a number in USD, not a string."
# } ] }

# --- block 2 ---
def extract_with_retry(client, user_text, tool, validate, max_retries=3):
    messages = [{"role": "user", "content": user_text}]
    for attempt in range(max_retries):
        resp = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            tools=[tool],
            tool_choice={"type": "tool", "name": tool["name"]},  # force our tool
            messages=messages,
        )
        block = next(b for b in resp.content if b.type == "tool_use")
        try:
            return validate(block.input)          # <- YOUR rules run here
        except ValidationError as e:
            messages.append({"role": "assistant", "content": resp.content})
            messages.append({"role": "user", "content": [{
                "type": "tool_result",
                "tool_use_id": block.id,
                "is_error": True,
                "content": str(e),               # the exact error, fed back
            }]})
    raise MaxRetriesExceeded(user_text)           # give up loudly, don't hang
