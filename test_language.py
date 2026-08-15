import language_ai


tests = [
    "Hello how are you?",
    "Mujhe reminder chahiye",
    "Mane 7 vagye yaad karavjo"
]


for text in tests:

    language = language_ai.detect_language(text)

    print(
        text,
        "→",
        language)