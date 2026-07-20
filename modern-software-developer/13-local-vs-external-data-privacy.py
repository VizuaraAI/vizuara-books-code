"""
The Modern Software Developer
Chapter 13: Local vs. External Data & Privacy Boundaries
Section: MCP Servers: Reusable Integrations

Read this chapter: https://books.vizuara.ai/read/modern-software-developer/local-vs-external-data-privacy

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# A LOCAL tool: reads a ticket, but redacts anything secret-shaped
SECRET_FIELDS = {"stripe_api_key", "password", "ssn"}

def read_ticket(id: int) -> dict:
    row = db.fetch_ticket(id)              # stays on this machine
    return {k: v for k, v in row.items()  # never returns a secret field
            if k not in SECRET_FIELDS}

# --- block 2 ---
# An EXTERNAL tool: the ONE place data leaves your control
def post_to_slack(channel: str, text: str) -> dict:
    scrub(text)          # raise if text still matches any secret pattern
    log_egress(channel, len(text))        # every crossing is recorded
    return slack.post(channel, text)      # crosses the boundary here
