import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")

engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query