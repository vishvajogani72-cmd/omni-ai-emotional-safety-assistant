import re


def detect_intent(text):

    text = text.lower().strip()

    # ======================================
    # GREETING
    # ======================================

    if any(word in text for word in [
        "hello",
        "hi",
        "hey",
        "namaste"
    ]):
        return "greeting"


    # ======================================
    # HOW ARE YOU
    # ======================================

    if any(phrase in text for phrase in [
        "how are you",
        "how are u",
        "how's everything",
        "how are things",
        "kaise ho",
        "kaisi ho",
        "kem cho"
    ]):
        return "how_are_you"


    # ======================================
    # NAME
    # ======================================

    if any(phrase in text for phrase in [
        "your name",
        "who are you",
        "what are you",
        "aapka naam",
        "tumhara naam",
        "tamaru naam",
        "tame kon"
    ]):
        return "identity"


    # ======================================
    # TIME
    # ======================================

    if any(phrase in text for phrase in [
        "what time is it",
        "tell me the time",
        "current time",
        "time right now",
        "time please",
        "kitne baje",
        "samay kya hai",
        "atyare ketla vagya"
    ]):
        return "time"


    # ======================================
    # DATE
    # ======================================

    if any(phrase in text for phrase in [
        "what is today's date",
        "what is the date",
        "today's date",
        "tell me today's date",
        "aaj ki date",
        "aaj ki tarikh",
        "aaj ni tarikh"
    ]):
        return "date"


    # ======================================
    # REMINDER
    # ======================================

    if any(phrase in text for phrase in [
        "remind me",
        "remember to remind me",
        "set a reminder",
        "create a reminder",
        "add a reminder",
        "yaad dilana",
        "yaad karavjo"
    ]):
        return "create_reminder"


    # ======================================
    # SHOW REMINDERS
    # ======================================

    if any(phrase in text for phrase in [
        "show my reminders",
        "what are my reminders",
        "list my reminders",
        "my reminders",
        "mere reminders",
        "mara reminders"
    ]):
        return "show_reminders"


    # ======================================
    # CLEAR REMINDERS
    # ======================================

    if any(phrase in text for phrase in [
        "cancel my reminders",
        "delete my reminders",
        "clear my reminders",
        "remove my reminders",
        "mere reminders hatao",
        "mara reminders delete karo"
    ]):
        return "clear_reminders"


    # ======================================
    # FAVORITES
    # ======================================

    if "favorite song" in text:
        return "favorite_song"

    if "favorite channel" in text:
        return "favorite_channel"

    if "favorite video" in text:
        return "favorite_video"

    if "favorite series" in text:
        return "favorite_series"

    if "favorite star" in text:
        return "favorite_star"


    # ======================================
    # OPEN APPLICATION
    # ======================================

    if text.startswith("open "):

        return "open_application"

    if any(phrase in text for phrase in [
        "open youtube",
        "open spotify",
        "open chatgpt",
        "launch youtube",
        "launch spotify",
        "start youtube",
        "start spotify"
    ]):
        return "open_application"


    # ======================================
    # GOODBYE
    # ======================================

    if any(word in text for word in [
        "bye",
        "goodbye",
        "exit",
        "stop"
    ]):
        return "goodbye"

    
    # =====
    if (
            "i am in danger" in text
            or "i'm in danger" in text
            or "help me" in text
            or "i need help" in text
            or "emergency" in text
            or "send sos" in text
            or "send an sos" in text
            or "i feel unsafe" in text
            or "someone is following me" in text
            or "someone is chasing me" in text
            or "call for help" in text
        ):
            return "emergency"
    
    # =================================
    # DEFAULT
    # ======================================

    return "conversation"