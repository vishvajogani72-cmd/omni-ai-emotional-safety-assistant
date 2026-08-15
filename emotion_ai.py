import re
Emotion_word={
    "happy":[ "happy", "great", "amazing", "awesome",
        "wonderful", "excited", "good", "joy",
        "love", "fun",
        "ખુશ", "સરસ", "મજા", "આનંદ",
        "खुश", "अच्छा", "बहुत बढ़िया", "मज़ा"],
    "sad": [
        "sad", "lonely", "unhappy", "cry",
        "crying", "hurt", "broken", "miss",
        "disappointed",
        "દુઃખી", "દુઃખ", "એકલો", "રડવું",
        "दुखी", "दुःख", "अकेला", "रोना"
    ],

    "angry": [
        "angry", "mad", "furious", "annoyed",
        "irritated", "hate", "rage",
        "ગુસ્સો", "ગુસ્સે", "નફરત",
        "गुस्सा", "नाराज़", "नफरत"
    ],

    "stressed": [
        "stress", "stressed", "tension",
        "worried", "worry", "pressure",
        "overwhelmed", "exhausted", "tired",
        "ચિંતા", "ટેન્શન", "દબાણ", "થાક",
         "चिंता", "तनाव", "दबाव", "थका"
    ],

    "surprised": [
        "wow", "surprised", "shocked",
        "unexpected", "unbelievable",
        "વાહ", "આશ્ચર્ય",
        "वाह", "हैरान", "अविश्वसनीय"
    ],

    "confused": [
        "confused", "confusing", "don't understand",
        "what", "why", "how",
        "મૂંઝવણ", "સમજાતું નથી",
        "उलझन", "समझ नहीं आ रहा"
    ]
}
    
# Supportive responses
EMOTION_MESSAGES = {

    "happy":
        "You sound happy today! Keep that positive energy going.",

    "sad":
        "It sounds like you're having a difficult moment. Take a breath. I'm here with you.",

    "angry":
        "You sound upset. Take a slow breath and let's handle this one step at a time.",

    "stressed":
        "You sound stressed. Take a short break, breathe slowly, and focus on one thing at a time.",

    "surprised":
        "That sounds unexpected! Tell me what happened.",
     "confused":
        "It's okay to feel confused. Let's break the problem into smaller steps.",

    "neutral":
        "I'm listening. Tell me what you need."
}


def clean_text(text):
    """
    Clean and prepare the user's speech text.
    """

    text = text.lower().strip()

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text

def detect_emotion(text):

    text = clean_text(text)

    scores = {}

    # Count matching emotion words
    for emotion, words in Emotion_word.items():

        score = 0

        for word in words:

            if word in text:
                score += 1

        scores[emotion] = score


    # Find strongest emotion
    best_emotion = max(scores, key=scores.get)

    best_score = scores[best_emotion]


    # Nothing matched
    if best_score == 0:

        return "neutral", 0.50


    # Simple confidence estimate
    confidence = min(
        0.60 + (best_score * 0.10),
        0.95
    )

    return best_emotion, confidence


def get_emotion_message(emotion):

    return EMOTION_MESSAGES.get( emotion,EMOTION_MESSAGES["neutral"])