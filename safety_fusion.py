# ==========================================
# OMNIAI SAFETY FUSION ENGINE
# ==========================================


def analyze_safety(
    user_text,
    risk,
    emergency_type,
    emotion=None,
    intent=None
):

    # ======================================
    # COPY BASIC INFORMATION
    # ======================================

    final_score = risk["score"]

    final_level = risk["level"]

    reasons = []

    if risk["reason"]:
        reasons.append(risk["reason"])


    # ======================================
    # EMERGENCY TYPE
    # ======================================

    emergency_name = emergency_type["type"]

    emergency_severity = emergency_type["severity"]

    emergency_reason = emergency_type["reason"]


    # ======================================
    # CRITICAL TYPES
    # ======================================

    critical_types = [
        "FOLLOWING",
        "ATTACK",
        "ACCIDENT",
        "MEDICAL",
        "GENERAL SOS"
    ]


    if emergency_name in critical_types:

        final_score = max(
            final_score,
            100
        )

        final_level = "CRITICAL"

        reasons.append(
            emergency_reason
        )


    # ======================================
    # HIGH-RISK TYPES
    # ======================================

    elif emergency_name == "UNSAFE":

        final_score = max(
            final_score,
            75
        )

        if final_level != "CRITICAL":

            final_level = "HIGH"

        reasons.append(
            emergency_reason
        )


    # ======================================
    # EMOTION BOOST
    # ======================================

    emotion_name = emotion

    if isinstance(emotion, tuple):

        emotion_name = emotion[0]


    if isinstance(emotion_name, str):

        emotion_name = emotion_name.lower()


    if emotion_name in [
        "fear",
        "fearful",
        "scared"
    ]:

        if final_score < 100:

            final_score += 10

        reasons.append(
            "Fear emotion supports the safety concern"
        )


    # ======================================
    # INTENT BOOST
    # ======================================

    if intent == "emergency":

        final_score = max(
            final_score,
            100
        )

        final_level = "CRITICAL"

        reasons.append(
            "Emergency intent confirmed"
        )


    # ======================================
    # LIMIT SCORE
    # ======================================

    if final_score > 100:

        final_score = 100


    # ======================================
    # FINAL LEVEL
    # ======================================

    if final_score >= 100:

        final_level = "CRITICAL"

    elif final_score >= 70:

        final_level = "HIGH"

    elif final_score >= 30:

        final_level = "MEDIUM"

    else:

        final_level = "LOW"


    # ======================================
    # REMOVE DUPLICATE REASONS
    # ======================================

    unique_reasons = []

    for reason in reasons:

        if reason not in unique_reasons:

            unique_reasons.append(reason)


    final_reason = " | ".join(
        unique_reasons
    )


    # ======================================
    # FINAL RESULT
    # ======================================

    return {

        "level": final_level,

        "score": final_score,

        "type": emergency_name,

        "severity": emergency_severity,

        "reason": final_reason
    }