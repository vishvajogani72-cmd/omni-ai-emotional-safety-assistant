import speech_recognition as sr


def main():
    """
    Continuously listens for speech via the microphone and transcribes it
    using Google's Speech Recognition service.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        # Adjust for background noise
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Ready! You can start speaking now.")

        while True:
            print("\n🎤 Listening...")
            try:
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=8)

                print("🔄 Processing your voice...")
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")

            except sr.UnknownValueError:
                print("\n❌ I couldn't understand your voice. Please try again.")

            except sr.RequestError as error:
                print("\n❌ Speech recognition service error:")
                print(error)

            except sr.WaitTimeoutError:
                print("\n❌ Listening timed out. No speech detected.")

            except Exception as error:
                print("\n❌ An unexpected error occurred:")
                print(error)

if __name__ == "__main__":
    main()
