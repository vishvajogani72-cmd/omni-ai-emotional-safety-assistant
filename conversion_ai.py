import emotion_ai
import language_ai
import pyttsx3


def generate_reply(user_text, language, emotion):

    text = user_text.lower().strip()

    # -----------------------------
    # ENGLISH
    # -----------------------------

    if language == "english":

        if "what can you do" in text:
            return (
                "I can remember information, manage reminders, "
                "open applications, access your favorite content, "
                "understand emotions, and talk with you."
            )

        if "are you real" in text:
            return (
                "I'm a software-based AI assistant, Owner. "
                "I'm here to interact with you and help you."
            )

        if "thank you" in text or "thanks" in text:
            return (
                "You're welcome, Owner. "
                "I'm always happy to help."
            )

        if emotion == "happy":
            return (
                "You sound positive today, Owner. "
                "What's on your mind?"
            )

        if emotion == "sad":
            return (
                "I'm listening, Owner. "
                "You can tell me what's bothering you."
            )
        if emotion == "stressed":
            return (
                "You seem stressed, Owner. "
                "Let's take it one step at a time."
            )

        if emotion == "angry":
            return (
                "I can sense some frustration, Owner. "
                "Let's solve the problem together."
            )

        return (
            "I understand what you're saying, Owner. "
            "Tell me a little more."
        )


    # -----------------------------
    # HINDI
    # -----------------------------

    elif language == "hindi":

        if "kya kar sakte ho" in text:
            return (
                "Main reminders manage kar sakta hoon, "
                "information yaad rakh sakta hoon, "
                "applications open kar sakta hoon aur "
                "aapse baat kar sakta hoon."
            )

        if "real ho" in text:
            return (
                "Main ek software based AI assistant hoon, Owner. "
                "Main aapki madad karne ke liye bana hoon."
            )

        if "dhanyawad" in text or "shukriya" in text:
            return (
                "Aapka swagat hai, Owner. "
                "Mujhe aapki madad karke khushi hoti hai."
            )

        if emotion == "happy":
            return (
                "Aap aaj kaafi khush lag rahe hain, Owner. "
                "Aapke mann mein kya hai?"
            )

        if emotion == "sad":
            return (
                "Main aapki baat sun raha hoon, Owner. "
                "Aap mujhe bata sakte hain ki kya hua."
            )
        if emotion == "stressed":
            return (
                "Aap thode stressed lag rahe hain, Owner. "
                "Ek-ek karke problem solve karte hain."
            )

        if emotion == "angry":
            return (
                "Mujhe lag raha hai aap thode frustrated hain. "
                "Chaliye milkar problem solve karte hain."
            )
        return (
            "Main aapki baat samajh raha hoon, Owner. "
            "Thoda aur bataiye."
        )


    # -----------------------------
    # GUJARATI
    # -----------------------------

    elif language == "gujarati":

        if "shu kari shako" in text:
            return (
                "Hu reminders manage kari shaku chu, "
                "mahiti yaad rakhi shaku chu, "
                "applications open kari shaku chu "
                "ane tamari sathe vaat kari shaku chu."
            )

        if "real cho" in text:
            return (
                "Hu ek software based AI assistant chu, Owner. "
                "Hu tamari madad karva mate banavyo chu."
            )

        if "aabhar" in text or "thanks" in text:
            return (
                "Tamaro aabhar, Owner. "
                "Tamari madad kari ne mane khushi thay che."
            )

        if emotion == "happy":
            return (
                "Tame aaje khub khush lago cho, Owner. "
                "Tamara man ma shu che?"
            )

        if emotion == "sad":
            return (
                "Hu tamari vaat sambhli rahyo chu, Owner. "
                "Tame mane kahi shako cho ke shu thayu."
            )
        if emotion == "stressed":
            return (
                "Tame thoda stressed lago cho, Owner. "
                "Chalo ek-ek kari ne problem solve kariye."
            )

        if emotion == "angry":
            return (
                "Mane lage che tame thoda frustrated cho. "
                "Chalo sathe mali ne problem solve kariye."
            )
        return (
            "Hu tamari vaat samji rahyo chu, Owner. "
            "Thodu vadhu janavo."
        )


    # -----------------------------
    # FALLBACK
    # -----------------------------

    return (
        "I'm here with you, Owner. "
        "Tell me more."
    )
