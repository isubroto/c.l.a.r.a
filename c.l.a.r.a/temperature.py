import requests
import json

class TemperatureInfo:
    def __init__(self):
        # OpenWeatherMap API key
        self.api_key = "e7768bbd20c31276e34dc57333e0c781"  # Replace with your OpenWeatherMap API key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
        
    def get_temperature(self, city):
        """Get current temperature and forecast for a city"""
        try:
            # Get current weather
            current_params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            }
            current_response = requests.get(self.base_url, params=current_params)
            current_data = current_response.json()
            
            if current_response.status_code != 200:
                return f"Sorry, I couldn't find temperature information for {city}"
            
            # Get forecast
            forecast_params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            }
            forecast_response = requests.get(self.forecast_url, params=forecast_params)
            forecast_data = forecast_response.json()
            
            if forecast_response.status_code != 200:
                return f"Sorry, I couldn't get the forecast for {city}"
            
            # Process current temperature
            current_temp = current_data['main']['temp']
            feels_like = current_data['main']['feels_like']
            humidity = current_data['main']['humidity']
            weather_desc = current_data['weather'][0]['description']
            
            # Process forecast for today
            today = datetime.now().date()
            today_temps = []
            
            for item in forecast_data['list']:
                item_date = datetime.fromtimestamp(item['dt']).date()
                if item_date == today:
                    today_temps.append(item['main']['temp'])
            
            if today_temps:
                min_temp = min(today_temps)
                max_temp = max(today_temps)
                
                # Format the response
                response = (
                    f"Current temperature in {city} is {current_temp}°C, "
                    f"feels like {feels_like}°C. "
                    f"The weather is {weather_desc} with {humidity}% humidity. "
                    f"Today's temperature will range from {min_temp}°C to {max_temp}°C."
                )
                
                return response
            else:
                return f"Current temperature in {city} is {current_temp}°C, feels like {feels_like}°C. The weather is {weather_desc} with {humidity}% humidity."
                
        except Exception as e:
            return f"Sorry, I couldn't get the temperature information for {city}"
    
    def process_temperature_command(self, query):
        """Process temperature-related commands and return response"""
        try:
            # Extract location from query
            location = query.lower()
            for phrase in ["temperature in", "how hot is it in", "how cold is it in", "what's the temperature in"]:
                if phrase in location:
                    location = location.replace(phrase, "").strip()
                    break
            
            if not location:
                return "Please specify a location for temperature information."
            
            # Get temperature data
            params = {
                "q": location,
                "appid": self.api_key,
                "units": "metric"
            }
            
            response = requests.get(self.base_url, params=params)
            data = response.json()
            
            if response.status_code == 200:
                temperature = data["main"]["temp"]
                feels_like = data["main"]["feels_like"]
                temp_min = data["main"]["temp_min"]
                temp_max = data["main"]["temp_max"]
                
                temp_info = (
                    f"The current temperature in {location} is {temperature}°C. "
                    f"It feels like {feels_like}°C. "
                    f"Today's temperature range is from {temp_min}°C to {temp_max}°C."
                )
                return temp_info
            else:
                return f"Sorry, I couldn't get temperature information for {location}."
                
        except Exception as e:
            return f"Error getting temperature information: {str(e)}" 