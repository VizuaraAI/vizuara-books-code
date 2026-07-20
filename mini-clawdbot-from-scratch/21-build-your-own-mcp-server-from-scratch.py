"""
Build a Mini ClawdBot from Scratch
Chapter 21: Build Your Own MCP Server from Scratch
Section: The Model Context Protocol (MCP)

Read this chapter: https://books.vizuara.ai/read/mini-clawdbot-from-scratch/build-your-own-mcp-server-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import sys, json

def send(msg):
    # one JSON object per line, on stdout ONLY
    sys.stdout.write(json.dumps(msg) + "\n")
    sys.stdout.flush()

def main():
    for line in sys.stdin:                 # blocks until the client sends a request
        line = line.strip()
        if not line:
            continue
        request = json.loads(line)
        method = request.get("method")
        req_id = request.get("id")         # None for notifications

        if method == "initialize":
            send(handle_initialize(req_id))
        elif method == "tools/list":
            send(handle_tools_list(req_id))
        elif method == "tools/call":
            send(handle_tools_call(req_id, request["params"]))
        # notifications (no id) → do nothing, send nothing

if __name__ == "__main__":
    main()

# --- block 2 ---
def handle_initialize(req_id):
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "result": {
            "protocolVersion": "2024-11-05",
            "capabilities": { "tools": {} },
            "serverInfo": { "name": "weather-server", "version": "0.1.0" }
        }
    }

# --- block 3 ---
TOOLS = [
    {
        "name": "get_weather",
        "description": "Get the current temperature for a given city.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "city": { "type": "string", "description": "City name, e.g. Pune" }
            },
            "required": ["city"]
        }
    }
]

def handle_tools_list(req_id):
    return { "jsonrpc": "2.0", "id": req_id, "result": { "tools": TOOLS } }

# --- block 4 ---
def run_get_weather(city):
    fake_db = { "Pune": 31, "Boston": 12, "London": 9 }
    temp = fake_db.get(city, 20)
    return f"It is currently {temp}°C in {city}."

def handle_tools_call(req_id, params):
    name = params["name"]
    args = params.get("arguments", {})
    if name == "get_weather":
        text = run_get_weather(args["city"])
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": { "content": [{ "type": "text", "text": text }] }
        }
    # unknown tool → a JSON-RPC error, not a crash
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": { "code": -32601, "message": f"Unknown tool: {name}" }
    }
