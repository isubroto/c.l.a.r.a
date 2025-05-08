import json
import os
from datetime import datetime
import random
from collections import defaultdict
from sayAndListen import SayAndListen

class ClaraLearning:
    def __init__(self):
        self.speech = SayAndListen()
        self.learned_commands = {}
        self.conversation_history = []
        self.max_history = 100
        self.learning_file = 'learning_data.json'
        self.command_history = []
        self.user_preferences = {}
        self.command_patterns = {}
        self.response_patterns = {}
        self.load_learning_data()
        self.conversation_file = "jarvis_conversations.json"
        self.learned_responses = self._load_learned_responses()
        self.conversations = self._load_conversations()
        self.emotion_patterns = {
            'happy': ['good', 'great', 'excellent', 'wonderful', 'amazing', 'love', 'happy'],
            'sad': ['sad', 'bad', 'terrible', 'awful', 'sorry', 'unfortunate', 'upset'],
            'angry': ['angry', 'mad', 'furious', 'annoyed', 'irritated', 'frustrated'],
            'neutral': ['okay', 'fine', 'alright', 'normal', 'usual']
        }
        self.personality_traits = {
            'formality': 0.7,  # 0-1 scale, higher means more formal
            'humor': 0.6,      # 0-1 scale, higher means more humorous
            'empathy': 0.8,    # 0-1 scale, higher means more empathetic
            'proactivity': 0.5 # 0-1 scale, higher means more proactive
        }
        
    def load_learning_data(self):
        """Load learning data from file"""
        try:
            if os.path.exists(self.learning_file):
                with open(self.learning_file, 'r') as f:
                    data = json.load(f)
                    self.command_history = data.get('command_history', [])
                    self.user_preferences = data.get('user_preferences', {})
                    self.command_patterns = data.get('command_patterns', {})
                    self.response_patterns = data.get('response_patterns', {})
        except Exception as e:
            print(f"Error loading learning data: {e}")
    
    def save_learning_data(self):
        """Save learning data to file"""
        try:
            data = {
                'command_history': self.command_history,
                'user_preferences': self.user_preferences,
                'command_patterns': self.command_patterns,
                'response_patterns': self.response_patterns
            }
            with open(self.learning_file, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error saving learning data: {e}")
    
    def learn_from_command(self, command, response, success=True):
        """Learn from a command interaction"""
        try:
            # Record command in history
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.command_history.append({
                'command': command,
                'response': response,
                'success': success,
                'timestamp': timestamp
            })
            
            # Keep only last 1000 commands
            if len(self.command_history) > 1000:
                self.command_history = self.command_history[-1000:]
            
            # Learn command patterns
            words = command.lower().split()
            for i in range(len(words) - 1):
                pattern = f"{words[i]} {words[i+1]}"
                if pattern not in self.command_patterns:
                    self.command_patterns[pattern] = 1
                else:
                    self.command_patterns[pattern] += 1
            
            # Learn response patterns
            if success:
                if response not in self.response_patterns:
                    self.response_patterns[response] = 1
                else:
                    self.response_patterns[response] += 1
            
            # Save learning data
            self.save_learning_data()
            
            return True
        except Exception as e:
            print(f"Error learning from command: {e}")
            return False
    
    def update_user_preference(self, key, value):
        """Update user preferences"""
        try:
            self.user_preferences[key] = value
            self.save_learning_data()
            return True
        except Exception as e:
            print(f"Error updating user preference: {e}")
            return False
    
    def get_user_preference(self, key, default=None):
        """Get user preference"""
        return self.user_preferences.get(key, default)
    
    def get_command_suggestions(self, partial_command):
        """Get command suggestions based on learning"""
        try:
            suggestions = []
            words = partial_command.lower().split()
            
            # Find matching patterns
            for pattern, count in self.command_patterns.items():
                if pattern.startswith(partial_command.lower()):
                    suggestions.append((pattern, count))
            
            # Sort by frequency
            suggestions.sort(key=lambda x: x[1], reverse=True)
            
            return [s[0] for s in suggestions[:5]]  # Return top 5 suggestions
        except Exception as e:
            print(f"Error getting command suggestions: {e}")
            return []
    
    def get_common_responses(self, command_type):
        """Get common responses for a type of command"""
        try:
            responses = []
            for response, count in self.response_patterns.items():
                if command_type.lower() in response.lower():
                    responses.append((response, count))
            
            # Sort by frequency
            responses.sort(key=lambda x: x[1], reverse=True)
            
            return [r[0] for r in responses[:3]]  # Return top 3 responses
        except Exception as e:
            print(f"Error getting common responses: {e}")
            return []
    
    def get_command_history(self, limit=10):
        """Get recent command history"""
        return self.command_history[-limit:]
    
    def analyze_usage_patterns(self):
        """Analyze usage patterns"""
        try:
            patterns = {
                'most_used_commands': [],
                'success_rate': 0,
                'common_times': [],
                'preferred_features': []
            }
            
            if not self.command_history:
                return patterns
            
            # Calculate success rate
            success_count = sum(1 for cmd in self.command_history if cmd['success'])
            patterns['success_rate'] = (success_count / len(self.command_history)) * 100
            
            # Find most used commands
            command_counts = {}
            for cmd in self.command_history:
                command = cmd['command']
                if command in command_counts:
                    command_counts[command] += 1
                else:
                    command_counts[command] = 1
            
            patterns['most_used_commands'] = sorted(
                command_counts.items(),
                key=lambda x: x[1],
                reverse=True
            )[:5]
            
            # Find common usage times
            time_counts = {}
            for cmd in self.command_history:
                hour = datetime.strptime(cmd['timestamp'], "%Y-%m-%d %H:%M:%S").hour
                if hour in time_counts:
                    time_counts[hour] += 1
                else:
                    time_counts[hour] = 1
            
            patterns['common_times'] = sorted(
                time_counts.items(),
                key=lambda x: x[1],
                reverse=True
            )[:3]
            
            return patterns
        except Exception as e:
            print(f"Error analyzing usage patterns: {e}")
            return {}
    
    def process_learning_command(self, command):
        """Process learning-related commands"""
        command = command.lower()
        
        if "show history" in command:
            history = self.get_command_history()
            if not history:
                return "No command history available"
            
            history_text = "Recent command history:\n"
            for cmd in history:
                history_text += f"- {cmd['command']} ({cmd['timestamp']})\n"
            return history_text
        
        elif "show preferences" in command:
            if not self.user_preferences:
                return "No user preferences set"
            
            prefs_text = "User preferences:\n"
            for key, value in self.user_preferences.items():
                prefs_text += f"- {key}: {value}\n"
            return prefs_text
        
        elif "show patterns" in command:
            patterns = self.analyze_usage_patterns()
            if not patterns:
                return "No usage patterns available"
            
            patterns_text = "Usage patterns:\n"
            patterns_text += f"Success rate: {patterns['success_rate']:.1f}%\n"
            patterns_text += "\nMost used commands:\n"
            for cmd, count in patterns['most_used_commands']:
                patterns_text += f"- {cmd}: {count} times\n"
            patterns_text += "\nCommon usage times:\n"
            for hour, count in patterns['common_times']:
                patterns_text += f"- {hour:02d}:00: {count} times\n"
            return patterns_text
        
        return "I didn't understand that learning command"
    
    def load_learning(self):
        """Load learned commands from file"""
        try:
            if os.path.exists(self.learning_file):
                with open(self.learning_file, 'r') as f:
                    data = json.load(f)
                    self.learned_commands = data.get('commands', {})
                    self.conversation_history = data.get('history', [])
        except Exception as e:
            print(f"Error loading learning data: {e}")
            self.learned_commands = {}
            self.conversation_history = []
    
    def save_learning(self):
        """Save learned commands to file"""
        try:
            data = {
                'commands': self.learned_commands,
                'history': self.conversation_history
            }
            with open(self.learning_file, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error saving learning data: {e}")
    
    def learn_command(self, command, response):
        """Learn a new command-response pair"""
        self.learned_commands[command] = response
        self.save_learning()
    
    def get_learned_response(self, command):
        """Get a learned response for a command"""
        return self.learned_commands.get(command)
    
    def store_conversation(self, user_input, response):
        """Store conversation in history"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.conversation_history.append({
            'timestamp': timestamp,
            'user_input': user_input,
            'response': response
        })
        
        # Keep history within limit
        if len(self.conversation_history) > self.max_history:
            self.conversation_history = self.conversation_history[-self.max_history:]
        
        self.save_learning()
    
    def get_conversation_history(self):
        """Get recent conversation history"""
        return self.conversation_history[-10:]  # Return last 10 conversations
    
    def _load_learned_responses(self):
        if os.path.exists(self.learning_file):
            try:
                with open(self.learning_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}
    
    def _load_conversations(self):
        if os.path.exists(self.conversation_file):
            try:
                with open(self.conversation_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []
    
    def analyze_conversation_patterns(self):
        """Analyze conversation patterns for learning opportunities"""
        # This is a placeholder for more sophisticated pattern analysis
        # In the future, this could use NLP or machine learning
        patterns = {}
        for conv in self.conversations:
            query = conv['query'].lower()
            if query not in patterns:
                patterns[query] = 1
            else:
                patterns[query] += 1
        return patterns
    
    def detect_emotion(self, text):
        """Detect emotion in user's text"""
        text = text.lower()
        emotions = defaultdict(int)
        
        for emotion, keywords in self.emotion_patterns.items():
            for keyword in keywords:
                if keyword in text:
                    emotions[emotion] += 1
        
        return max(emotions.items(), key=lambda x: x[1])[0] if emotions else 'neutral'
    
    def adapt_personality(self, user_emotion):
        """Adapt personality based on user's emotional state"""
        if user_emotion == 'happy':
            self.personality_traits['humor'] = min(1.0, self.personality_traits['humor'] + 0.1)
            self.personality_traits['empathy'] = min(1.0, self.personality_traits['empathy'] + 0.05)
        elif user_emotion == 'sad':
            self.personality_traits['empathy'] = min(1.0, self.personality_traits['empathy'] + 0.1)
            self.personality_traits['formality'] = max(0.0, self.personality_traits['formality'] - 0.05)
        elif user_emotion == 'angry':
            self.personality_traits['formality'] = min(1.0, self.personality_traits['formality'] + 0.1)
            self.personality_traits['proactivity'] = max(0.0, self.personality_traits['proactivity'] - 0.05)
    
    def learn_preference(self, category, preference):
        """Learn user preferences with context"""
        if category not in self.learned_responses:
            self.learned_responses[category] = []
        if preference not in self.learned_responses[category]:
            self.learned_responses[category].append({
                "value": preference,
                "learned_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "context": self.get_current_context()
            })
        self._save_learned_responses()
    
    def get_current_context(self):
        """Get current interaction context"""
        return {
            "time": datetime.now().strftime("%H:%M"),
            "day": datetime.now().strftime("%A"),
            "mood": self.detect_emotion(self.conversations[-1]["query"]) if self.conversations else "neutral"
        }
    
    def analyze_patterns(self):
        """Analyze command patterns with emotional and temporal context"""
        patterns = self.learned_responses
        analysis = {
            "most_used_commands": sorted(patterns.items(), key=lambda x: x[1]["usage_count"], reverse=True),
            "emotional_patterns": defaultdict(int),
            "time_patterns": defaultdict(int),
            "user_mood_trends": self.analyze_mood_trends()
        }
        
        for command, data in patterns.items():
            emotion = self.detect_emotion(command)
            analysis["emotional_patterns"][emotion] += data["usage_count"]
            analysis["time_patterns"][data["learned_at"][:10]] += data["usage_count"]
        
        return analysis
    
    def analyze_mood_trends(self):
        """Analyze user mood trends over time"""
        moods = [self.detect_emotion(conv['query']) for conv in self.conversations]
        return {
            "overall_mood": max(set(moods), key=moods.count) if moods else "neutral",
            "mood_changes": len(set(moods)),
            "recent_mood": moods[-1] if moods else "neutral"
        }
    
    def get_user_preferences(self, category):
        """Get user preferences with context"""
        return self.learned_responses.get(category, [])
    
    def suggest_topics(self):
        """Suggest conversation topics based on user's interests and patterns"""
        topics = defaultdict(int)
        for conv in self.conversations:
            words = conv['query'].split()
            for word in words:
                if len(word) > 3:  # Only consider significant words
                    topics[word] += 1
        
        return sorted(topics.items(), key=lambda x: x[1], reverse=True)[:5] 