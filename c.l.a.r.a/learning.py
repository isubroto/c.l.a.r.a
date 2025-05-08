import json
import os
from datetime import datetime
import random
from collections import defaultdict

class ClaraLearning:
    def __init__(self):
        self.learned_commands = {}
        self.conversation_history = []
        self.max_history = 100
        self.learning_file = 'clara_learning.json'
        self.load_learning()
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