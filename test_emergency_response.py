import emergency_response


tests = [
    ("FOLLOWING", "CRITICAL", 100),
    ("ATTACK", "CRITICAL", 100),
    ("ACCIDENT", "CRITICAL", 100),
    ("MEDICAL", "CRITICAL", 100),
    ("UNSAFE", "HIGH", 75),
    ("GENERAL SOS", "CRITICAL", 100),
    ("NONE", "LOW", 0),
]


for emergency_type, risk_level, risk_score in tests:

    result = emergency_response.get_response(
        emergency_type,
        risk_level,
        risk_score
    )

    print()
    print("====================================")
    print("Emergency:", emergency_type)
    print("Risk:", risk_level)
    print("Score:", risk_score)
    print("Action:", result["action"])
    print("Priority:", result["priority"])
    print("Message:", result["message"])
    