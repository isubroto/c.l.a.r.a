import requests
import json
import geocoder

def get_weather(query):
    """Get weather information for a location"""
    try:
        # Extract location from query
        query = query.lower()
        location = None
        
        # Common weather-related phrases to remove
        weather_phrases = [
            "what is the weather",
            "how's the weather",
            "tell me the weather",
            "what's the weather like",
            "weather outside",
            "weather today",
            "current weather",
            "weather right now",
            "weather forecast",
            "weather report",
            "weather in",
            "how is the weather"
        ]
        
        # Remove weather-related phrases
        for phrase in weather_phrases:
            query = query.replace(phrase, "").strip()
        
        # If there's any remaining text, use it as location
        if query:
            location = query.strip()
        
        # If no location specified, get current city
        if not location:
            try:
                # Get current location using IP geolocation
                g = geocoder.ip('me')
                if g.ok:
                    location = g.city
                    print(f"Using current city: {location}")
                else:
                    return "I couldn't detect your current location. Please specify a city name."
            except Exception as e:
                return "I couldn't detect your current location. Please specify a city name."
            
        # Get weather data from OpenWeatherMap API
        api_key = "8e6a087ce7f01ae91d068390473d3dca"  # Replace with your OpenWeatherMap API key
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        
        params = {
            "q": location,
            "appid": api_key,
            "units": "metric"
        }
        
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            weather = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            
            weather_info = (
                f"The weather in {location} is {weather}. "
                f"Temperature is {temperature}°C, "
                f"humidity is {humidity}%, "
                f"and wind speed is {wind_speed} meters per second."
            )
            return weather_info
        else:
            return f"Sorry, I couldn't get weather information for {location}."
            
    except Exception as e:
        return f"Error getting weather information: {str(e)}"
