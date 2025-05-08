import os
import platform
import subprocess
import time
from sayAndListen import SayAndListen

class SystemController:
    def __init__(self):
        self.speech = SayAndListen()
        self.system = platform.system().lower()
    
    def shutdown(self, delay=0):
        """Shutdown the system"""
        try:
            if self.system == "windows":
                os.system(f"shutdown /s /t {delay}")
            elif self.system == "linux":
                os.system(f"shutdown -h {delay}")
            elif self.system == "darwin":  # macOS
                os.system(f"shutdown -h +{delay}")
            return f"System will shutdown in {delay} seconds"
        except Exception as e:
            return f"Error shutting down system: {str(e)}"
    
    def restart(self, delay=0):
        """Restart the system"""
        try:
            if self.system == "windows":
                os.system(f"shutdown /r /t {delay}")
            elif self.system == "linux":
                os.system(f"shutdown -r {delay}")
            elif self.system == "darwin":  # macOS
                os.system(f"shutdown -r +{delay}")
            return f"System will restart in {delay} seconds"
        except Exception as e:
            return f"Error restarting system: {str(e)}"
    
    def cancel_shutdown(self):
        """Cancel a scheduled shutdown/restart"""
        try:
            if self.system == "windows":
                os.system("shutdown /a")
            elif self.system == "linux":
                os.system("shutdown -c")
            elif self.system == "darwin":  # macOS
                os.system("killall shutdown")
            return "Shutdown/restart cancelled"
        except Exception as e:
            return f"Error cancelling shutdown: {str(e)}"
    
    def sleep(self):
        """Put system to sleep"""
        try:
            if self.system == "windows":
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            elif self.system == "linux":
                os.system("systemctl suspend")
            elif self.system == "darwin":  # macOS
                os.system("pmset sleepnow")
            return "Putting system to sleep"
        except Exception as e:
            return f"Error putting system to sleep: {str(e)}"
    
    def hibernate(self):
        """Hibernate the system"""
        try:
            if self.system == "windows":
                os.system("rundll32.exe powrprof.dll,SetSuspendState 1,1,0")
            elif self.system == "linux":
                os.system("systemctl hibernate")
            elif self.system == "darwin":  # macOS
                os.system("pmset sleepnow")
            return "Hibernating system"
        except Exception as e:
            return f"Error hibernating system: {str(e)}"
    
    def get_system_info(self):
        """Get system information"""
        try:
            info = f"Operating System: {platform.system()} {platform.release()}\n"
            info += f"Architecture: {platform.machine()}\n"
            info += f"Processor: {platform.processor()}\n"
            info += f"Python Version: {platform.python_version()}"
            return info
        except Exception as e:
            return f"Error getting system info: {str(e)}"
    
    def process_system_command(self, command):
        """Process system-related commands"""
        command = command.lower()
        
        if "shutdown" in command:
            # Extract delay if specified
            try:
                import re
                delay_match = re.search(r'(\d+)', command)
                delay = int(delay_match.group(1)) if delay_match else 0
                return self.shutdown(delay)
            except Exception as e:
                return f"Error processing shutdown command: {str(e)}"
        
        elif "restart" in command:
            # Extract delay if specified
            try:
                import re
                delay_match = re.search(r'(\d+)', command)
                delay = int(delay_match.group(1)) if delay_match else 0
                return self.restart(delay)
            except Exception as e:
                return f"Error processing restart command: {str(e)}"
        
        elif "cancel shutdown" in command or "cancel restart" in command:
            return self.cancel_shutdown()
        
        elif "sleep" in command:
            return self.sleep()
        
        elif "hibernate" in command:
            return self.hibernate()
        
        elif "system info" in command:
            return self.get_system_info()
        
        return "I didn't understand that system command" 