# ==========================================
# OMNIAI AUTOMATIC EMERGENCY RESPONSE ENGINE
# ==========================================

def get_response(emergency_type, risk_level, risk_score):
    """
    Decide the appropriate emergency response
    based on emergency type and risk.
    """

    emergency_type = emergency_type.upper().strip()
    risk_level = risk_level.upper().strip()

    # ======================================
    # CRITICAL EMERGENCIES
    # ======================================

    if emergency_type == "ATTACK":

        return {
            "action": "ACTIVATE_SOS",
            "message": (
                "You may be under physical attack. "
                "Stay as safe as possible. "
                "Emergency assistance is being prepared."
            ),
            "priority": "CRITICAL"
        }

    # ======================================
    # FOLLOWING
    # ======================================

    elif emergency_type == "FOLLOWING":

        return {
            "action": "PREPARE_SOS",
            "message": (
                "Someone may be following you. "
                "Move toward a safe public place "
                "and avoid confrontation."
            ),
            "priority": "CRITICAL"
        }

    # ======================================
    # ACCIDENT
    # ======================================

    elif emergency_type == "ACCIDENT":

        return {
            "action": "ACTIVATE_SOS",
            "message": (
                "A possible accident has been detected. "
                "Emergency assistance should be contacted."
            ),
            "priority": "CRITICAL"
        }

    # ======================================
    # MEDICAL
    # ======================================

    elif emergency_type == "MEDICAL":

        return {
            "action": "MEDICAL_ALERT",
            "message": (
                "A possible medical emergency has been detected. "
                "Please seek medical assistance immediately."
            ),
            "priority": "CRITICAL"
        }

    # ======================================
    # GENERAL SOS
    # ======================================

    elif emergency_type == "GENERAL SOS":

        return {
            "action": "ACTIVATE_SOS",
            "message": (
                "Emergency assistance has been requested."
            ),
            "priority": "CRITICAL"
        }

    # ======================================
    # UNSAFE
    # ======================================

    elif emergency_type == "UNSAFE":

        return {
            "action": "SAFETY_WARNING",
            "message": (
                "You appear to feel unsafe. "
                "Move to a safe and populated location "
                "if possible."
            ),
            "priority": "HIGH"
        }

    # ======================================
    # LOW RISK
    # ======================================

    if risk_level == "LOW":

        return {
            "action": "NO_ACTION",
            "message": (
                "No immediate emergency detected."
            ),
            "priority": "LOW"
        }

    # ======================================
    # MEDIUM RISK
    # ======================================

    if risk_level == "MEDIUM":

        return {
            "action": "MONITOR",
            "message": (
                "Your safety situation should be monitored."
            ),
            "priority": "MEDIUM"
        }

    # ======================================
    # HIGH RISK
    # ======================================

    if risk_level == "HIGH":

        return {
            "action": "PREPARE_SOS",
            "message": (
                "Your safety risk appears elevated. "
                "Stay alert and move toward safety."
            ),
            "priority": "HIGH"
        }

    # ======================================
    # FALLBACK
    # ======================================

    return {
        "action": "MONITOR",
        "message": (
            "Safety monitoring is active."
        ),
        "priority": risk_level
    }