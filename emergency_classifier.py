# ==========================================
# OMNIAI EMERGENCY CLASSIFIER
# ==========================================

def classify_emergency(user_text):

    text = user_text.lower().strip()

    categories = {
        "PERSONAL_DANGER": [
            "danger",
            "unsafe",
            "threat",
            "attacking",
            "attack",
            "help me"
        ],

        "FOLLOWING": [
            "following me",
            "someone is following",
            "chasing me",
            "someone is chasing"
        ],

        "MEDICAL_EMERGENCY": [
            "medical emergency",
            "i am injured",
            "injured",
            "bleeding",
            "can't breathe",
            "cannot breathe",
            "heart attack",
            "ambulance"
        ],

        "ACCIDENT": [
            "accident",
            "crash",
            "car accident",
            "bike accident",
            "road accident"
        ],

        "FIRE": [
            "fire",
            "building is burning",
            "smoke",
            "burning"
        ],

        "LOST": [
            "i am lost",
            "lost",
            "don't know where i am",
            "cannot find my way"
        ],

        "PANIC": [
            "panic",
            "panic attack",
            "i am panicking"
        ]
    }

    # Check every category
    for category, keywords in categories.items():

        for keyword in keywords:

            if keyword in text:

                return {
                    "type": category,
                    "keyword": keyword
                }

    # No specific emergency detected
    return {
        "type": "GENERAL_EMERGENCY",
        "keyword": None
    }