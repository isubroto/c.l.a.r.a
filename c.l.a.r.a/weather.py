import requests
from sayAndListen import speak

def get_weather(query):
    # List of possible weather command phrases
    weather_phrases = [
        "what is the weather in",
        "weather in",
        "how's the weather in",
        "tell me the weather in",
        "what's the weather like in",
        "give me the weather for",
        "check weather in",
        "what's the temperature in",
        "how hot is it in",
        "how cold is it in",
        "is it raining in",
        "is it sunny in",
        "what's the forecast for",
        "weather forecast for",
        "temperature in",
        "weather conditions in",
        "current weather in",
        "today's weather in",
        "weather report for",
        "weather update for",
        "weather status in",
        "weather details for",
        "weather information for",
        "weather data for",
        "weather situation in"
    ]
    
    # Extract city name by removing any of the weather phrases
    city = query
    for phrase in weather_phrases:
        if phrase in query.lower():
            city = query.lower().replace(phrase, "").strip()
            break
    
    # You need to replace this with your actual API key from OpenWeatherMap
    API_KEY = "e7768bbd20c31276e34dc57333e0c781"
    
    try:
        # Make API request
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            temp = data['main']['temp']
            weather_desc = data['weather'][0]['description']
            humidity = data['main']['humidity']
            
            weather_info = f"The temperature in {city} is {temp}°C. Weather is {weather_desc}. Humidity is {humidity}%"
            speak(weather_info)
        else:
            speak(f"Sorry, I couldn't find weather information for {city}")
            
    except Exception as e:
        speak("Sorry, I couldn't fetch the weather information at the moment")
