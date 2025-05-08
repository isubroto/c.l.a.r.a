import speech_recognition
import time

class HotwordDetector:
    def __init__(self):
        # Initialize speech recognizer with optimized settings
        self.recognizer = speech_recognition.Recognizer()
        self.recognizer.energy_threshold = 4000  # Increased for better detection
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.dynamic_energy_adjustment_damping = 0.15
        self.recognizer.dynamic_energy_ratio = 1.5
        self.recognizer.pause_threshold = 0.8
        self.recognizer.phrase_threshold = 0.3
        self.recognizer.non_speaking_duration = 0.3
        
        # Wake words to detect
        self.wake_words = ["hey clara", "hi clara", "hello clara", "clara"]
        
        # Calibration settings
        self.calibration_done = False
    
    def adjust_for_ambient_noise(self, source):
        """One-time calibration for ambient noise"""
        if self.calibration_done:
            return
            
        try:
            print("Initial microphone calibration...")
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
            self.calibration_done = True
            print("Microphone calibrated successfully")
        except Exception as e:
            print(f"Calibration error: {str(e)}")
    
    def start_listening(self):
        """Continuous listening for wake word"""
        print("Listening for wake word 'Hey Clara'...")
        
        while True:
            try:
                with speech_recognition.Microphone() as source:
                    # One-time calibration
                    if not self.calibration_done:
                        self.adjust_for_ambient_noise(source)
                    
                    print("Listening...")
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    
                    try:
                        text = self.recognizer.recognize_google(audio, language="en-in").lower()
                        print(f"Heard: {text}")
                        
                        # More robust wake word detection
                        # Accept if 'clara' is present, or if any wake word is close
                        if "clara" in text:
                            print("Wake word detected (clara found)!")
                            return True
                        # Accept common misrecognitions
                        for wake_word in self.wake_words:
                            if wake_word in text:
                                print(f"Wake word detected ({wake_word} found)!")
                                return True
                        # Accept if text starts with something like 'hay', 'hey', 'hi' followed by anything close to 'clara'
                        for prefix in ["hay", "hey", "hi", "hello"]:
                            if text.startswith(prefix):
                                if "clara" in text:
                                    print(f"Wake word detected (prefix {prefix} + clara)!")
                                    return True
                            
                    except speech_recognition.UnknownValueError:
                        pass
                    except speech_recognition.RequestError as e:
                        print(f"Could not request results: {str(e)}")
                        
            except speech_recognition.WaitTimeoutError:
                continue
            except Exception as e:
                print(f"Error in listening loop: {str(e)}")
                time.sleep(1)
                continue 