import json

with open("symbol_map.json", "r") as f:
    glyphs = json.load(f)

print("\n===== Glyph Visualizer =====\n")
for name, data in glyphs.items():
    print(f"— {name} —")
    print(f"Description: {data.get('description')}")
    print(f"Author: {data.get('author')}")
    print(f"Timestamp: {data.get('timestamp')}\n")

