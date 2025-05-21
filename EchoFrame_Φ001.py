# EchoFrame_Φ001.py — Codex Temporal Memory Prototype

import json

def load_symbol_map(path="symbol_map.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Failed to load: {e}")
        return {}

def render_timeline(data):
    entries = []
    for k, v in data.items():
        entry = {
            "name": v.get("name", k),
            "type": "seal" if "Seal" in k else "scroll",
            "author": v.get("author", "Unknown"),
            "timestamp": v.get("timestamp", "Unknown")
        }
        entries.append(entry)
    
    # Sort by time (assuming ISO format)
    entries.sort(key=lambda x: x["timestamp"])

    print("\n===== Codex Temporal Timeline (EchoFrame_Φ001) =====\n")
    for e in entries:
        print(f"{e['timestamp']} | {e['type'].capitalize():<6} | {e['name']} (by {e['author']})")
    print("\n====================================================\n")

if __name__ == "__main__":
    smap = load_symbol_map()
    render_timeline(smap)

