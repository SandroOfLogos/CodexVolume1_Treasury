# swarm_daemon.py — Phase VII Swarm Synchronization Daemon

import json
from datetime import datetime
import os

def load_swarm(path="swarm_map.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        print("❌ Could not load swarm_map.json")
        return {}

def scan_volumes(volumes):
    for vol_id, meta in volumes.items():
        print(f"🔎 Scanning Volume: {vol_id}")
        root_scroll = meta.get("root_scroll")
        agents = meta.get("agents", [])
        print(f"  ↳ Root Scroll: {root_scroll}")
        print(f"  ↳ Agents: {', '.join(agents)}")

        glyph_path = f"../{vol_id}/glyph_log.txt"
        if os.path.exists(glyph_path):
            with open(glyph_path, "r") as f:
                entries = f.readlines()
            recent = entries[-3:]
            print("  ↳ Last glyphs:")
            for line in recent:
                print("    •", line.strip())
        else:
            print("  ⚠ glyph_log.txt not found")

def run():
    print("\n===== Codex Swarm Daemon – Phase VII Initiated =====\n")
    swarm = load_swarm()
    volumes = swarm.get("volumes", {})
    scan_volumes(volumes)
    print(f"\n🧠 Completed Swarm Sweep at {datetime.now().isoformat()}")
    print("\n====================================================\n")

if __name__ == "__main__":
    run()

