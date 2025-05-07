# C.L.A.R.A - Conversational Learning AI Response Assistant

C.L.A.R.A is an advanced voice-controlled AI assistant built with Python that combines natural language processing, system control capabilities, and self-learning features. The assistant can understand and respond to voice commands, control system functions, provide weather updates, and learn from user interactions.

## Features

- 🎤 Voice Recognition and Response
- 🌤️ Weather Information
- 💻 System Control Commands
- 📰 News Updates
- 🧠 Self-Learning Capabilities
- 🎯 Context-Aware Responses
- 🔄 Response Caching
- ⚡ Fast Command Processing
- 🐳 Docker Support
- 🔄 CI/CD Pipeline
- 🪟 Windows Integration
- 🐧 Linux Support

## Prerequisites

- Python 3.13 or higher
- Windows 10/11 (for full system control features)
- Linux (for Docker deployment)
- Microphone
- Speakers

## Installation

### Local Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/c.l.a.r.a.git
cd c.l.a.r.a
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Run the assistant:

```bash
python c.l.a.r.a/Jarvis_main.py
```

### Docker Installation

1. Pull the Docker image:

```bash
docker pull ghcr.io/yourusername/clara:latest
```

2. Run the container:

```bash
docker run -it --device /dev/snd ghcr.io/yourusername/clara:latest
```

## Development

### Project Structure

```
c.l.a.r.a/
├── c.l.a.r.a/
│   ├── Jarvis_main.py          # Main application file
│   ├── command_handler.py      # Command processing logic
│   ├── responses.py           # Response generation
│   ├── learning.py           # Self-learning module
│   ├── system_commands.py    # System control commands
│   └── weather.py           # Weather information
├── tests/                    # Test directory
├── .github/
│   └── workflows/           # GitHub Actions workflows
├── Dockerfile               # Docker configuration
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

### Running Tests

```bash
python -m unittest discover c.l.a.r.a/tests
```

### CI/CD Pipeline

The project uses GitHub Actions for continuous integration and deployment:

- Windows Build and Test: Runs tests on Windows
- Docker Build: Builds and pushes Docker images
- Release: Creates GitHub releases with changelog

## Available Commands

### Basic Commands

- **Greeting**: "Hello", "Hi", "Hey"
- **Name**: "What is your name", "Who are you"
- **Time**: "What time is it", "Tell me the time"
- **Feelings**: "I am good", "I am not fine"
- **Sleep**: "Go to sleep", "Sleep now", "Goodbye Jarvis"

### Weather Commands

- "What is the weather in [city]"
- "Weather in [city]"
- "How's the weather in [city]"
- "Tell me the weather in [city]"
- "What's the temperature in [city]"

### System Commands (Windows Only)

#### Power Management

- "Shutdown computer"
- "Restart computer"
- "Sleep mode"
- "Put computer to sleep"

#### Volume Control

- "Volume up"
- "Volume down"
- "Mute"
- "Increase volume"
- "Decrease volume"

#### Display Control

- "Brightness up"
- "Brightness down"
- "Increase brightness"
- "Decrease brightness"

#### System Information

- "Battery status"
- "System info"
- "Disk space"
- "Running processes"
- "Network status"

### News Commands

- "What is the news"
- "Tell me the news"
- "Latest news"
- "Current news"
- "News update"

## Configuration

The assistant uses a `user_preferences.json` file to store user preferences. You can modify:

- Default name
- Email settings
- Weather location
- News preferences
- Voice preferences (rate and volume)

## Platform Support

### Windows

- Full system control features
- Audio control
- Display control
- System information

### Linux (Docker)

- Basic voice commands
- Weather information
- News updates
- Learning capabilities

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- pyttsx3 for text-to-speech conversion
- speech_recognition for voice recognition
- psutil for system information
- pycaw for audio control
- wmi for Windows Management Instrumentation
- Docker for containerization
- GitHub Actions for CI/CD

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---

Made with ❤️ by Subroto Saha
