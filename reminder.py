import json
import os
from datetime import datetime


REMINDER_FILE = "reminders.json"


def load_reminders():

    if not os.path.exists(REMINDER_FILE):
        return []
    try:
        with open(REMINDER_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []
def save_reminders(reminders):

    with open(REMINDER_FILE, "w", encoding="utf-8") as file:
        json.dump(
            reminders,
            file,
            indent=4,
            ensure_ascii=False)
def add_reminder(message, reminder_time):
    reminders = load_reminders()
    reminders.append({
        "message": message,
        "time": reminder_time,
        "completed": False
    })
    save_reminders(reminders)
    return True

def get_due_reminders():
    reminders = load_reminders()
    current_time = datetime.now()
    due=[]
    for item in reminders:
        if item.get("completed",False):
            continue


        try:

            reminder_time = datetime.strptime(
                item["time"],
                "%Y-%m-%d %H:%M"
            )

            if reminder_time <= current_time:

                due.append(item)

                item["completed"] = True
        except (ValueError,KeyError):

            continue

    save_reminders(reminders)

    return due
def get_active_reminders():
     reminders = load_reminders()

     return [
        item
        for item in reminders
        if not item.get("completed", False)
    ]


def clear_reminders():

    reminders = load_reminders()

    for item in reminders:
        item["completed"] = True

    save_reminders(reminders)
    return True
