from datetime import datetime
from responses import ResponseGenerator
from learning import ClaraLearning
from system_commands import SystemCommands
from app_manager import AppManager

class CommandHandler:
    def __init__(self):
        self.response_gen = ResponseGenerator()
        self.clara_learning = ClaraLearning()
        self.system_commands = SystemCommands()
        self.app_manager = AppManager()
        
        # Convert lists to sets for O(1) lookups
        self.wake_phrases = {
            "wake up", "hey clara", "hello clara", "clara wake up",
            "are you there", "are you awake", "wake up clara",
            "start clara", "activate clara", "clara activate",
            "clara start", "clara are you there", "clara are you awake"
        }
        
        self.sleep_phrases = {
            "go to sleep", "sleep now", "goodbye clara", "bye clara",
            "clara sleep", "clara stop", "stop clara", "clara goodbye",
            "clara bye", "deactivate clara", "clara deactivate",
            "clara rest", "rest clara"
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
        
        self.wake_words = ["hey clara", "hello clara", "clara"]
        self.sleep_words = ["goodbye clara", "sleep clara", "bye clara"]
        
    def handle_wake_commands(self, query):
        """Check if the query contains a wake word"""
        return any(word in query.lower() for word in self.wake_words)
    
    def handle_sleep_commands(self, query):
        """Check if the query contains a sleep word"""
        return any(word in query.lower() for word in self.sleep_words)
    
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
        """Process user command and return appropriate response"""
        query = query.lower()
        
        # App management commands - Open variations
        open_phrases = [
            "open ",
            "start ",
            "launch ",
            "run ",
            "begin ",
            "execute ",
            "initiate ",
            "activate ",
            "turn on ",
            "switch on ",
            "power on ",
            "boot up ",
            "fire up ",
            "bring up ",
            "get ",
            "show me ",
            "display ",
            "let's open ",
            "can you open ",
            "please open ",
            "would you open ",
            "could you open ",
            "i want to open ",
            "i need to open ",
            "i'd like to open ",
            "i want to start ",
            "i need to start ",
            "i'd like to start ",
            "i want to launch ",
            "i need to launch ",
            "i'd like to launch "
        ]
        
        # App management commands - Close variations
        close_phrases = [
            "close ",
            "stop ",
            "exit ",
            "quit ",
            "terminate ",
            "end ",
            "shut down ",
            "turn off ",
            "switch off ",
            "power off ",
            "kill ",
            "shut ",
            "let's close ",
            "can you close ",
            "please close ",
            "would you close ",
            "could you close ",
            "i want to close ",
            "i need to close ",
            "i'd like to close ",
            "i want to stop ",
            "i need to stop ",
            "i'd like to stop ",
            "i want to exit ",
            "i need to exit ",
            "i'd like to exit "
        ]
        
        # Check for open commands
        for phrase in open_phrases:
            if query.startswith(phrase):
                app_name = query[len(phrase):].strip()
                return self.app_manager.open_app(app_name), True
                
        # Check for close commands
        for phrase in close_phrases:
            if query.startswith(phrase):
                app_name = query[len(phrase):].strip()
                return self.app_manager.close_app(app_name), True
            
        # Temperature commands
        temp_phrases = [
            "what is the temperature in",
            "temperature in",
            "how hot is it in",
            "how cold is it in",
            "what's the temperature in",
            "tell me the temperature in",
            "current temperature in",
            "today's temperature in",
            "temperature today in",
            "weather temperature in"
        ]
        if any(phrase in query for phrase in temp_phrases):
            return "temperature", True
            
        # Weather commands
        weather_phrases = [
            "what is the weather in",
            "weather in",
            "how's the weather in",
            "tell me the weather in",
            "what's the weather like in"
        ]
        if any(phrase in query for phrase in weather_phrases):
            return "weather", True
            
        # Search commands
        search_phrases = [
            "search for",
            "search wikipedia for",
            "search youtube for",
            "search github for",
            "search stack overflow for",
            "search reddit for",
            "search amazon for",
            "search bing for",
            "search yahoo for",
            "search duckduckgo for",
            "show search history",
            "recent searches"
        ]
        if any(phrase in query for phrase in search_phrases):
            return "search", True
            
        # News commands
        news_phrases = [
            "what is the news",
            "tell me the news",
            "latest news",
            "current news",
            "news update"
        ]
        if any(phrase in query for phrase in news_phrases):
            return "news", True
            
        # Basic commands
        if "hello" in query or "hi" in query:
            return "Hello! How can I help you today?", False
            
        if "how are you" in query:
            return "I'm doing well, thank you for asking! How can I assist you?", False
            
        if "what time is it" in query:
            current_time = datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}", False
            
        if "what is your name" in query or "who are you" in query:
            return "I am Clara, your personal assistant. I'm here to help you with various tasks.", False
            
        # Check cache first
        if query in self.response_cache:
            return self.response_cache[query]
            
        # Check learned responses
        learned_response = self.clara_learning.get_learned_response(query)
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
            self.clara_learning.learn_command(query, response)
            self._update_cache(query, (response, True))
            return response, True
            
        elif self.handle_greeting_commands(query):
            response = self.response_gen.get_greeting_response()
            self.clara_learning.learn_command(query, response)
            self._update_cache(query, (response, True))
            return response, True
            
        elif self.handle_name_commands(query):
            response = self.response_gen.get_name_response()
            self.clara_learning.learn_command(query, response)
            self._update_cache(query, (response, True))
            return response, True
            
        elif self.handle_time_commands(query):
            # Get current time in 12-hour format
            current_time = datetime.now()
            strTime = current_time.strftime("%I:%M %p")  # 12-hour format with AM/PM
            response = self.response_gen.get_time_response(strTime)
            self.clara_learning.learn_command(query, response)
            self._update_cache(query, (response, True))
            return response, True
            
        elif self.handle_feeling_good_commands(query):
            response = self.response_gen.get_feeling_good_response()
            self.clara_learning.learn_command(query, response)
            self._update_cache(query, (response, True))
            return response, True
            
        elif self.handle_feeling_bad_commands(query):
            response = self.response_gen.get_feeling_bad_response()
            self.clara_learning.learn_command(query, response)
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
            self.clara_learning.store_conversation(query, response)
            self._update_cache(query, (response, False))
            return response, False
    
    def _update_cache(self, query, response):
        """Update response cache with LRU-like behavior"""
        if len(self.response_cache) >= self.cache_size:
            # Remove oldest entry
            self.response_cache.pop(next(iter(self.response_cache)))
        self.response_cache[query] = response 