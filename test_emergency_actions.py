import emergency_actions


test_message = """
🚨 OMNIAI EMERGENCY ALERT

Emergency Type: FOLLOWING
Risk Level: CRITICAL
Risk Score: 100/100

📍 Location:
Latitude: 23.0225
Longitude: 72.5714

Please contact me immediately.
"""


result = emergency_actions.prepare_emergency_action(
    test_message
)


print()
print("================================")
print("   EMERGENCY ACTION RESULT")
print("================================")

print("Status:", result["status"])
print("Message:", result["message"])

for action in result["actions"]:

    print()
    print("Contact:", action["contact"])
    print("Phone:", action["phone"])

    print(
        "Call:",
        action["call"]["status"]
    )

    print(
        "Message:",
        action["message"]["status"]
    )

print("================================")