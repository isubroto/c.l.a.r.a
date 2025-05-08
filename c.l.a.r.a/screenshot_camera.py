import pyautogui
import cv2
import os
from datetime import datetime
from sayAndListen import SayAndListen

class ScreenshotCamera:
    def __init__(self):
        self.speech = SayAndListen()
        self.screenshot_dir = 'screenshots'
        self.photo_dir = 'photos'
        self._create_directories()
    
    def _create_directories(self):
        """Create directories for screenshots and photos"""
        try:
            if not os.path.exists(self.screenshot_dir):
                os.makedirs(self.screenshot_dir)
            if not os.path.exists(self.photo_dir):
                os.makedirs(self.photo_dir)
        except Exception as e:
            print(f"Error creating directories: {e}")
    
    def take_screenshot(self, region=None):
        """Take a screenshot"""
        try:
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(self.screenshot_dir, f"screenshot_{timestamp}.png")
            
            # Take screenshot
            if region:
                screenshot = pyautogui.screenshot(region=region)
            else:
                screenshot = pyautogui.screenshot()
            
            # Save screenshot
            screenshot.save(filename)
            
            return f"Screenshot saved as {filename}"
        except Exception as e:
            return f"Error taking screenshot: {str(e)}"
    
    def take_photo(self):
        """Take a photo using the camera"""
        try:
            # Initialize camera
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                return "Error: Could not open camera"
            
            # Read frame
            ret, frame = cap.read()
            if not ret:
                return "Error: Could not read frame"
            
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(self.photo_dir, f"photo_{timestamp}.jpg")
            
            # Save photo
            cv2.imwrite(filename, frame)
            
            # Release camera
            cap.release()
            
            return f"Photo saved as {filename}"
        except Exception as e:
            return f"Error taking photo: {str(e)}"
    
    def process_camera_command(self, command):
        """Process camera-related commands"""
        command = command.lower()
        
        if "screenshot" in command:
            return self.take_screenshot()
        
        elif "photo" in command or "picture" in command:
            return self.take_photo()
        
        return "I didn't understand that camera command" 