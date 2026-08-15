import pyttsx3
import threading
import speech_recognition as sr
# this variable is used by the avatar

is_speaking = False


def speak(text):
  "hello Owner!! how i can help you?"
  global is_speaking
  
  is_speaking = True
  print("🤖 OmniAI:", text)
  try:
    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate", 160)
    engine.setProperty("volume", 1.0)
    engine.say(text)
    engine.runAndWait()

    engine.stop()
    is_speaking=False

  except Exception as error:
    print(" Voice error:",repr(error))
    
  finally:
    is_speaking=False

def speak_async(text):

 thread=threading.Thread(target=speak,args=(text,),daemon=True)
 thread.start()


def listen(language="en-IN"):
  recognizer=sr.Recognizer()

  # Make recognition less sensitive to background noise
  recognizer.energy_threshold = 300
  recognizer.dynamic_energy_threshold = True
  recognizer.pause_threshold = 0.8
  try:
   with sr.Microphone() as source:

    print("omni is listing:....")
    print("speak now...")
    recognizer.adjust_for_ambient_noise(source, duration=0.5)
    
    audio=recognizer.listen(source,timeout=10,phrase_time_limit=10)
    text=recognizer.recognize_google(audio,language=language)
    print("you:",text)
    print("omni is processing your voice:....")
  
    return text
  
  except sr.WaitTimeoutError:
        print("⏱️ No speech detected.")
        return ""
  except sr.UnknownValueError:
        print("❌ I heard you, but couldn't understand the words.")
        return ""

  except sr.RequestError as e:
        print("🌐 Speech recognition service error:", e)
        return ""

  except Exception as e:
        print("❌ Microphone error:", e)
        return ""



            

  



