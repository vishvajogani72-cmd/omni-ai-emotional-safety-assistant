import safety_engine
import emergency_type_ai
import safety_fusion


tests = [
    ("I'm fine", "neutral", "greeting"),

    ("I feel unsafe", "fear", "normal"),

    ("Someone is following me", "fear", "emergency"),

    ("Someone is attacking me", "fear", "emergency"),

    ("I met with an accident", "fear", "emergency"),

    ("I can't breathe", "fear", "emergency"),

    ("Send SOS", "fear", "emergency"),
]


for user_text, emotion, intent in tests:

    print()
    print("========================================")

    print("USER:", user_text)

    # Risk engine
    risk = safety_engine.assess_risk(
        user_text,
        emotion,
        intent
    )

    # Emergency type
    emergency_type = (
        emergency_type_ai.detect_emergency_type(
            user_text
        )
    )

    # Fusion
    final = safety_fusion.analyze_safety(
        user_text,
        risk,
        emergency_type,
        emotion,
        intent
    )

    print("Risk:", risk)
    print("Emergency Type:", emergency_type)

    print()
    print("FINAL RESULT")
    print("Level:", final["level"])
    print("Score:", final["score"])
    print("Type:", final["type"])
    print("Severity:", final["severity"])
    print("Reason:", final["reason"])
    