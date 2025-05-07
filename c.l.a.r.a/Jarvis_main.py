import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib
import random
import json
import threading
from command_handler import CommandHandler
from responses import ResponseGenerator
from learning import JarvisLearning
from weather import get_weather

class Jarvis:
    def __init__(self):
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)
        
        # Initialize voice
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        
        # Initialize command handler and learning system
        self.command_handler = CommandHandler()
        self.response_gen = ResponseGenerator()
        self.jarvis_learning = JarvisLearning()
        
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Adjust for ambient noise
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
        
        # Load user preferences
        self.load_preferences()
        
        # Initialize threading for concurrent operations
        self.speech_thread = None
        self.is_speaking = False
        
    def load_preferences(self):
        """Load user preferences from file"""
        try:
            with open('user_preferences.json', 'r') as f:
                self.preferences = json.load(f)
        except FileNotFoundError:
            self.preferences = {
                'name': 'User',
                'email': '',
                'weather_location': 'London',
                'news_preferences': ['technology', 'science'],
                'voice_preferences': {
                    'rate': 150,
                    'volume': 1.0
                }
            }
            self.save_preferences()
    
    def save_preferences(self):
        """Save user preferences to file"""
        with open('user_preferences.json', 'w') as f:
            json.dump(self.preferences, f, indent=4)
    
    def speak(self, text):
        """Convert text to speech using threading for non-blocking operation"""
        print(f"Jarvis: {text}")
        
        # If already speaking, wait for current speech to finish
        if self.is_speaking and self.speech_thread and self.speech_thread.is_alive():
            self.speech_thread.join()
        
        def speak_thread():
            self.is_speaking = True
            self.engine.say(text)
            self.engine.runAndWait()
            self.is_speaking = False
        
        self.speech_thread = threading.Thread(target=speak_thread)
        self.speech_thread.start()
    
    def listen(self):
        """Listen for user input with improved error handling"""
        with self.microphone as source:
            print("Listening...")
            try:
                # Adjust for ambient noise before each listen
                self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                
                # Set timeout and phrase time limit for faster response
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                
                try:
                    text = self.recognizer.recognize_google(audio)
                    print(f"User: {text}")
                    return text.lower()
                except sr.UnknownValueError:
                    return ""
                except sr.RequestError:
                    self.speak("Sorry, I'm having trouble connecting to the speech recognition service.")
                    return ""
            except sr.WaitTimeoutError:
                return ""
    
    def process_command(self, query):
        """Process user command and generate response"""
        if not query:
            return
            
        # Check for wake word
        if self.command_handler.handle_wake_commands(query):
            self.speak("Hello! I'm awake and ready to help.")
            return True
            
        # Process the command
        response, is_command = self.command_handler.process_command(query)
        
        if response == "weather":
            # Handle weather command
            weather_info = get_weather(query)
            if weather_info:
                self.speak(weather_info)
            else:
                self.speak("I couldn't get the weather information at the moment.")
        elif response == "news":
            # Handle news command
            self.speak("I'll get the latest news for you.")
            # Add news module integration here
            self.speak("Here are the latest headlines...")  # Placeholder for news integration
        else:
            # For all other responses, speak them directly
            self.speak(response)
            
        return is_command
    
    def run(self):
        """Main loop for Jarvis with improved responsiveness"""
        self.speak("Hello! I'm Jarvis, your personal assistant. How can I help you today?")
        
        while True:
            query = self.listen()
            if query:
                if self.command_handler.handle_sleep_commands(query):
                    self.speak(self.response_gen.get_sleep_response())
                    break
                self.process_command(query)
    
if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.run()

