# safety_engine.py

# ==========================================
# OMNIAI SAFETY RISK ENGINE
# ==========================================

def assess_risk(user_text, emotion=None, intent=None):

    text = user_text.lower().strip()

    score=0
    reasons=[]

    # ======================================
    # CRITICAL EMERGENCY
    # ======================================

    critical_words = [
        "i am in danger",
        "i'm in danger",
        "send sos",
        "send an sos",
         "emergency",
        "call for help",
        "someone is attacking me",
        "someone is chasing me",
        "someone is following me",
        "help me"
    ]

    for word in critical_words:

        if word in text:
            score=100
            reasons.append(f"Emergency phrase detected: {word}")
            break
       
    # ======================================
    # HIGH RISK
    # ======================================
    high_risk_words = [
        "i feel unsafe",
        "i am scared",
        "i'm scared",
        "i feel threatened",
        "stranger is near me",
        "i don't feel safe",
        "dangerous"
    ]

    for word in high_risk_words:

        if word in text:
          score += 75
          
          reasons.append(
                          f"Safety concern detected: {word}"
                      )
          
          break 
      
    
    # ======================================
    # EMOTION SIGNAL
    # ======================================

    emotion_name = emotion

    # If emotion is returned as:
    # ("fear", 0.95)

    if isinstance(emotion, tuple):

        emotion_name = emotion[0]

    if isinstance(emotion_name, str):

        emotion_name = emotion_name.lower()


    if emotion_name in [
        "fear",
        "fearful",
        "scared"
    ]:

        score += 30

        reasons.append(
            "Fear-related emotion detected"
        )
    # ======================================
    # INTENT SIGNAL
    # ======================================

    if intent == "emergency":

        score += 50

        reasons.append(
            "Emergency intent detected"
        )


    # ======================================
    # LIMIT SCORE
    # ======================================

    if score > 100:

        score = 100
    # ======================================
    # DETERMINE RISK LEVEL
    # ======================================

    if score >= 100:

        level = "CRITICAL"

    elif score >= 70:

        level = "HIGH"

    elif score >= 30:

        level = "MEDIUM"

    else:

        level = "LOW"
     # ======================================
    # REASON
    # ======================================

    if reasons:

        reason = " | ".join(reasons)

    else:

        reason = (
            "No immediate safety threat detected"
        )


    # ======================================
    # RETURN RESULT
    # ======================================

    return {
        "level": level,
        "score":score,
        "reason": reason
    }