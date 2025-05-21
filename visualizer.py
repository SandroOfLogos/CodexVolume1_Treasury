# visualizer.py
import json

def load_symbol_map(path="symbol_map.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return {}

def render_tree(symbol_map):
    def recurse(node_id, depth=0):
        prefix = "  " * depth + "- "
        node = symbol_map.get(node_id, {})
        name = node.get("name", node_id)
        print(f"{prefix}{name}")
        for child_id in node.get("links", []):
            recurse(child_id, depth + 1)

    root_nodes = [k for k, v in symbol_map.items() if v.get("root", False)]
    for root in root_nodes:
        recurse(root)

if __name__ == "__main__":
    smap = load_symbol_map()
    render_tree(smap)

