# ==========================================
# OMNIAI SMART SAFETY SCORE
# ==========================================

def calculate_safety_score(
    intent,
    emotion,
    risk_level,
    user_text
):
    """
    Calculate a safety score from 0 to 100.

    Higher score = greater danger.
    """

    text = user_text.lower().strip()

    score = 0
    reasons = []

    # ======================================
    # 1. INTENT RISK
    # ======================================

    if intent == "emergency":
        score += 40
        reasons.append("Emergency intent detected")

    # ======================================
    # 2. EXISTING RISK LEVEL
    # ======================================

    if risk_level == "CRITICAL":
        score += 40
        reasons.append("Critical safety risk")

    elif risk_level == "HIGH":
        score += 25
        reasons.append("High safety risk")

    elif risk_level == "MEDIUM":
        score += 15
        reasons.append("Medium safety risk")

    # ======================================
    # 3. EMOTION
    # ======================================

    if emotion in ["fear", "fearful", "scared"]:
        score += 15
        reasons.append("Fear detected")

    elif emotion in ["sad", "angry", "panic", "anxious"]:
        score += 10
        reasons.append(f"{emotion} emotion detected")

    # ======================================
    # 4. DANGER SITUATION
    # ======================================

    danger_words = [
        "following",
        "chasing",
        "attacking",
        "threat",
        "unsafe",
        "danger",
        "help me",
        "kidnap",
        "rob",
        "fire",
        "accident"
    ]

    detected_words = []

    for word in danger_words:

        if word in text:
            detected_words.append(word)

    if detected_words:

        score += min(len(detected_words) * 5, 20)

        reasons.append(
            "Danger indicators: "
            + ", ".join(detected_words)
        )

    # ======================================
    # LIMIT SCORE
    # ======================================

    score = min(score, 100)

    # ======================================
    # FINAL SAFETY STATUS
    # ======================================

    if score >= 80:
        status = "CRITICAL"

    elif score >= 60:
        status = "HIGH RISK"

    elif score >= 30:
        status = "CAUTION"

    else:
        status = "SAFE"

    # ======================================
    # DEFAULT REASON
    # ======================================

    if not reasons:
        reasons.append("No major danger indicators detected")

    return {
        "score": score,
        "status": status,
        "reasons": reasons
    }