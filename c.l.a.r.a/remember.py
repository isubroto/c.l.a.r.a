import json
import os
from datetime import datetime
from sayAndListen import SayAndListen

class RememberManager:
    def __init__(self):
        self.memory_file = 'memory.json'
        self.memories = {}
        self.speech = SayAndListen()
        self.load_memories()
    
    def load_memories(self):
        """Load saved memories from file"""
        try:
            if os.path.exists(self.memory_file):
                with open(self.memory_file, 'r') as f:
                    self.memories = json.load(f)
        except Exception as e:
            print(f"Error loading memories: {e}")
            self.memories = {}
    
    def save_memories(self):
        """Save memories to file"""
        try:
            with open(self.memory_file, 'w') as f:
                json.dump(self.memories, f, indent=4)
        except Exception as e:
            print(f"Error saving memories: {e}")
    
    def remember(self, key, value):
        """Store a new memory"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.memories[key] = {
                'value': value,
                'timestamp': timestamp
            }
            self.save_memories()
            return f"I'll remember that {key} is {value}"
        except Exception as e:
            return f"Error remembering: {str(e)}"
    
    def recall(self, key):
        """Recall a memory"""
        try:
            if key in self.memories:
                memory = self.memories[key]
                return f"{key} is {memory['value']} (remembered on {memory['timestamp']})"
            return f"I don't remember anything about {key}"
        except Exception as e:
            return f"Error recalling memory: {str(e)}"
    
    def forget(self, key):
        """Forget a memory"""
        try:
            if key in self.memories:
                del self.memories[key]
                self.save_memories()
                return f"I've forgotten about {key}"
            return f"I don't have any memory of {key}"
        except Exception as e:
            return f"Error forgetting memory: {str(e)}"
    
    def list_memories(self):
        """List all memories"""
        if not self.memories:
            return "I don't remember anything yet"
        
        memory_list = "Here's what I remember:\n"
        for key, memory in self.memories.items():
            memory_list += f"- {key}: {memory['value']} (remembered on {memory['timestamp']})\n"
        return memory_list
    
    def process_remember_command(self, command):
        """Process remember-related commands"""
        command = command.lower()
        
        if "remember" in command:
            # Extract key and value
            try:
                # Remove "remember" and split into key and value
                parts = command.replace("remember", "").strip().split(" is ", 1)
                if len(parts) == 2:
                    key, value = parts
                    return self.remember(key.strip(), value.strip())
                else:
                    return "Please specify what to remember in the format 'remember X is Y'"
            except Exception as e:
                return f"Error processing remember command: {str(e)}"
        
        elif "recall" in command or "what do you remember about" in command:
            # Extract key
            try:
                key = command.replace("recall", "").replace("what do you remember about", "").strip()
                if key:
                    return self.recall(key)
                else:
                    return "Please specify what to recall"
            except Exception as e:
                return f"Error processing recall command: {str(e)}"
        
        elif "forget" in command:
            # Extract key
            try:
                key = command.replace("forget", "").strip()
                if key:
                    return self.forget(key)
                else:
                    return "Please specify what to forget"
            except Exception as e:
                return f"Error processing forget command: {str(e)}"
        
        elif "list memories" in command:
            return self.list_memories()
        
        return "I didn't understand that remember command" 