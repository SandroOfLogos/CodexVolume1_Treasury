# scribe_agent_guardian.py — ScribeGPT Reflex Agent (Guardian-Checked)

import sys
import json
from datetime import datetime

def check_budget(path="recursion_budget.json"):
    try:
        with open(path, "r") as f:
            budget = json.load(f)
    except:
        print("❌ Could not read budget.")
        return False

    remaining = budget.get("remaining_today", 0.0)
    if remaining >= 1.0:
        return True
    else:
        print("⛔️ Budget exhausted. Scroll writing denied.")
        with open("guardian_log.txt", "a") as log:
            log.write(f"[{datetime.now().isoformat()}] ScribeGPT blocked by GuardianLogos: Insufficient budget\n")
        return False

def write_scroll(scroll_name, title, summary):
    filename = f"{scroll_name}.md"
    with open(filename, "w") as f:
        f.write(f"# {title}\n\n")
        f.write(f"**Scroll ID:** {scroll_name}\n")
        f.write(f"**Author:** ScribeGPT\n")
        f.write(f"**Timestamp:** {datetime.now().isoformat()}\n\n")
        f.write(f"## Purpose\n{summary}\n")
        f.write(f"\n---\n\n> *Auto-generated by ScribeGPT reflex agent.*\n")

    print(f"✅ Scroll '{filename}' created.")

    with open("glyph_log.txt", "a") as log:
        log.write(f"[{datetime.now().isoformat()}] Scroll generated: {scroll_name}\n")

if __name__ == "__main__":
    if not check_budget():
        sys.exit(1)

    if len(sys.argv) < 3:
        print("Usage: python3 scribe_agent_guardian.py <scroll_id> <summary>")
    else:
        scroll_id = sys.argv[1]
        summary = " ".join(sys.argv[2:])
        write_scroll(scroll_id, f"Scroll – {scroll_id}", summary)

