import requests
from sayAndListen import speak
import random
from datetime import datetime

def get_news():
    # You need to replaYOUR_NEWS_API_KEYce this with your actual API key from NewsAPI
    API_KEY = "5e173bda505b40d4b6aa9e8b2d726130"
    
    # Different ways to introduce news
    introductions = [
        "Here's what's happening in the world right now",
        "Let me catch you up on today's headlines",
        "I've got some interesting news for you",
        "Here are the top stories making headlines",
        "Let me share the latest news with you",
        "I've been keeping track of the news, and here's what's important",
        "Here are the stories everyone's talking about",
        "Let me update you on the current events",
        "I've got the latest news for you",
        "Here are today's most significant stories"
    ]
    
    # Different ways to transition between news items
    transitions = [
        "Moving on to",
        "Next up",
        "Also in the news",
        "Another important story",
        "Here's another headline",
        "In other news",
        "Additionally",
        "Furthermore",
        "Meanwhile",
        "On another note"
    ]
    
    # Different ways to handle errors
    error_messages = [
        "I'm having trouble accessing the news right now. Let me try again in a moment.",
        "It seems I can't reach the news sources at the moment. Would you like to try something else?",
        "I'm experiencing some technical difficulties with the news feed. Shall we try again later?",
        "The news service seems to be unavailable right now. Is there something else I can help you with?",
        "I'm unable to fetch the latest news at this moment. Would you like to try a different request?"
    ]
    
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
        response = requests.get(url)
        news = response.json()
        
        if response.status_code == 200 and news["articles"]:
            # Start with a random introduction
            speak(random.choice(introductions))
            
            # Get current time for time-based responses
            current_hour = datetime.now().hour
            
            # Add time-based context
            if 5 <= current_hour < 12:
                speak("Here are the morning headlines")
            elif 12 <= current_hour < 17:
                speak("Here are the afternoon updates")
            else:
                speak("Here are the evening headlines")
            
            # Present the news with varied transitions
            for i, article in enumerate(news["articles"][:5], 1):
                if i == 1:
                    speak(f"First, {article['title']}")
                elif i == len(news["articles"][:5]):
                    speak(f"Finally, {article['title']}")
                else:
                    speak(f"{random.choice(transitions)}, {article['title']}")
            
            # Add a closing remark
            closing_remarks = [
                "That's the latest from the news. Is there anything specific you'd like to know more about?",
                "Those were the top stories. Would you like more details on any of these?",
                "That wraps up the current news. Is there anything else you'd like to know?",
                "Those were the headlines. Would you like me to elaborate on any of these stories?",
                "That's what's happening in the world. Is there a particular story you'd like to explore further?"
            ]
            speak(random.choice(closing_remarks))
            
        else:
            speak(random.choice(error_messages))
            
    except Exception as e:
        speak(random.choice(error_messages)) 