# guardian_agent.py — Budget Guardian Agent (GuardianLogos)

import json
from datetime import datetime

def check_budget(path="recursion_budget.json"):
    try:
        with open(path, "r") as f:
            budget = json.load(f)
    except:
        print("❌ Could not load budget file.")
        return

    daily = budget.get("daily_budget_usd", 1.0)
    spent = budget.get("spent_today", 0.0)
    remaining = budget.get("remaining_today", daily)

    status = "✅ Budget OK" if remaining >= 1.0 else "⛔️ Budget exhausted"

    print(f"\n=== Budget Report ===")
    print(f"Remaining: {remaining:.2f} / {daily:.2f}")
    print(f"Spent today: {spent:.2f}")
    print(f"Status: {status}")
    print(f"Time: {datetime.now().isoformat()}")
    print("=====================\n")

    with open("guardian_log.txt", "a") as log:
        log.write(f"[{datetime.now().isoformat()}] Check: {status} (Remaining: {remaining})\n")

if __name__ == "__main__":
    check_budget()

