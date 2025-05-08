import random
from datetime import datetime

class ResponseGenerator:
    def __init__(self):
        self.greetings = [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Greetings! I'm here to assist you.",
            "Hello! I'm ready to help you with anything you need.",
            "Hi! How may I be of service today?"
        ]
        
        self.sleep_responses = [
            "Goodbye! Have a wonderful day!",
            "Going to sleep now. Take care!",
            "Resting for now. Call me when you need me!",
            "Sleep mode activated. Sweet dreams!",
            "Taking a break. I'll be here when you need me!"
        ]
        
        self.name_responses = [
            "I'm Clara, your personal AI assistant. I'm here to help you with various tasks!",
            "My name is Clara. I'm your friendly AI companion, ready to assist you!",
            "I'm Clara! I love helping people and making their lives easier.",
            "You can call me Clara. I'm your personal assistant, always here to help!",
            "I'm Clara, and I'm excited to be your AI assistant!"
        ]
        
        self.time_responses = [
            "The current time is {time}.",
            "It's {time} right now.",
            "The time is {time}.",
            "According to my clock, it's {time}.",
            "It's currently {time}."
        ]
        
        self.feeling_good_responses = [
            "That's wonderful to hear! I'm glad you're doing well!",
            "That's fantastic! I'm happy to hear you're feeling good!",
            "Great to hear that! I hope your day continues to be amazing!",
            "That's lovely! I'm glad you're in good spirits!",
            "Wonderful! I'm happy to hear you're doing well!"
        ]
        
        self.feeling_bad_responses = [
            "I'm sorry to hear that. Is there anything I can do to help?",
            "That's not good. Would you like to talk about it?",
            "I'm here for you. Would you like to share what's bothering you?",
            "I'm sorry you're feeling down. I'm here to help if you need anything.",
            "That's unfortunate. Remember, I'm here to support you in any way I can."
        ]
        
        self.unknown_command_responses = [
            "I'm not sure I understand. Could you please rephrase that?",
            "I didn't quite catch that. Could you try saying it differently?",
            "I'm still learning. Could you explain that in another way?",
            "I'm not sure how to help with that yet. Could you try asking something else?",
            "I'm still developing my skills. Could you try a different question?"
        ]

    def get_greeting_response(self):
        return random.choice(self.greetings)
    
    def get_sleep_response(self):
        return random.choice(self.sleep_responses)
    
    def get_name_response(self):
        return random.choice(self.name_responses)
    
    def get_time_response(self, time):
        return random.choice(self.time_responses).format(time=time)
    
    def get_feeling_good_response(self):
        return random.choice(self.feeling_good_responses)
    
    def get_feeling_bad_response(self):
        return random.choice(self.feeling_bad_responses)
    
    def get_unknown_command_response(self):
        return random.choice(self.unknown_command_responses) 