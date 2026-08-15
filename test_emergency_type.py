import emergency_type_ai


test_messages = [
    "Someone is following me",
    "Someone is attacking me",
    "I met with an accident",
    "I can't breathe",
    "I feel unsafe",
    "Send SOS",
    "I am fine"
]


for message in test_messages:

    result = emergency_type_ai.detect_emergency_type(
        message
    )

    print()
    print("User:", message)
    print("Type:", result["type"])
    print("Severity:", result["severity"])
    print("Reason:", result["reason"])
    