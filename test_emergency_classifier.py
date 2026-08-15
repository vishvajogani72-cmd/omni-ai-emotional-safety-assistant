import emergency_classifier


test_cases = [
    "Someone is following me",
    "I am injured",
    "There is a fire",
    "I had an accident",
    "I am lost",
    "I am in danger",
    "I am having a panic attack"
]


for text in test_cases:

    result = emergency_classifier.classify_emergency(text)

    print()
    print("================================")
    print("User:", text)
    print("Emergency Type:", result["type"])
    print("Detected Keyword:", result["keyword"])