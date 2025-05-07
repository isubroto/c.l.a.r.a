from sayAndListen import takeCommand
from sayAndListen import speak
from learning import JarvisLearning

# Initialize learning system
jarvis_learning = JarvisLearning()

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if any(phrase in query for phrase in [
            "wake up",
            "hey jarvis",
            "hello jarvis",
            "jarvis wake up",
            "are you there",
            "are you awake",
            "wake up jarvis",
            "start jarvis",
            "activate jarvis",
            "jarvis activate",
            "jarvis start",
            "jarvis are you there",
            "jarvis are you awake"
        ]):
            from greedMe import wishMe
            wishMe()
            
            while True:
                query = takeCommand().lower()
                
                # First check if we have a learned response
                learned_response = jarvis_learning.get_learned_response(query)
                if learned_response:
                    speak(learned_response)
                    jarvis_learning.store_conversation(query, learned_response)
                    continue
                
                if any(phrase in query for phrase in [
                    "go to sleep",
                    "sleep now",
                    "goodbye jarvis",
                    "bye jarvis",
                    "jarvis sleep",
                    "jarvis stop",
                    "stop jarvis",
                    "jarvis goodbye",
                    "jarvis bye",
                    "deactivate jarvis",
                    "jarvis deactivate",
                    "jarvis rest",
                    "rest jarvis"
                ]):
                    response = "ok sir, you can call me anytime"
                    speak(response)
                    jarvis_learning.learn_command(query, response)
                    jarvis_learning.store_conversation(query, response)
                elif any(phrase in query for phrase in [
                    "hello",
                    "hi",
                    "hey",
                    "greetings",
                    "good morning",
                    "good afternoon",
                    "good evening",
                    "hello there",
                    "hi there",
                    "hey there"
                ]):
                    response = "Hello sir, how can I help you today?"
                    speak(response)
                    jarvis_learning.learn_command(query, response)
                    jarvis_learning.store_conversation(query, response)
                elif any(phrase in query for phrase in [
                    "what is your name",
                    "who are you",
                    "what should i call you",
                    "what's your name",
                    "tell me your name",
                    "what do people call you",
                    "what can i call you",
                    "your name",
                    "name please",
                    "introduce yourself"
                ]):
                    response = "I am Jarvis, your personal assistant"
                    speak(response)
                    jarvis_learning.learn_command(query, response)
                    jarvis_learning.store_conversation(query, response)
                elif any(phrase in query for phrase in [
                    "what is the time",
                    "what time is it",
                    "tell me the time",
                    "current time",
                    "time now",
                    "what's the time",
                    "do you know the time",
                    "can you tell me the time",
                    "what time do you have",
                    "time please",
                    "show me the time",
                    "give me the time",
                    "time check",
                    "check the time",
                    "time update",
                    "current time now",
                    "what's the current time",
                    "tell me current time",
                    "time right now",
                    "what's the time right now"
                ]):
                    from datetime import datetime
                    strTime = datetime.now().strftime("%H:%M:%S")
                    response = f"The current time is {strTime}"
                    speak(response)
                    jarvis_learning.learn_command(query, response)
                    jarvis_learning.store_conversation(query, response)
                elif any(phrase in query for phrase in [
                    "i am good",
                    "i am fine",
                    "doing good",
                    "doing fine",
                    "feeling good",
                    "feeling fine",
                    "all good",
                    "all fine",
                    "pretty good",
                    "pretty fine",
                    "quite good",
                    "quite fine",
                    "very good",
                    "very fine"
                ]):
                    response = "That's great to hear"
                    speak(response)
                    jarvis_learning.learn_command(query, response)
                    jarvis_learning.store_conversation(query, response)
                elif any(phrase in query for phrase in [
                    "i am bad",
                    "i am not fine",
                    "feeling bad",
                    "not good",
                    "not fine",
                    "feeling down",
                    "feeling sad",
                    "feeling terrible",
                    "feeling awful",
                    "feeling horrible",
                    "feeling sick",
                    "feeling unwell",
                    "feeling low",
                    "feeling blue"
                ]):
                    response = "I am sorry to hear that"
                    speak(response)
                    jarvis_learning.learn_command(query, response)
                    jarvis_learning.store_conversation(query, response)
                elif "weather" in query:
                    from weather import get_weather
                    get_weather(query)
                    jarvis_learning.store_conversation(query, "Weather information provided")
                elif any(phrase in query for phrase in [
                    "what is the news",
                    "tell me the news",
                    "latest news",
                    "current news",
                    "news update",
                    "what's happening",
                    "what's going on",
                    "what's new",
                    "any news",
                    "news please",
                    "show me the news",
                    "give me the news",
                    "news headlines",
                    "today's news",
                    "breaking news"
                ]):
                    from news import get_news
                    get_news()
                    jarvis_learning.store_conversation(query, "News information provided")
                else:
                    # Learn from unknown commands
                    jarvis_learning.store_conversation(query, "Command not recognized")
                    break

