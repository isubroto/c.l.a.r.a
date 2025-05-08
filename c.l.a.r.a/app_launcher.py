import os
import subprocess
import platform
import json
from sayAndListen import SayAndListen

class AppLauncher:
    def __init__(self):
        self.speech = SayAndListen()
        self.system = platform.system().lower()
        self.apps_file = 'apps.json'
        self.apps = {}
        self.load_apps()
    
    def load_apps(self):
        """Load saved app configurations from file"""
        try:
            if os.path.exists(self.apps_file):
                with open(self.apps_file, 'r') as f:
                    self.apps = json.load(f)
        except Exception as e:
            print(f"Error loading apps: {e}")
            self.apps = {}
    
    def save_apps(self):
        """Save app configurations to file"""
        try:
            with open(self.apps_file, 'w') as f:
                json.dump(self.apps, f, indent=4)
        except Exception as e:
            print(f"Error saving apps: {e}")
    
    def add_app(self, name, path):
        """Add a new app configuration"""
        try:
            if name in self.apps:
                return f"App '{name}' already exists"
            
            self.apps[name] = {
                'path': path,
                'system': self.system
            }
            self.save_apps()
            return f"App '{name}' added successfully"
        except Exception as e:
            return f"Error adding app: {str(e)}"
    
    def remove_app(self, name):
        """Remove an app configuration"""
        try:
            if name not in self.apps:
                return f"App '{name}' not found"
            
            del self.apps[name]
            self.save_apps()
            return f"App '{name}' removed successfully"
        except Exception as e:
            return f"Error removing app: {str(e)}"
    
    def list_apps(self):
        """List all configured apps"""
        if not self.apps:
            return "No apps configured"
        
        app_list = "Configured apps:\n"
        for name, config in self.apps.items():
            app_list += f"- {name}: {config['path']}\n"
        return app_list
    
    def open_app(self, name):
        """Open an application"""
        try:
            if name not in self.apps:
                return f"App '{name}' not found"
            
            app_config = self.apps[name]
            path = app_config['path']
            
            if self.system == "windows":
                os.startfile(path)
            elif self.system == "darwin":  # macOS
                subprocess.Popen(["open", path])
            else:  # Linux
                subprocess.Popen(["xdg-open", path])
            
            return f"Opening {name}"
        except Exception as e:
            return f"Error opening app: {str(e)}"
    
    def process_app_command(self, command):
        """Process app-related commands"""
        command = command.lower()
        
        if "add app" in command:
            # Extract app name and path
            try:
                # Remove "add app" and split into name and path
                parts = command.replace("add app", "").strip().split(" with path ", 1)
                if len(parts) == 2:
                    name, path = parts
                    return self.add_app(name.strip(), path.strip())
                return "Please specify app name and path"
            except Exception as e:
                return f"Error processing add app command: {str(e)}"
        
        elif "remove app" in command:
            # Extract app name
            name = command.replace("remove app", "").strip()
            if name:
                return self.remove_app(name)
            return "Please specify app name"
        
        elif "list apps" in command:
            return self.list_apps()
        
        elif "open" in command:
            # Extract app name
            name = command.replace("open", "").strip()
            if name:
                return self.open_app(name)
            return "Please specify app name"
        
        return "I didn't understand that app command" 