import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language='en-in')
            print("🗣️ You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Speech service error.")
            return ""

speak("Hello! I'm your virtual assistant. How can I help you?")

while True:
    command = listen()
    if command == "":
        continue

    if "hi" in command:
        speak("Hello, how is your day?")
    elif "python" in command:
        speak("Python classes will end today.")
    elif "your name" in command:
        speak("I am your Python assistant.")
    elif "stop" in command or "exit" in command or "bye" in command:
        speak("Okay bye bye! Have a good day.")
        break
    else:
        speak("Sorry, I can't do that yet.")
