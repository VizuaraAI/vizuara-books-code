"""
Harness Engineering
Chapter 10: Streaming responses into a terminal
Section: The Agent Loop

Read this chapter: https://books.vizuara.ai/read/harness-engineering/streaming-responses

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo: imports & stubs (added to make this file runnable) ---
# 2. names the BOOK defines in another chapter. context.py holds those
#    definitions copied verbatim from the chapter that introduces them.
from context import client, SYSTEM_PROMPT, TOOLS, run_tool

# 3. names this chapter refers to but the book never defines. They are
#    stubbed - honestly - so the file imports and static-checks; the
#    reader supplies the real thing.
to_tool_results = None  # TODO: turn tool outputs into tool_result blocks
# --- end companion-repo additions ---

# --- block 1 ---
def call_model_stream(messages, tools):
    # yields raw events; the with-block also builds a final message for us
    with client.messages.stream(
        model="claude-sonnet-4-5",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=messages,
        tools=tools,
    ) as stream:
        for event in stream:
            yield event
        # a sentinel dict so the caller can't confuse it with a real SDK event
        yield {"__final__": stream.get_final_message()}   # the assembled reply

# --- block 2 ---
def run_agent(user_request, ui):
    messages = [{"role": "user", "content": user_request}]
    while True:
        reply = None
        for event in call_model_stream(messages, TOOLS):
            if isinstance(event, dict):                  # sentinel: fully assembled
                reply = event["__final__"]
            elif event.type == "content_block_start" and \
                 event.content_block.type == "tool_use":
                ui.on_tool_start(event.content_block.name)   # 1. show the call, live
            elif event.type == "content_block_delta":
                d = event.delta
                if d.type == "text_delta":
                    ui.on_text(d.text)                        # 2. print tokens as they land
                elif d.type == "input_json_delta":
                    ui.on_tool_args(d.partial_json)          # 3. optional: show args filling in

        messages.append({"role": "assistant", "content": reply.content})
        if reply.stop_reason != "tool_use":              # 4. no tool → we're done
            return
        # run the tools exactly as before — the args are now complete, valid JSON
        results = [run_tool(b.name, b.input) for b in reply.content
                   if b.type == "tool_use"]
        messages.append({"role": "user", "content": to_tool_results(results, reply)})

# --- block 3 ---
class TerminalUI:
    def on_text(self, chunk):
        print(chunk, end="", flush=True)          # flush is the whole point

    def on_tool_start(self, name):
        print(f"\n\033[2m→ {name}(…)\033[0m", flush=True)   # dim, live

    def on_tool_result(self, name, ok):
        mark = "✓" if ok else "✗"
        print(f"\033[2m  {mark} {name}\033[0m", flush=True)
