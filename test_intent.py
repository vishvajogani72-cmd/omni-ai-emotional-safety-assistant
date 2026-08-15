import intent_ai


tests = [
    "Hey OmniAI",
    "How's everything going?",
    "Can you tell me the time?",
    "What time is it right now?",
    "Could you remind me to study at 7 PM?",
    "Please set a reminder for my physics study",
    "Show me my reminders",
    "Open YouTube",
    "What is your name?",
    "Bye",
    "i'm in danger",
    "send sos",
    "I feel unsafe",
    "someone is following me",
    "someone is chasing me",
    "call for help",
    "call my mom"

]


for text in tests:

    intent = intent_ai.detect_intent(text)

    print(
        f"{text}  →  {intent}"
    )