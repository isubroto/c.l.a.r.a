import json
import os
from datetime import datetime
import random
from collections import defaultdict

class JarvisLearning:
    def __init__(self):
        self.learning_file = "jarvis_learning.json"
        self.learned_data = self.load_learning_data()
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
        if os.path.exists(self.learning_file):
            with open(self.learning_file, 'r') as f:
                return json.load(f)
        return {
            "command_patterns": {},
            "user_preferences": {},
            "conversation_history": [],
            "learned_responses": {},
            "user_personality": {},
            "interaction_style": {},
            "emotional_context": [],
            "daily_patterns": defaultdict(list),
            "user_mood_history": [],
            "personalized_greetings": [],
            "conversation_topics": defaultdict(int)
        }
    
    def save_learning_data(self):
        with open(self.learning_file, 'w') as f:
            json.dump(self.learned_data, f, indent=4)
    
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
    
    def learn_command(self, command, response):
        """Learn new command patterns and their responses with emotional context"""
        emotion = self.detect_emotion(command)
        current_time = datetime.now()
        time_of_day = current_time.strftime("%H:%M")
        
        if command not in self.learned_data["command_patterns"]:
            self.learned_data["command_patterns"][command] = {
                "response": response,
                "count": 1,
                "last_used": current_time.strftime("%Y-%m-%d %H:%M:%S"),
                "emotions": {emotion: 1},
                "time_patterns": {time_of_day: 1}
            }
        else:
            self.learned_data["command_patterns"][command]["count"] += 1
            self.learned_data["command_patterns"][command]["last_used"] = current_time.strftime("%Y-%m-%d %H:%M:%S")
            self.learned_data["command_patterns"][command]["emotions"][emotion] = \
                self.learned_data["command_patterns"][command]["emotions"].get(emotion, 0) + 1
            self.learned_data["command_patterns"][command]["time_patterns"][time_of_day] = \
                self.learned_data["command_patterns"][command]["time_patterns"].get(time_of_day, 0) + 1
        
        self.adapt_personality(emotion)
        self.save_learning_data()
    
    def generate_personalized_response(self, command, base_response):
        """Generate a personalized response based on learned patterns and personality"""
        emotion = self.detect_emotion(command)
        current_time = datetime.now()
        time_of_day = current_time.strftime("%H:%M")
        
        # Add time-based greeting
        if 5 <= current_time.hour < 12:
            greeting = "Good morning"
        elif 12 <= current_time.hour < 17:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
        
        # Add personality-based modifiers
        if self.personality_traits['humor'] > 0.7 and random.random() < 0.3:
            base_response += " 😊"
        
        if self.personality_traits['empathy'] > 0.7 and emotion in ['sad', 'angry']:
            base_response = f"I understand. {base_response}"
        
        if self.personality_traits['formality'] > 0.7:
            base_response = f"{greeting}, sir. {base_response}"
        else:
            base_response = f"{greeting}! {base_response}"
        
        return base_response
    
    def learn_preference(self, category, preference):
        """Learn user preferences with context"""
        if category not in self.learned_data["user_preferences"]:
            self.learned_data["user_preferences"][category] = []
        if preference not in self.learned_data["user_preferences"][category]:
            self.learned_data["user_preferences"][category].append({
                "value": preference,
                "learned_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "context": self.get_current_context()
            })
        self.save_learning_data()
    
    def get_current_context(self):
        """Get current interaction context"""
        return {
            "time": datetime.now().strftime("%H:%M"),
            "day": datetime.now().strftime("%A"),
            "mood": self.detect_emotion(self.learned_data["conversation_history"][-1]["user_input"]) if self.learned_data["conversation_history"] else "neutral"
        }
    
    def store_conversation(self, user_input, response):
        """Store conversation history with emotional and contextual data"""
        emotion = self.detect_emotion(user_input)
        context = self.get_current_context()
        
        self.learned_data["conversation_history"].append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user_input": user_input,
            "response": response,
            "emotion": emotion,
            "context": context
        })
        
        # Update daily patterns
        self.learned_data["daily_patterns"][context["day"]].append({
            "time": context["time"],
            "emotion": emotion,
            "command": user_input
        })
        
        # Keep only last 100 conversations
        if len(self.learned_data["conversation_history"]) > 100:
            self.learned_data["conversation_history"] = self.learned_data["conversation_history"][-100:]
        
        self.save_learning_data()
    
    def get_learned_response(self, command):
        """Get learned response with personalization"""
        base_response = self.learned_data["command_patterns"].get(command, {}).get("response")
        if base_response:
            return self.generate_personalized_response(command, base_response)
        return None
    
    def analyze_patterns(self):
        """Analyze command patterns with emotional and temporal context"""
        patterns = self.learned_data["command_patterns"]
        analysis = {
            "most_used_commands": sorted(patterns.items(), key=lambda x: x[1]["count"], reverse=True),
            "emotional_patterns": defaultdict(int),
            "time_patterns": defaultdict(int),
            "user_mood_trends": self.analyze_mood_trends()
        }
        
        for command_data in patterns.values():
            for emotion, count in command_data["emotions"].items():
                analysis["emotional_patterns"][emotion] += count
            for time, count in command_data["time_patterns"].items():
                analysis["time_patterns"][time] += count
        
        return analysis
    
    def analyze_mood_trends(self):
        """Analyze user mood trends over time"""
        moods = [entry["emotion"] for entry in self.learned_data["conversation_history"]]
        return {
            "overall_mood": max(set(moods), key=moods.count) if moods else "neutral",
            "mood_changes": len(set(moods)),
            "recent_mood": moods[-1] if moods else "neutral"
        }
    
    def get_user_preferences(self, category):
        """Get user preferences with context"""
        return self.learned_data["user_preferences"].get(category, [])
    
    def get_recent_conversations(self, limit=10):
        """Get recent conversations with emotional context"""
        return self.learned_data["conversation_history"][-limit:]
    
    def suggest_topics(self):
        """Suggest conversation topics based on user's interests and patterns"""
        topics = defaultdict(int)
        for conv in self.learned_data["conversation_history"]:
            words = conv["user_input"].split()
            for word in words:
                if len(word) > 3:  # Only consider significant words
                    topics[word] += 1
        
        return sorted(topics.items(), key=lambda x: x[1], reverse=True)[:5] 