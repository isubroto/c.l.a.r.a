import datetime
import time
import threading
import json
import os
from sayAndListen import SayAndListen

class AlarmManager:
    def __init__(self):
        self.alarms = {}
        self.speech = SayAndListen()
        self.alarm_file = 'alarms.json'
        self.load_alarms()
        
    def load_alarms(self):
        """Load saved alarms from file"""
        try:
            if os.path.exists(self.alarm_file):
                with open(self.alarm_file, 'r') as f:
                    self.alarms = json.load(f)
        except Exception as e:
            print(f"Error loading alarms: {e}")
            self.alarms = {}
    
    def save_alarms(self):
        """Save alarms to file"""
        try:
            with open(self.alarm_file, 'w') as f:
                json.dump(self.alarms, f, indent=4)
        except Exception as e:
            print(f"Error saving alarms: {e}")
    
    def set_alarm(self, time_str, label=None):
        """Set a new alarm"""
        try:
            # Parse time string (accepts formats like "7:30 AM", "19:30", etc.)
            alarm_time = datetime.datetime.strptime(time_str, "%I:%M %p").time()
            current_time = datetime.datetime.now().time()
            
            # Create alarm datetime
            alarm_datetime = datetime.datetime.combine(datetime.date.today(), alarm_time)
            if alarm_time < current_time:
                alarm_datetime += datetime.timedelta(days=1)
            
            # Generate unique ID for alarm
            alarm_id = str(len(self.alarms) + 1)
            
            # Store alarm
            self.alarms[alarm_id] = {
                'time': alarm_datetime.strftime("%I:%M %p"),
                'label': label or f"Alarm {alarm_id}",
                'active': True
            }
            
            self.save_alarms()
            
            # Start alarm thread
            threading.Thread(target=self._monitor_alarm, args=(alarm_id,), daemon=True).start()
            
            return f"Alarm set for {time_str}"
        except Exception as e:
            return f"Error setting alarm: {str(e)}"
    
    def _monitor_alarm(self, alarm_id):
        """Monitor and trigger alarm"""
        while True:
            try:
                if alarm_id in self.alarms and self.alarms[alarm_id]['active']:
                    alarm_time = datetime.datetime.strptime(self.alarms[alarm_id]['time'], "%I:%M %p").time()
                    current_time = datetime.datetime.now().time()
                    
                    if alarm_time.hour == current_time.hour and alarm_time.minute == current_time.minute:
                        self._trigger_alarm(alarm_id)
                        break
                
                time.sleep(30)  # Check every 30 seconds
            except Exception as e:
                print(f"Error monitoring alarm: {e}")
                break
    
    def _trigger_alarm(self, alarm_id):
        """Trigger alarm notification"""
        if alarm_id in self.alarms:
            label = self.alarms[alarm_id]['label']
            self.speech.speak(f"Alarm! {label}")
            # You can add more notification methods here (e.g., system notification, sound)
    
    def list_alarms(self):
        """List all active alarms"""
        if not self.alarms:
            return "No alarms set"
        
        alarm_list = "Current alarms:\n"
        for alarm_id, alarm in self.alarms.items():
            if alarm['active']:
                alarm_list += f"- {alarm['label']} at {alarm['time']}\n"
        return alarm_list
    
    def cancel_alarm(self, alarm_id):
        """Cancel an alarm"""
        if alarm_id in self.alarms:
            del self.alarms[alarm_id]
            self.save_alarms()
            return f"Alarm {alarm_id} cancelled"
        return "Alarm not found"
    
    def process_alarm_command(self, command):
        """Process alarm-related commands"""
        command = command.lower()
        
        if "set alarm" in command:
            # Extract time from command
            try:
                # Look for time patterns like "7:30 AM" or "7:30"
                import re
                time_match = re.search(r'(\d{1,2}:\d{2}(?:\s*[AaPp][Mm])?)', command)
                if time_match:
                    time_str = time_match.group(1)
                    # Add AM/PM if not present
                    if 'am' not in time_str.lower() and 'pm' not in time_str.lower():
                        time_str += ' AM'
                    return self.set_alarm(time_str)
                else:
                    return "Please specify a time for the alarm"
            except Exception as e:
                return f"Error setting alarm: {str(e)}"
        
        elif "list alarms" in command:
            return self.list_alarms()
        
        elif "cancel alarm" in command:
            # Extract alarm ID or label
            try:
                import re
                alarm_id = re.search(r'(\d+)', command)
                if alarm_id:
                    return self.cancel_alarm(alarm_id.group(1))
                else:
                    return "Please specify which alarm to cancel"
            except Exception as e:
                return f"Error cancelling alarm: {str(e)}"
        
        return "I didn't understand that alarm command" 