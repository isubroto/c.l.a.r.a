import speech_recognition
import time
from sayAndListen import SayAndListen

class HotwordDetector:
    def __init__(self):
        # Initialize speech recognizer with optimized settings
        self.recognizer = speech_recognition.Recognizer()
        self.recognizer.energy_threshold = 3000  # Lowered for better sensitivity
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.dynamic_energy_adjustment_damping = 0.15
        self.recognizer.dynamic_energy_ratio = 1.2
        self.recognizer.pause_threshold = 0.5  # Reduced for faster response
        self.recognizer.phrase_threshold = 0.3
        self.recognizer.non_speaking_duration = 0.3
        
        # Initialize speech interface
        self.speech = SayAndListen()
        
        # Wake words to detect
        self.wake_words = [
            "hey clara",
            "hi clara",
            "hello clara",
            "clara",
            "hey pra",  # Common misrecognition
            "hi pra",
            "hello pra"
        ]
        
        # Calibration settings
        self.calibration_done = False
        
        # Debug mode
        self.debug = True
    
    def adjust_for_ambient_noise(self, source):
        """One-time calibration for ambient noise"""
        if self.calibration_done:
            return
            
        try:
            print("Initial microphone calibration...")
            self.speech.speak("Calibrating microphone...")
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
            self.calibration_done = True
            print("Microphone calibrated successfully")
            self.speech.speak("Microphone calibrated and ready!")
        except Exception as e:
            print(f"Calibration error: {str(e)}")
            self.speech.speak("Error calibrating microphone. Please check your audio settings.")
    
    def is_wake_word(self, text):
        """Check if the text contains a wake word"""
        text = text.lower()
        
        # Direct wake word match
        if any(wake_word in text for wake_word in self.wake_words):
            return True
            
        # Check for common misrecognitions
        if "clara" in text or "pra" in text:
            # Check if it's preceded by a greeting
            for prefix in ["hey", "hi", "hello", "hay"]:
                if text.startswith(prefix):
                    return True
                    
        return False
    
    def start_listening(self):
        """Continuous listening for wake word"""
        print("Listening for wake word 'Hey Clara'...")
        self.speech.speak("I'm listening for 'Hey Clara'")
        
        while True:
            try:
                with speech_recognition.Microphone() as source:
                    # One-time calibration
                    if not self.calibration_done:
                        self.adjust_for_ambient_noise(source)
                    
                    if self.debug:
                        print("Listening...")
                    
                    # Reduced timeout for faster response
                    audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=3)
                    
                    try:
                        text = self.recognizer.recognize_google(audio, language="en-in").lower()
                        if self.debug:
                            print(f"Heard: {text}")
                        
                        if self.is_wake_word(text):
                            if self.debug:
                                print("Wake word detected!")
                            self.speech.speak("Yes, I'm listening!")
                            return True
                            
                    except speech_recognition.UnknownValueError:
                        if self.debug:
                            print("Could not understand audio")
                    except speech_recognition.RequestError as e:
                        print(f"Could not request results: {str(e)}")
                        self.speech.speak("I'm having trouble connecting to the speech recognition service.")
                        
            except speech_recognition.WaitTimeoutError:
                continue
            except Exception as e:
                print(f"Error in listening loop: {str(e)}")
                time.sleep(1)
                continue 