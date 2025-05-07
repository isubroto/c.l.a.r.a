from datetime import datetime
from responses import ResponseGenerator
from learning import JarvisLearning
from system_commands import SystemCommands

class CommandHandler:
    def __init__(self):
        self.response_gen = ResponseGenerator()
        self.jarvis_learning = JarvisLearning()
        self.system_commands = SystemCommands()
        
        # Convert lists to sets for O(1) lookups
        self.wake_phrases = {
            "wake up", "hey jarvis", "hello jarvis", "jarvis wake up",
            "are you there", "are you awake", "wake up jarvis",
            "start jarvis", "activate jarvis", "jarvis activate",
            "jarvis start", "jarvis are you there", "jarvis are you awake"
        }
        
        self.sleep_phrases = {
            "go to sleep", "sleep now", "goodbye jarvis", "bye jarvis",
            "jarvis sleep", "jarvis stop", "stop jarvis", "jarvis goodbye",
            "jarvis bye", "deactivate jarvis", "jarvis deactivate",
            "jarvis rest", "rest jarvis"
        }
        
        self.greeting_phrases = {
            "hello", "hi", "hey", "greetings", "good morning",
            "good afternoon", "good evening", "hello there",
            "hi there", "hey there"
        }
        
        self.name_phrases = {
            "what is your name", "who are you", "what should i call you",
            "what's your name", "tell me your name", "what do people call you",
            "what can i call you", "your name", "name please",
            "introduce yourself"
        }
        
        self.time_phrases = {
            "what is the time", "what time is it", "tell me the time",
            "current time", "time now", "what's the time",
            "do you know the time", "can you tell me the time",
            "what time do you have", "time please", "show me the time",
            "give me the time", "time check", "check the time",
            "time update", "current time now", "what's the current time",
            "tell me current time", "time right now",
            "what's the time right now"
        }
        
        self.feeling_good_phrases = {
            "i am good", "i am fine", "doing good", "doing fine",
            "feeling good", "feeling fine", "all good", "all fine",
            "pretty good", "pretty fine", "quite good", "quite fine",
            "very good", "very fine"
        }
        
        self.feeling_bad_phrases = {
            "i am bad", "i am not fine", "feeling bad", "not good",
            "not fine", "feeling down", "feeling sad", "feeling terrible",
            "feeling awful", "feeling horrible", "feeling sick",
            "feeling unwell", "feeling low", "feeling blue"
        }
        
        self.news_phrases = {
            "what is the news", "tell me the news", "latest news",
            "current news", "news update", "what's happening",
            "what's going on", "what's new", "any news", "news please",
            "show me the news", "give me the news", "news headlines",
            "today's news", "breaking news"
        }
        
        # Cache for learned responses
        self.response_cache = {}
        self.cache_size = 100
        
    def handle_wake_commands(self, query):
        return any(phrase in query for phrase in self.wake_phrases)
    
    def handle_sleep_commands(self, query):
        return any(phrase in query for phrase in self.sleep_phrases)
    
    def handle_greeting_commands(self, query):
        return any(phrase in query for phrase in self.greeting_phrases)
    
    def handle_name_commands(self, query):
        return any(phrase in query for phrase in self.name_phrases)
    
    def handle_time_commands(self, query):
        return any(phrase in query for phrase in self.time_phrases)
    
    def handle_feeling_good_commands(self, query):
        return any(phrase in query for phrase in self.feeling_good_phrases)
    
    def handle_feeling_bad_commands(self, query):
        return any(phrase in query for phrase in self.feeling_bad_phrases)
    
    def handle_news_commands(self, query):
        return any(phrase in query for phrase in self.news_phrases)
    
    def process_command(self, query):
        # Check cache first
        if query in self.response_cache:
            return self.response_cache[query]
            
        # Check learned responses
        learned_response = self.jarvis_learning.get_learned_response(query)
        if learned_response:
            self._update_cache(query, (learned_response, True))
            return learned_response, True
        
        # Check system commands
        system_response = self.system_commands.process_command(query)
        if system_response:
            self._update_cache(query, (system_response, True))
            return system_response, True
        
        # Process command
        if self.handle_sleep_commands(query):
            response = self.response_gen.get_sleep_response()
            self.jarvis_learning.learn_command(query, response)
            self._update_cache(query, (response, True))
            return response, True
            
        elif self.handle_greeting_commands(query):
            response = self.response_gen.get_greeting_response()
            self.jarvis_learning.learn_command(query, response)
            self._update_cache(query, (response, True))
            return response, True
            
        elif self.handle_name_commands(query):
            response = self.response_gen.get_name_response()
            self.jarvis_learning.learn_command(query, response)
            self._update_cache(query, (response, True))
            return response, True
            
        elif self.handle_time_commands(query):
            # Get current time in 12-hour format
            current_time = datetime.now()
            strTime = current_time.strftime("%I:%M %p")  # 12-hour format with AM/PM
            response = self.response_gen.get_time_response(strTime)
            self.jarvis_learning.learn_command(query, response)
            self._update_cache(query, (response, True))
            return response, True
            
        elif self.handle_feeling_good_commands(query):
            response = self.response_gen.get_feeling_good_response()
            self.jarvis_learning.learn_command(query, response)
            self._update_cache(query, (response, True))
            return response, True
            
        elif self.handle_feeling_bad_commands(query):
            response = self.response_gen.get_feeling_bad_response()
            self.jarvis_learning.learn_command(query, response)
            self._update_cache(query, (response, True))
            return response, True
            
        elif "weather" in query:
            self._update_cache(query, ("weather", True))
            return "weather", True
            
        elif self.handle_news_commands(query):
            self._update_cache(query, ("news", True))
            return "news", True
            
        else:
            response = self.response_gen.get_unknown_command_response()
            self.jarvis_learning.store_conversation(query, response)
            self._update_cache(query, (response, False))
            return response, False
    
    def _update_cache(self, query, response):
        """Update response cache with LRU-like behavior"""
        if len(self.response_cache) >= self.cache_size:
            # Remove oldest entry
            self.response_cache.pop(next(iter(self.response_cache)))
        self.response_cache[query] = response 