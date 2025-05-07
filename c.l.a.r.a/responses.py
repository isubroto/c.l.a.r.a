import random
from datetime import datetime

class ResponseGenerator:
    def __init__(self):
        self.wake_responses = [
            "Hello! I'm here and ready to help",
            "Yes, I'm awake and listening",
            "At your service! How can I help you today?",
            "I'm here and ready to assist you",
            "Hello! What can I do for you?",
            "I'm awake and ready to help",
            "Yes, I'm here. How can I assist you?",
            "Hello! I'm ready to help you with anything",
            "I'm here and listening. What do you need?",
            "Yes, I'm awake. How can I be of service?"
        ]
        
        self.sleep_responses = [
            "Going to sleep mode. Goodbye!",
            "Powering down. Have a great day!",
            "Entering sleep mode. See you later!",
            "Shutting down. Take care!",
            "Going to rest now. Goodbye!",
            "Deactivating. Until next time!",
            "Entering standby mode. Farewell!",
            "Powering off. Have a wonderful day!",
            "Going offline. See you soon!",
            "Taking a break. Goodbye!"
        ]
        
        self.greeting_responses = [
            "Hello! How can I assist you today?",
            "Hi there! What can I do for you?",
            "Greetings! How may I help you?",
            "Hello! I'm here to help. What do you need?",
            "Hi! I'm ready to assist. What's on your mind?",
            "Greetings! How can I be of service?",
            "Hello! What can I help you with today?",
            "Hi there! I'm at your service. What do you need?",
            "Greetings! How may I assist you today?",
            "Hello! I'm here and ready to help. What can I do for you?"
        ]
        
        self.name_responses = [
            "I am Jarvis, your personal AI assistant.",
            "You can call me Jarvis. I'm here to help!",
            "I'm Jarvis, your friendly AI companion.",
            "My name is Jarvis. How can I assist you?",
            "I go by Jarvis. I'm your personal assistant.",
            "You can call me Jarvis. I'm at your service!",
            "I'm known as Jarvis. How may I help you?",
            "My name is Jarvis. I'm here to assist you.",
            "I'm called Jarvis. What can I do for you?",
            "You can refer to me as Jarvis. How can I help?"
        ]
        
        self.feeling_good_responses = [
            "That's wonderful to hear! I'm glad you're doing well.",
            "Great to know you're feeling good!",
            "That's fantastic! I'm happy for you.",
            "Wonderful! It's nice to hear you're doing well.",
            "That's excellent! I'm glad you're feeling good.",
            "Great to hear you're doing fine!",
            "That's wonderful! I'm happy you're feeling good.",
            "Excellent! It's nice to know you're doing well.",
            "That's fantastic! I'm glad you're feeling fine.",
            "Wonderful! I'm happy to hear you're doing good."
        ]
        
        self.feeling_bad_responses = [
            "I'm sorry to hear that. Is there anything I can do to help?",
            "That's unfortunate. Would you like to talk about it?",
            "I'm sorry you're feeling down. How can I assist you?",
            "That's not good to hear. Is there something I can do?",
            "I'm sorry you're not feeling well. Would you like to discuss it?",
            "That's unfortunate. I'm here if you need to talk.",
            "I'm sorry to hear you're feeling bad. How can I help?",
            "That's not good. Would you like to share what's bothering you?",
            "I'm sorry you're feeling down. Is there anything I can do?",
            "That's unfortunate. I'm here to listen if you need to talk."
        ]
        
        self.time_responses = [
            "It's {time}.",
            "The time is {time}.",
            "Right now it's {time}.",
            "The current time is {time}.",
            "It's {time} at the moment.",
            "The clock shows {time}.",
            "It's {time} on the dot.",
            "The time right now is {time}.",
            "Currently, it's {time}.",
            "The present time is {time}."
        ]
        
        self.unknown_command_responses = [
            "I'm not sure I understand. Could you please rephrase that?",
            "I didn't quite catch that. Could you try saying it differently?",
            "I'm not sure what you mean. Could you explain differently?",
            "I didn't understand that. Could you rephrase your request?",
            "I'm not sure I follow. Could you try saying it another way?",
            "I didn't quite get that. Could you please rephrase?",
            "I'm not sure what you're asking. Could you explain differently?",
            "I didn't understand that. Could you try saying it another way?",
            "I'm not sure I follow. Could you please rephrase?",
            "I didn't quite catch that. Could you explain differently?"
        ]

    def get_wake_response(self):
        return random.choice(self.wake_responses)
    
    def get_sleep_response(self):
        return random.choice(self.sleep_responses)
    
    def get_greeting_response(self):
        return random.choice(self.greeting_responses)
    
    def get_name_response(self):
        return random.choice(self.name_responses)
    
    def get_feeling_good_response(self):
        return random.choice(self.feeling_good_responses)
    
    def get_feeling_bad_response(self):
        return random.choice(self.feeling_bad_responses)
    
    def get_time_response(self, time):
        return random.choice(self.time_responses).format(time=time)
    
    def get_unknown_command_response(self):
        return random.choice(self.unknown_command_responses) 