import emotion_ai
import datetime
import memory
import computer_control
import reminder
import re
from datetime import datetime, timedelta
import language_ai
import intent_ai
import conversion_ai
import emergency
import safety_engine
import sos_message
import safety_score
import emergency_classifier

def process(user_text, emotion_data):

    print("🧠 OmniAI received:", user_text)
    emotion, confidence = emotion_data
    print("😊 Emotion:", emotion)
    
    print("📊 Confidence:", confidence)

    language=language_ai.detect_language(user_text)
    print("🌐 Language:", language)

    intent = intent_ai.detect_intent(user_text)
    print("🎯 Intent:", intent)
    # ======================================
# SAFETY RISK ANALYSIS
# ======================================

    risk = safety_engine.assess_risk(
         user_text,
         emotion,
         intent
        ) 
    print("🛡️ Risk Level:", risk["level"])
    print("📊 Risk Score:", risk["score"])
    print("📝 Risk Reason:", risk["reason"])
    # ======================================
    # SMART SAFETY SCORE
    # ======================================

    safety = safety_score.calculate_safety_score(
        intent,
        emotion,
        risk["level"],
        user_text
    )

    print("🧠 Smart Safety Score:", safety["score"])
    print("🚦 Safety Status:", safety["status"])

    # ======================================
# EMERGENCY SITUATION CLASSIFICATION
# ======================================

    emergency = emergency_classifier.classify_emergency(
        user_text
    )

    print("🚨 Emergency Type:", emergency["type"])

    if emergency["keyword"]:
        print("🔎 Detected Keyword:", emergency["keyword"])

    for reason in safety["reasons"]:
        print("   •", reason)
    if risk["level"] == "CRITICAL":
    
        print("🚨 CRITICAL SAFETY EVENT")
    
        message = sos_message.generate_sos_message(
            emergency_type="Personal Emergency",
            risk_level=risk["level"],
            risk_score=risk["score"],
            risk_reason=risk["reason"]
        )
    
        print(message)    

    print("🛡️ Risk Level:", risk["level"])
    print("📊 Risk Score:", risk["score"])
    print("📝 Risk Reason:", risk["reason"])

    # Temporary OmniAI brain
    response = generate_response(
        user_text,
        emotion,
        language,
        intent
    )

    return response


def generate_response(user_text, emotion,language="english",intent="conversation"):

    text = user_text.lower().strip()
    if intent == "emergency":

      print("🚨 EMERGENCY INTENT DETECTED")

      return (
        "Owner, I detected an emergency. "
        "Please confirm SOS if you need immediate assistance."
    )
    if "hello" in text or "hi" in text or "namste" in text:

      if intent == "greeting":
        if language == "hindi":

          return (
            "Namaste Owner! "
            "OmniAI mein aapka swagat hai. "
            "Main aapki kaise madad kar sakta hoon?"
        )

        elif language == "gujarati":

          return (
            "Namaste Owner! "
            "OmniAI ma tamaru swagat che. "
            "Hu tamari kevi rite madad kari shaku?"
        )
        else:

         return (
            "Hello Owner! "
            "Welcome back to OmniAI. "
            "How can I help you?"
        )

    
       
    elif (
     "how are you" in text or
     "how are u" in text or
     "kaise ho" in text or
     "kaisi ho" in text or
     "kem cho" in text):
      if intent == "how_are_you":

        if language=="hindi":
           return ("Main bilkul theek hoon, Owner. "
            "Main aapki madad karne ke liye ready hoon.")
        if language=="gujarati":
           return ("Hu bilkul majama chu, Owner. "
            "Hu tamari madad karva mate ready chu.")
        else:
          return ("I'm doing great, Owner. I'm ready to help you.")
    elif (
    "your name" in text
    or "who are you" in text
    or "aapka naam kya hai" in text
    or "tumhara naam kya hai" in text
    or "tamaru naam shu che" in text
    or "tame kon cho" in text
    ): 
      if intent == "identity":
        if language=="hindi":
           return (
            "Mera naam OmniAI hai, Owner. "
            "Main aapka personal emotional AI assistant hoon."
        )

        elif language == "gujarati":
          return (
            "Maru naam OmniAI che, Owner. "
            "Hu tamaro personal emotional AI assistant chu."
        )
           
        else:
            return ("My name is OmniAI, your personal emotional AI assistant.")
    # ======================================
    # TIME
    # ======================================
    if intent == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        return f"Owner, the current time is {current_time}."
    # ======================================
    # DATE
    # ======================================
    if intent == "date":
        current_date = datetime.now().strftime(
            "%A, %d %B %Y"
        )

        return (
            f"Today is {current_date}."
        )
    # ======================================
    # EMOTIONAL RESPONSES (if no command matches)
    # ======================================
    elif emotion == "happy":
        return (
            "You sound happy today, Owner! "
            "Keep that positive energy going."
        )


    elif emotion == "sad":
        return (
            "I can sense that you're feeling low. "
            "Take a deep breath. "
            "I'm here with you, Owner."
        )


    # ======================================
    # STRESSED / ANGRY / SURPRISED
    # ======================================
    elif emotion == "stressed":
        return (
            "You seem stressed, Owner. "
            "Let's take one thing at a time. "
            "You've got this."
        )


    elif emotion == "angry":
        return (
            "I can sense some frustration. "
            "Take a moment and breathe slowly. "
            "Let's solve the problem together."
        )

    elif emotion == "surprised":
        return (
            "That sounds surprising, Owner! "
            "Tell me more about what happened."
        )
    # youtube search
    if (
        "search youtube for" in text
        or "search youtube" in text
        or "find a video about" in text
    ):
    
        if "search youtube for" in text:
    
            query = text.split(
                "search youtube for",
                1
            )[1].strip()
    
        elif "search youtube" in text:
    
            query = text.split(
                "search youtube",
                1
            )[1].strip()
    
       # ======================================
       # GOODBYE
       # ============
        else:
    
            query = text.split(
                "find a video about",
                1
            )[1].strip()
    
        return computer_control.search_youtube(
            query
        )
    if (
        "search google for" in text
        or "search google" in text
        or "google search for" in text
        ):
    
        if "search google for" in text:
    
            query = text.split(
                "search google for",
                1
            )[1].strip()
    
        elif "google search for" in text:
    
            query = text.split(
                "google search for",
                1
            )[1].strip()
    
        else:
           query = text.split(
            "search google",
            1
        )[1].strip()

        return computer_control.search_google(query)

    if any(
        word in text
        for word in ["bye", "goodbye", "exit", "stop"]
    ):

        return (
            "Goodbye Owner. "
            "I'll be here whenever you need me."
        )
    # ======================================
    # REMEMBER INFORMATION
    # ======================================

    if "my favorite subject is" in text:
        value = text.split(
            "my favorite subject is",
            1
        )[1].strip()

        memory.remember(
            "favorite_subject",
            value
        )

        return (
            f"Got it, Owner. "
            f"I'll remember that your favorite "
            f"subject is {value}."
        )
    # ======================================
    # RECALL INFORMATION
    # ======================================

    if "what is my favorite subject" in text:
        value = memory.recall(
            "favorite_subject"
        )

        if value:
            return (
                f"Your favorite subject is {value}, Owner."
            )

        return (
            "You haven't told me your favorite "
            "subject yet, Owner."
        )
    # ======================================
    # SMART CHATGPT    
    # ======================================

    if (
    "open chatgpt" in text
    or "open chat gpt" in text
    or "talk to chatgpt" in text
    or "use chatgpt" in text
    ):

      return computer_control.open_application(
        "chatgpt"
    )
    # ======================================
# SMART GEMINI
# ======================================

    elif (
    "open gemini" in text
    or "use gemini" in text
    or "talk to gemini" in text
    ):

      return computer_control.open_application(
        "gemini"
    )


# ======================================
# SMART WHATSAPP
# ======================================

    elif (
    "open whatsapp" in text
    or "open whatsapp web" in text
    or "check whatsapp" in text
    or "use whatsapp" in text
    ):

      return computer_control.open_application(
        "whatsapp"
    )

    elif text.startswith("open "):
     app_name = text.replace(
        "open ",
        "",
        1
    ).strip()

     return computer_control.open_application(
        app_name
    )
    # ======================================
    # FAVORITE SONG
    # ======================================

    elif "favorite song" in text or "favourite song" in text:

     favorite = memory.recall("favorite_song")

     if not favorite:
        return "Owner, you haven't saved a favorite song yet."

     return computer_control.open_favorite(
        "song",
        favorite
    )
    # ======================================
    # FAVORITE CHANNEL / VIDEO / SERIES / STAR
    # ======================================
    elif "favorite channel" in text or "favourite channel" in text:

     favorite = memory.recall("favorite_channel")

     if not favorite:
        return "Owner, you haven't saved a favorite channel yet."

     return computer_control.open_favorite(
        "channel",
        favorite
    )

    
    elif "favorite video" in text or "favourite video" in text:

     favorite = memory.recall("favorite_video")

     if not favorite:
        return "Owner, you haven't saved a favorite video yet."

     return computer_control.open_favorite(
        "video",
        favorite
    )

    elif "favorite series" in text or "favourite series" in text:

     favorite = memory.recall("favorite_series")

     if not favorite:
        return "Owner, you haven't saved a favorite series yet."

     return computer_control.open_favorite(
        "series",
        favorite
    )
    elif "favorite star" in text or "favourite star" in text:

      favorite = memory.recall("favorite_star")

      if not favorite:
        return "Owner, you haven't saved a favorite star yet."

      return computer_control.open_favorite(
        "star",
        favorite
    )

    elif text.startswith("open "):

     app_name = text.replace(
        "open ",
        "",
        1
     ).strip()

     return computer_control.open_application(
        app_name
    )
    
    
    # ======================================
    # CREATE REMINDER
    # ======================================
    elif "remind me to" in text:
        match = re.search(
        r"remind me to (.+?) at (\d{1,2})(?::(\d{2}))?\s*(am|pm)?",
        text
    )

        if match:

          task = match.group(1).strip()

          hour = int(match.group(2))
          minute = int(match.group(3) or 0)
          period = match.group(4)
 
          if period == "pm" and hour != 12:
            hour += 12

          elif period == "am" and hour == 12:
            hour = 0

          now = datetime.now()

          reminder_time = now.replace(
            hour=hour,
            minute=minute,
            second=0,
            microsecond=0
         )
        # If today's time has already passed,
        # schedule it for tomorrow.
          if reminder_time <= now:
            reminder_time += timedelta(days=1)

          reminder.add_reminder(
            task,
            reminder_time.strftime(
                "%Y-%m-%d %H:%M"
             )
            )
          if language == "hindi":

                return (
                    f"Done Owner. Main aapko "
                    f"{task} ke liye "
                    f"{reminder_time.strftime('%I:%M %p')} "
                    f"par yaad dilaoonga."
                )

          elif language == "gujarati":

                return (
                    f"Done Owner. Hu tamne "
                    f"{task} mate "
                    f"{reminder_time.strftime('%I:%M %p')} "
                    f"vage yaad karavish.")

          else:

            return (
                "Please use the format: "
                "remind me to [task] at [time]."
            )


        else:
         return (
                "Sure Owner. Please use the format: "
                "remind me to [task] at [time]."
            )

    # ======================================
    # EMERGENCY / DANGER DETECTION
    # ======================================

    emergency_words = [
       # English
        "help me",
        "i need help",
        "i am in danger",
        "i'm in danger",
        "emergency",
        "save me",
        "someone is attacking me",
        "call for help",

         # Hindi
        "mujhe madad chahiye",
        "main khatre mein hoon",
        "mujhe bachao",
        "madad karo",
        "main danger mein hoon",
         # Gujarati
        "mane madad joie",
        "hu jokham ma chu",
        "mane bachavo",
        "madad karo",
        "hu danger ma chu"
        ]

    if any(
      phrase in text
      for phrase in emergency_words
      ):

      print("🚨 EMERGENCY DETECTED")

      return emergency.activate_emergency()

    if any(
      phrase in text
      for phrase in [
        "cancel emergency",
        "cancel sos",
        "stop emergency",
        "false alarm"
      ]
      ):

      return emergency.cancel_emergency()
    # ======================================
    # SHOW REMINDERS
    # ======================================
    elif (
        "what are my reminders" in text
        or "show my reminders" in text
        or "my reminders" in text
    ):
        reminders = reminder.get_active_reminders()
        if not reminders:
            return "Owner, you don't have any active reminders."

        response = "Owner, your active reminders are: "
        for item in reminders:
            # Re-parse time for friendly format
            time_obj = datetime.strptime(item["time"], "%Y-%m-%d %H:%M")
            response += f"{item['message']} at {time_obj.strftime('%I:%M %p')}. "
        return response.strip()
    # ======================================
    # CLEAR REMINDERS
    # ======================================
    elif (
        "cancel my reminders" in text
        or "delete my reminders" in text
        or "clear my reminders" in text
    ):
        reminder.clear_reminders()
        return "Done Owner. I've cleared your reminders."

    # ======================================
    # MULTILINGUAL DYNAMIC FALLBACK (if no other command matches)
    # ======================================
    if language == "hindi":
        return (
            "Main aapki baat samajh gaya hoon, Owner, "
            "lekin main abhi is par kaam karna seekh raha hoon."
        )
    elif language == "gujarati":
        return (
            "Hu tamari vaat samji gayo chu, Owner, "
            "pan hu haji aa par kaam karta sikhi rahyo chu."
        )
    else:
        return (
            "I understood you, Owner. "
            "I'm still learning how to help with that."
        )