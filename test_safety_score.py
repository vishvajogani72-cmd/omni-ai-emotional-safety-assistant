import safety_score


test_cases = [

    {
        "text": "I'm fine",
        "intent": "greeting",
        "emotion": "neutral",
        "risk": "LOW"
    },

    {
        "text": "I feel unsafe",
        "intent": "emergency",
        "emotion": "fear",
        "risk": "HIGH"
    },

    {
        "text": "Someone is following me",
        "intent": "emergency",
        "emotion": "fear",
        "risk": "CRITICAL"
    },

    {
        "text": "I'm in danger",
        "intent": "emergency",
        "emotion": "fear",
        "risk": "CRITICAL"
    }
]


for case in test_cases:

    result = safety_score.calculate_safety_score(
        case["intent"],
        case["emotion"],
        case["risk"],
        case["text"]
    )

    print()
    print("================================")
    print("User:", case["text"])
    print("Safety Score:", result["score"])
    print("Status:", result["status"])
    print("Reasons:")

    for reason in result["reasons"]:
        print(" -", reason)
        