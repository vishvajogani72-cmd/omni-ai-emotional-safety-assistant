# =========================================================
# OMNIAI EMERGENCY TYPE AI
# =========================================================

def detect_emergency_type(user_text):

    text = user_text.lower().strip()

    # =====================================================
    # FOLLOWING / STALKING
    # =====================================================

    following_words = [
        "someone is following me",
        "someone follows me",
        "i am being followed",
        "i'm being followed",
        "someone is chasing me",
        "someone is behind me",
        "a person is following me",
        "stranger is following me"
    ]

    for word in following_words:

        if word in text:

            return {
                "type": "FOLLOWING",
                "severity": "CRITICAL",
                "reason": "Possible person-following situation detected"
            }


    # =====================================================
    # ATTACK
    # =====================================================

    attack_words = [
        "someone is attacking me",
        "someone attacked me",
        "i am being attacked",
        "i'm being attacked",
        "someone is hitting me",
        "someone is hurting me",
        "someone wants to hurt me",
        "i am being assaulted"
    ]

    for word in attack_words:

        if word in text:

            return {
                "type": "ATTACK",
                "severity": "CRITICAL",
                "reason": "Possible physical attack detected"
            }


    # =====================================================
    # ACCIDENT
    # =====================================================

    accident_words = [
        "i had an accident",
        "i met with an accident",
        "there was an accident",
        "car accident",
        "bike accident",
        "road accident",
        "vehicle accident",
        "i crashed",
        "we crashed"
    ]

    for word in accident_words:

        if word in text:

            return {
                "type": "ACCIDENT",
                "severity": "CRITICAL",
                "reason": "Possible accident detected"
            }


    # =====================================================
    # MEDICAL EMERGENCY
    # =====================================================

    medical_words = [
        "i can't breathe",
        "i cannot breathe",
        "difficulty breathing",
        "chest pain",
        "i am unconscious",
        "i feel faint",
        "i am bleeding",
        "heavy bleeding",
        "medical emergency",
        "i need a doctor",
        "i need medical help"
    ]

    for word in medical_words:

        if word in text:

            return {
                "type": "MEDICAL",
                "severity": "CRITICAL",
                "reason": "Possible medical emergency detected"
            }


    # =====================================================
    # UNSAFE SITUATION
    # =====================================================

    unsafe_words = [
        "i feel unsafe",
        "i don't feel safe",
        "i do not feel safe",
        "i am scared",
        "i'm scared",
        "i feel threatened",
        "this place is dangerous",
        "i am alone and scared",
        "stranger is near me"
    ]

    for word in unsafe_words:

        if word in text:

            return {
                "type": "UNSAFE",
                "severity": "HIGH",
                "reason": "Unsafe situation detected"
            }


    # =====================================================
    # GENERAL SOS
    # =====================================================

    sos_words = [
        "send sos",
        "send an sos",
        "emergency",
        "call for help",
        "help me",
        "i am in danger",
        "i'm in danger"
    ]

    for word in sos_words:

        if word in text:

            return {
                "type": "GENERAL SOS",
                "severity": "CRITICAL",
                "reason": "General emergency request detected"
            }


    # =====================================================
    # NORMAL
    # =====================================================

    return {
        "type": "NONE",
        "severity": "LOW",
        "reason": "No specific emergency type detected"
    }