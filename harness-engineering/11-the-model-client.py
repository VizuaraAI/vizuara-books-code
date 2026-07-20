"""
Harness Engineering
Chapter 11: The model client & provider abstraction
Section: The Agent Loop

Read this chapter: https://books.vizuara.ai/read/harness-engineering/the-model-client

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo: imports & stubs (added to make this file runnable) ---
# 2. names the BOOK defines in another chapter. context.py holds those
#    definitions copied verbatim from the chapter that introduces them.
from context import SYSTEM_PROMPT, TOOLS

# 3. names this chapter refers to but the book never defines. They are
#    stubbed - honestly - so the file imports and static-checks; the
#    reader supplies the real thing.
Reply = None             # TODO: the normalised reply dataclass this chapter describes
to_openai_tools = None   # TODO: translate Anthropic tool schemas to OpenAI's shape
normalize_openai = None  # TODO: translate an OpenAI response into the Reply shape
text_of = None           # TODO: the book never defines it; return the reply's plain text
# --- end companion-repo additions ---

# --- block 1 ---
import os, time, json, anthropic, openai

class ModelClient:
    def __init__(self, config_path="models.json"):
        cfg = json.load(open(config_path))
        self.models  = cfg["models"]
        self.default = cfg["default"]
        self._anthropic = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        self._openai    = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def send(self, messages, tools, model=None, system=""):
        spec = self.models[model or self.default]        # resolve the config entry
        adapter = getattr(self, f"_send_{spec['provider']}")
        return self._with_retries(lambda: adapter(spec, messages, tools, system))

    # ---- provider adapters: the ONLY provider-specific code in the whole harness ----
    def _send_anthropic(self, spec, messages, tools, system):
        r = self._anthropic.messages.create(
            model=spec["model"], max_tokens=spec["max_tokens"],
            system=system, messages=messages, tools=tools,
        )
        return Reply(stop_reason=r.stop_reason, content=r.content,
                     usage=(r.usage.input_tokens, r.usage.output_tokens))

    def _send_openai(self, spec, messages, tools, system):
        msgs = [{"role": "system", "content": system}, *messages]
        r = self._openai.chat.completions.create(
            model=spec["model"], max_tokens=spec["max_tokens"],
            messages=msgs, tools=to_openai_tools(tools),
        )
        return normalize_openai(r)                        # → the SAME Reply shape

    def _with_retries(self, fn, tries=5):
        for i in range(tries):
            try:
                return fn()
            except anthropic.APIStatusError as e:
                # retry only what's worth retrying: 429, 529, and transient 5xx.
                # a 400/401/404 will never fix itself — surface it immediately.
                if e.status_code not in (429, 529) and e.status_code < 500:
                    raise
                if i == tries - 1:
                    raise
                time.sleep(2 ** i)                        # 1, 2, 4, 8, 16s backoff

    def count_tokens(self, messages, model=None):
        spec = self.models[model or self.default]
        # provider-specific; anthropic exposes a dedicated endpoint
        return self._anthropic.messages.count_tokens(
            model=spec["model"], messages=messages).input_tokens

# --- block 2 ---
client = ModelClient()          # reads models.json once

def run_agent(user_request, model=None):
    messages = [{"role": "user", "content": user_request}]
    while True:
        reply = client.send(messages, TOOLS, model=model, system=SYSTEM_PROMPT)
        messages.append({"role": "assistant", "content": reply.content})
        if reply.stop_reason != "tool_use":
            return text_of(reply)
        # ... run tools, append tool_results, loop — exactly as before
