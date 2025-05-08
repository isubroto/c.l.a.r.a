import pyautogui
import time
import webbrowser
from sayAndListen import SayAndListen

class YouTubeController:
    def __init__(self):
        self.speech = SayAndListen()
        self.youtube_url = "https://www.youtube.com"
        self.is_playing = False
        
    def open_youtube(self):
        """Open YouTube in default browser"""
        try:
            webbrowser.open(self.youtube_url)
            return "Opening YouTube"
        except Exception as e:
            return f"Error opening YouTube: {str(e)}"
    
    def play_pause(self):
        """Toggle play/pause"""
        try:
            pyautogui.press('k')  # YouTube's keyboard shortcut for play/pause
            self.is_playing = not self.is_playing
            return "Paused" if not self.is_playing else "Playing"
        except Exception as e:
            return f"Error controlling playback: {str(e)}"
    
    def next_video(self):
        """Play next video"""
        try:
            pyautogui.press('shift+n')  # YouTube's keyboard shortcut for next video
            return "Playing next video"
        except Exception as e:
            return f"Error playing next video: {str(e)}"
    
    def previous_video(self):
        """Play previous video"""
        try:
            pyautogui.press('shift+p')  # YouTube's keyboard shortcut for previous video
            return "Playing previous video"
        except Exception as e:
            return f"Error playing previous video: {str(e)}"
    
    def volume_up(self):
        """Increase volume"""
        try:
            pyautogui.press('up')
            return "Volume increased"
        except Exception as e:
            return f"Error adjusting volume: {str(e)}"
    
    def volume_down(self):
        """Decrease volume"""
        try:
            pyautogui.press('down')
            return "Volume decreased"
        except Exception as e:
            return f"Error adjusting volume: {str(e)}"
    
    def mute(self):
        """Toggle mute"""
        try:
            pyautogui.press('m')
            return "Muted" if not self.is_playing else "Unmuted"
        except Exception as e:
            return f"Error toggling mute: {str(e)}"
    
    def fullscreen(self):
        """Toggle fullscreen"""
        try:
            pyautogui.press('f')
            return "Toggled fullscreen"
        except Exception as e:
            return f"Error toggling fullscreen: {str(e)}"
    
    def search_video(self, query):
        """Search for a video"""
        try:
            # Open YouTube
            webbrowser.open(self.youtube_url)
            time.sleep(2)  # Wait for page to load
            
            # Click search box and type query
            pyautogui.hotkey('ctrl', 'l')  # Focus on address bar
            pyautogui.write(f"{self.youtube_url}/results?search_query={query.replace(' ', '+')}")
            pyautogui.press('enter')
            return f"Searching for {query}"
        except Exception as e:
            return f"Error searching video: {str(e)}"
    
    def process_youtube_command(self, command):
        """Process YouTube-related commands"""
        command = command.lower()
        
        if "open youtube" in command:
            return self.open_youtube()
        
        elif "play" in command or "pause" in command:
            return self.play_pause()
        
        elif "next video" in command:
            return self.next_video()
        
        elif "previous video" in command:
            return self.previous_video()
        
        elif "volume up" in command:
            return self.volume_up()
        
        elif "volume down" in command:
            return self.volume_down()
        
        elif "mute" in command:
            return self.mute()
        
        elif "fullscreen" in command:
            return self.fullscreen()
        
        elif "search" in command:
            # Extract search query
            query = command.replace("search", "").strip()
            if query:
                return self.search_video(query)
            return "Please specify what to search for"
        
        return "I didn't understand that YouTube command" 