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
from alarm import AlarmManager
from youtube_controls import YouTubeController
from remember import RememberManager
from playlist import PlaylistManager
from calculator import Calculator
from whatsapp import WhatsAppController
from system_control import SystemController
from password_protection import PasswordManager
from schedule import ScheduleManager
from app_launcher import AppLauncher
from speed_test import SpeedTester
from ipl_score import IPLScore
from rock_paper_scissors import RockPaperScissors
from screenshot_camera import ScreenshotCamera
from translator import GoogleTranslator
import time

class Clara:
    def __init__(self):
        # Initialize speech interface
        self.speech = SayAndListen()
        
        # Initialize hotword detector
        self.hotword_detector = HotwordDetector()
        
        # Initialize core components
        self.command_handler = CommandHandler()
        self.response_gen = ResponseGenerator()
        self.clara_learning = ClaraLearning()
        self.temperature_info = TemperatureInfo()
        self.web_search = WebSearch()
        
        # Initialize feature managers
        self.alarm_manager = AlarmManager()
        self.youtube_controller = YouTubeController()
        self.remember_manager = RememberManager()
        self.playlist_manager = PlaylistManager()
        self.calculator = Calculator()
        self.whatsapp_controller = WhatsAppController()
        self.system_controller = SystemController()
        self.password_manager = PasswordManager()
        self.schedule_manager = ScheduleManager()
        self.app_launcher = AppLauncher()
        self.speed_tester = SpeedTester()
        self.ipl_score = IPLScore()
        self.rock_paper_scissors = RockPaperScissors()
        self.screenshot_camera = ScreenshotCamera()
        self.translator = GoogleTranslator()
        
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
            response = "Hello! I'm awake and ready to help."
            self.speech.speak(response)
            self.clara_learning.learn_from_command(query, response, True)
            return True
        
        # Process feature-specific commands
        if "alarm" in query.lower():
            response = self.alarm_manager.process_alarm_command(query)
            self.speech.speak(response)
            self.clara_learning.learn_from_command(query, response, True)
            return True
            
        elif "youtube" in query.lower():
            response = self.youtube_controller.process_youtube_command(query)
            self.speech.speak(response)
            self.clara_learning.learn_from_command(query, response, True)
            return True
            
        elif "remember" in query.lower() or "recall" in query.lower():
            response = self.remember_manager.process_remember_command(query)
            self.speech.speak(response)
            self.clara_learning.learn_from_command(query, response, True)
            return True
            
        elif "playlist" in query.lower():
            response = self.playlist_manager.process_playlist_command(query)
            self.speech.speak(response)
            self.clara_learning.learn_from_command(query, response, True)
            return True
            
        elif "calculate" in query.lower() or "what is" in query.lower():
            response = self.calculator.process_calculator_command(query)
            self.speech.speak(response)
            self.clara_learning.learn_from_command(query, response, True)
            return True
            
        elif "whatsapp" in query.lower():
            response = self.whatsapp_controller.process_whatsapp_command(query)
            self.speech.speak(response)
            self.clara_learning.learn_from_command(query, response, True)
            return True
            
        elif any(word in query.lower() for word in ["shutdown", "restart", "sleep", "system"]):
            response = self.system_controller.process_system_command(query)
            self.speech.speak(response)
            self.clara_learning.learn_from_command(query, response, True)
            return True
            
        elif "password" in query.lower():
            response = self.password_manager.process_password_command(query)
            self.speech.speak(response)
            self.clara_learning.learn_from_command(query, response, True)
            return True
            
        elif "schedule" in query.lower():
            response = self.schedule_manager.process_schedule_command(query)
            self.speech.speak(response)
            self.clara_learning.learn_from_command(query, response, True)
            return True
            
        elif "app" in query.lower() or "open" in query.lower():
            response = self.app_launcher.process_app_command(query)
            self.speech.speak(response)
            self.clara_learning.learn_from_command(query, response, True)
            return True
            
        elif "speed" in query.lower() or "test internet" in query.lower():
            response = self.speed_tester.process_speed_command(query)
            self.speech.speak(response)
            self.clara_learning.learn_from_command(query, response, True)
            return True
            
        elif "ipl" in query.lower() or "cricket" in query.lower():
            response = self.ipl_score.process_ipl_command(query)
            self.speech.speak(response)
            self.clara_learning.learn_from_command(query, response, True)
            return True
            
        elif "rock" in query.lower() or "paper" in query.lower() or "scissors" in query.lower():
            response = self.rock_paper_scissors.process_game_command(query)
            self.speech.speak(response)
            self.clara_learning.learn_from_command(query, response, True)
            return True
            
        elif "screenshot" in query.lower() or "photo" in query.lower() or "picture" in query.lower():
            response = self.screenshot_camera.process_camera_command(query)
            self.speech.speak(response)
            self.clara_learning.learn_from_command(query, response, True)
            return True
            
        elif "translate" in query.lower() or "language" in query.lower():
            response = self.translator.process_translator_command(query)
            self.speech.speak(response)
            self.clara_learning.learn_from_command(query, response, True)
            return True
            
        # Process core commands
        response, is_command = self.command_handler.process_command(query)
        
        if response == "weather":
            weather_info = get_weather(query)
            if weather_info:
                self.speech.speak(weather_info)
                self.clara_learning.learn_from_command(query, weather_info, True)
            else:
                error_msg = "I couldn't get the weather information at the moment."
                self.speech.speak(error_msg)
                self.clara_learning.learn_from_command(query, error_msg, False)
        elif response == "temperature":
            temp_info = self.temperature_info.process_temperature_command(query)
            self.speech.speak(temp_info)
            self.clara_learning.learn_from_command(query, temp_info, True)
        elif response == "search":
            search_result = self.web_search.process_search_command(query)
            self.speech.speak(search_result)
            self.clara_learning.learn_from_command(query, search_result, True)
        elif response == "news":
            self.speech.speak("I'll get the latest news for you.")
            news_msg = "Here are the latest headlines..."  # Placeholder for news integration
            self.speech.speak(news_msg)
            self.clara_learning.learn_from_command(query, news_msg, True)
        else:
            self.speech.speak(response)
            self.clara_learning.learn_from_command(query, response, True)
            
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

