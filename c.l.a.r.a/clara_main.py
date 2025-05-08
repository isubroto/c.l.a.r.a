import datetime
import webbrowser
import os
import smtplib
import random
import json
from command_handler import CommandHandler
from responses import ResponseGenerator
from learning import ClaraLearning
from weather import get_weather
from temperature import TemperatureInfo
from web_search import WebSearch
from sayAndListen import SayAndListen
from hotword_detector import HotwordDetector
import time

class Clara:
    def __init__(self):
        # Initialize speech interface
        self.speech = SayAndListen()
        
        # Initialize hotword detector
        self.hotword_detector = HotwordDetector()
        
        # Initialize command handler and learning system
        self.command_handler = CommandHandler()
        self.response_gen = ResponseGenerator()
        self.clara_learning = ClaraLearning()
        self.temperature_info = TemperatureInfo()
        self.web_search = WebSearch()
        
        # Load user preferences
        self.load_preferences()
        
        # Welcome message
        self.speech.speak("Hello! I'm Clara, your personal assistant. How can I help you today?")
    
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
                    'rate': 180,
                    'volume': 1.0
                }
            }
            self.save_preferences()
    
    def save_preferences(self):
        """Save user preferences to file"""
        with open('user_preferences.json', 'w') as f:
            json.dump(self.preferences, f, indent=4)
    
    def process_command(self, query):
        """Process user command and generate response"""
        if not query or query == "None":
            return
            
        # Check for wake word
        if self.command_handler.handle_wake_commands(query):
            self.speech.speak("Hello! I'm awake and ready to help.")
            return True
            
        # Process the command
        response, is_command = self.command_handler.process_command(query)
        
        if response == "weather":
            # Handle weather command
            weather_info = get_weather(query)
            if weather_info:
                self.speech.speak(weather_info)
            else:
                self.speech.speak("I couldn't get the weather information at the moment.")
        elif response == "temperature":
            # Handle temperature command
            temp_info = self.temperature_info.process_temperature_command(query)
            self.speech.speak(temp_info)
        elif response == "search":
            # Handle web search command
            self.web_search.process_search_command(query)
        elif response == "news":
            # Handle news command
            self.speech.speak("I'll get the latest news for you.")
            # Add news module integration here
            self.speech.speak("Here are the latest headlines...")  # Placeholder for news integration
        else:
            # For all other responses, speak them directly
            self.speech.speak(response)
            
        return is_command
    
    def run(self):
        """Main loop for Clara with improved listening"""
        print("Clara is ready! Say 'Hey Clara' to begin.")
        self.speech.speak("I'm ready to help! Say Hey Clara to begin.")
        
        while True:
            try:
                # Start continuous listening for wake word
                if self.hotword_detector.start_listening():
                    self.speech.speak("Yes, I'm listening!")
                    
                    # Continuous command listening loop
                    while True:
                        try:
                            # Get command
                            query = self.speech.takeCommand()
                            if query:
                                print(f"Command received: {query}")
                                
                                # Check for sleep command
                                if self.command_handler.handle_sleep_commands(query):
                                    self.speech.speak(self.response_gen.get_sleep_response())
                                    break  # Break inner loop to return to wake word detection
                                    
                                # Process the command
                                self.process_command(query)
                                
                                # Brief pause before next command
                                time.sleep(0.2)
                            
                        except Exception as e:
                            print(f"Error processing command: {str(e)}")
                            continue
                
            except Exception as e:
                print(f"Error in main loop: {str(e)}")
                time.sleep(1)  # Brief pause on error
                continue
    
if __name__ == "__main__":
    clara = Clara()
    clara.run()

