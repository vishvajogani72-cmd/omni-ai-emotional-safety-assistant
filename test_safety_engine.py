import safety_engine


tests = [

    ("I'm fine", "neutral", "greeting"),

    ("I feel unsafe", "fear", "normal"),

    ("I'm scared", "fear", "normal"),

    ("Someone is following me", "fear", "emergency"),

    ("Someone is attacking me", "fear", "emergency"),

    ("Send SOS", "fear", "emergency"),

    ("Help me", "fear", "emergency"),
]


for user_text, emotion, intent in tests:

    result = safety_engine.assess_risk(
        user_text,
        emotion,
        intent
    )

    print()
    print("================================")
    print("User:", user_text)
    print("Emotion:", emotion)
    print("Intent:", intent)
    print("Risk Level:", result["level"])
    print("Risk Score:", result["score"])
    print("Reason:", result["reason"])