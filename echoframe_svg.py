# echoframe_svg.py — SVG Memory Ring for EchoFrame_Φ001

import json

def load_data(path="symbol_map.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Load error: {e}")
        return {}

def generate_svg(data, output_path="echoframe.svg"):
    entries = []
    for k, v in data.items():
        entries.append({
            "name": v.get("name", k),
            "author": v.get("author", "Unknown"),
            "timestamp": v.get("timestamp", "Unknown"),
        })

    entries.sort(key=lambda x: x["timestamp"])
    radius = 180
    spacing = 360 / len(entries)

    svg = [
        f'<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">',
        f'<circle cx="200" cy="200" r="{radius}" stroke="#333" stroke-width="1" fill="none" />'
    ]

    for i, e in enumerate(entries):
        angle = spacing * i
        x = 200 + radius * 0.85 * __import__("math").cos(__import__("math").radians(angle))
        y = 200 + radius * 0.85 * __import__("math").sin(__import__("math").radians(angle))
        svg.append(f'<text x="{x:.2f}" y="{y:.2f}" font-size="8" text-anchor="middle">{e["name"]}</text>')

    svg.append('</svg>')

    with open(output_path, "w") as f:
        f.write("\n".join(svg))
    print(f"✅ SVG written to {output_path}")

if __name__ == "__main__":
    data = load_data()
    generate_svg(data)

