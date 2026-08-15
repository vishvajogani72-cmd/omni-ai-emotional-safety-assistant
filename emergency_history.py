import json
from datetime import datetime
from pathlib import Path


HISTORY_FILE = Path(__file__).with_name("emergency_history.json")


def load_history():
    if not HISTORY_FILE.exists():
        return []

    try:
        with HISTORY_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_history(history):
    with HISTORY_FILE.open("w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)


def add_record(
    status,
    emergency_type="GENERAL_EMERGENCY",
    risk_level="UNKNOWN",
    risk_score=0,
    reason="",
    action_status=""
):
    history = load_history()

    record = {
        "time": datetime.now().strftime("%d %B %Y, %I:%M:%S %p"),
        "status": status,
        "emergency_type": emergency_type,
        "risk_level": risk_level,
        "risk_score": risk_score,
        "reason": reason,
        "action_status": action_status
    }

    history.append(record)
    save_history(history)

    print("📁 Emergency history saved.")
    return record


def display_history():
    history = load_history()

    print()
    print("================================")
    print("      OMNIAI EMERGENCY HISTORY")
    print("================================")

    if not history:
        print("No emergency records found.")
        return

    for index, record in enumerate(history, start=1):
        print()
        print(f"Record {index}")
        print("Time:", record["time"])
        print("Status:", record["status"])
        print("Type:", record["emergency_type"])
        print("Risk:", record["risk_level"])
        print("Score:", record["risk_score"])
        print("Reason:", record["reason"])
        print("Action:", record["action_status"])

    print("================================")