# import voice_assistance



# print("Starting microphone test...")

# text = voice_assistance.listen("en-IN")

# print("Final result:", text)
import pyttsx3
import sys
print("My Python path is:", sys.executable)
import voice_assistance
print("Starting microphone test...")
text = voice_assistance.listen("en-IN")
print("Final result:", text)