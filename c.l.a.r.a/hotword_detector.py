import speech_recognition
import time
import numpy as np
from collections import deque

class HotwordDetector:
    def __init__(self):
        # Initialize speech recognizer with optimized settings
        self.recognizer = speech_recognition.Recognizer()
        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.dynamic_energy_adjustment_damping = 0.15
        self.recognizer.dynamic_energy_ratio = 1.5
        self.recognizer.pause_threshold = 0.5
        self.recognizer.phrase_threshold = 0.3
        self.recognizer.non_speaking_duration = 0.3
        
        # Wake words to detect
        self.wake_words = {
            "hey clara": ["hey clara", "hi clara", "hello clara", "hi", "hello", "hey"],
            "wake up": ["wake up clara", "wake up", "start clara", "activate clara"],
            "clara": ["clara", "clara wake up", "clara start", "clara activate"]
        }
        
        # Calibration settings
        self.calibration_done = False
        self.last_calibration_time = 0
        self.calibration_cooldown = 300  # 5 minutes between calibrations
        
        # Performance settings
        self.min_detection_interval = 0.3
        self.last_detection_time = 0
    
    def adjust_for_ambient_noise(self, source):
        """One-time calibration for ambient noise"""
        if self.calibration_done:
            return
            
        try:
            print("Initial microphone calibration...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            self.calibration_done = True
            self.last_calibration_time = time.time()
            print("Microphone calibrated successfully")
        except Exception as e:
            print(f"Calibration error: {str(e)}")
    
    def detect_wake_word(self):
        """Detect wake word with improved reliability"""
        with speech_recognition.Microphone() as source:
            # One-time calibration
            if not self.calibration_done:
                self.adjust_for_ambient_noise(source)
            
            try:
                # Listen for audio with shorter timeout
                audio = self.recognizer.listen(source, timeout=0.8, phrase_time_limit=1.5)
                
                try:
                    # Convert speech to text
                    text = self.recognizer.recognize_google(audio, language="en-in").lower()
                    print(f"Heard: {text}")
                    
                    # Check for wake words
                    for wake_word, variations in self.wake_words.items():
                        if any(variation in text for variation in variations):
                            current_time = time.time()
                            if current_time - self.last_detection_time >= self.min_detection_interval:
                                self.last_detection_time = current_time
                                print("Wake word detected!")
                                return True
                    
                except speech_recognition.UnknownValueError:
                    pass
                except speech_recognition.RequestError:
                    print("Could not request results from speech recognition service")
                    
            except speech_recognition.WaitTimeoutError:
                pass
                
        return False
    
    def start_listening(self):
        """Continuous listening for wake word"""
        print("Listening for wake word 'Hey Clara'...")
        
        while True:
            try:
                if self.detect_wake_word():
                    return True
                time.sleep(0.1)  # Short sleep to prevent CPU overuse
            except Exception as e:
                print(f"Error in listening loop: {str(e)}")
                time.sleep(0.5)  # Longer sleep on error
                continue 