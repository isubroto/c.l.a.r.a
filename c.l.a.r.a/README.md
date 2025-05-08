# C.L.A.R.A - Command Line Assistant with Real-time Analysis

C.L.A.R.A is an intelligent voice-controlled personal assistant that can help you with various tasks through natural language commands.

## Features

- **Voice Control**: Wake up Clara by saying "Hey Clara" and give voice commands
- **Weather Information**: Get current weather conditions for any location
- **Web Search**: Search the web for information
- **Temperature Conversion**: Convert temperatures between different units
- **News Updates**: Get the latest news (coming soon)
- **Learning Capabilities**: Clara learns from interactions to improve responses
- **Customizable**: Save and load user preferences

## Requirements

- Python 3.13 or higher
- Windows 10/11
- Working microphone
- Internet connection

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/c.l.a.r.a.git
cd c.l.a.r.a
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Set up your OpenWeatherMap API key:
   - Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
   - Replace the API key in `weather.py` with your own

## Usage

1. Run Clara:

```bash
python clara_main.py
```

2. Wait for the "Clara is ready!" message
3. Say "Hey Clara" to activate
4. Give your command

### Example Commands

- "What's the weather in London?"
- "How's the weather outside?"
- "Convert 32 degrees Fahrenheit to Celsius"
- "Search for Python programming"
- "Tell me the latest news"

## Project Structure

- `clara_main.py`: Main program file
- `command_handler.py`: Processes and routes commands
- `responses.py`: Generates natural language responses
- `weather.py`: Handles weather information
- `temperature.py`: Manages temperature conversions
- `web_search.py`: Handles web searches
- `sayAndListen.py`: Manages speech input/output
- `hotword_detector.py`: Detects wake word
- `learning.py`: Implements learning capabilities

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenWeatherMap API for weather data
- SpeechRecognition library for voice recognition
- pyttsx3 for text-to-speech capabilities
