import json
import os
import datetime
import time
import threading
from sayAndListen import SayAndListen

class ScheduleManager:
    def __init__(self):
        self.speech = SayAndListen()
        self.schedule_file = 'schedule.json'
        self.schedules = {}
        self.load_schedules()
    
    def load_schedules(self):
        """Load saved schedules from file"""
        try:
            if os.path.exists(self.schedule_file):
                with open(self.schedule_file, 'r') as f:
                    self.schedules = json.load(f)
        except Exception as e:
            print(f"Error loading schedules: {e}")
            self.schedules = {}
    
    def save_schedules(self):
        """Save schedules to file"""
        try:
            with open(self.schedule_file, 'w') as f:
                json.dump(self.schedules, f, indent=4)
        except Exception as e:
            print(f"Error saving schedules: {e}")
    
    def add_schedule(self, time_str, task, repeat_daily=False):
        """Add a new schedule entry"""
        try:
            # Parse time string (accepts formats like "7:30 AM", "19:30", etc.)
            schedule_time = datetime.datetime.strptime(time_str, "%I:%M %p").time()
            
            # Generate unique ID for schedule
            schedule_id = str(len(self.schedules) + 1)
            
            # Store schedule
            self.schedules[schedule_id] = {
                'time': schedule_time.strftime("%I:%M %p"),
                'task': task,
                'repeat_daily': repeat_daily,
                'active': True
            }
            
            self.save_schedules()
            
            # Start schedule thread
            threading.Thread(target=self._monitor_schedule, args=(schedule_id,), daemon=True).start()
            
            return f"Schedule added for {time_str}: {task}"
        except Exception as e:
            return f"Error adding schedule: {str(e)}"
    
    def _monitor_schedule(self, schedule_id):
        """Monitor and trigger schedule"""
        while True:
            try:
                if schedule_id in self.schedules and self.schedules[schedule_id]['active']:
                    schedule_time = datetime.datetime.strptime(self.schedules[schedule_id]['time'], "%I:%M %p").time()
                    current_time = datetime.datetime.now().time()
                    
                    if schedule_time.hour == current_time.hour and schedule_time.minute == current_time.minute:
                        self._trigger_schedule(schedule_id)
                        if not self.schedules[schedule_id]['repeat_daily']:
                            break
                
                time.sleep(30)  # Check every 30 seconds
            except Exception as e:
                print(f"Error monitoring schedule: {e}")
                break
    
    def _trigger_schedule(self, schedule_id):
        """Trigger schedule notification"""
        if schedule_id in self.schedules:
            task = self.schedules[schedule_id]['task']
            self.speech.speak(f"Schedule reminder: {task}")
    
    def list_schedules(self):
        """List all active schedules"""
        if not self.schedules:
            return "No schedules set"
        
        schedule_list = "Current schedules:\n"
        for schedule_id, schedule in self.schedules.items():
            if schedule['active']:
                repeat = " (repeats daily)" if schedule['repeat_daily'] else ""
                schedule_list += f"- {schedule['time']}: {schedule['task']}{repeat}\n"
        return schedule_list
    
    def delete_schedule(self, schedule_id):
        """Delete a schedule"""
        try:
            if schedule_id in self.schedules:
                del self.schedules[schedule_id]
                self.save_schedules()
                return f"Schedule {schedule_id} deleted"
            return "Schedule not found"
        except Exception as e:
            return f"Error deleting schedule: {str(e)}"
    
    def process_schedule_command(self, command):
        """Process schedule-related commands"""
        command = command.lower()
        
        if "add schedule" in command:
            # Extract time and task
            try:
                # Remove "add schedule" and split into time and task
                parts = command.replace("add schedule", "").strip().split(" for ", 1)
                if len(parts) == 2:
                    time_str, task = parts
                    # Add AM/PM if not present
                    if 'am' not in time_str.lower() and 'pm' not in time_str.lower():
                        time_str += ' AM'
                    return self.add_schedule(time_str.strip(), task.strip())
                return "Please specify time and task"
            except Exception as e:
                return f"Error processing add schedule command: {str(e)}"
        
        elif "list schedules" in command:
            return self.list_schedules()
        
        elif "delete schedule" in command:
            # Extract schedule ID
            try:
                import re
                schedule_id = re.search(r'(\d+)', command)
                if schedule_id:
                    return self.delete_schedule(schedule_id.group(1))
                return "Please specify which schedule to delete"
            except Exception as e:
                return f"Error processing delete schedule command: {str(e)}"
        
        return "I didn't understand that schedule command" 