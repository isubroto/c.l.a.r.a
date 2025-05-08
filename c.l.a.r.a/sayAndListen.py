import pyttsx3
import speech_recognition

class SayAndListen:
    def __init__(self):
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init("sapi5")
        
        # Get available voices
        voices = self.engine.getProperty("voices")
        
        # Set voice properties
        self.engine.setProperty("voice", voices[1].id)  # Using female voice
        self.engine.setProperty("rate", 180)
        
        # Initialize speech recognizer
        self.recognizer = speech_recognition.Recognizer()
        self.recognizer.pause_threshold = 1
        self.recognizer.energy_threshold = 300
    
    def speak(self, audio):
        """Convert text to speech"""
        self.engine.say(audio)
        self.engine.runAndWait()
    
    def takeCommand(self):
        """Listen for user input and convert to text"""
        with speech_recognition.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source, 0, 4)
            
        try:
            print("Recognizing...")
            query = self.recognizer.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            print("Say that again")
            return "None"