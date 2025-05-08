# C.L.A.R.A - Your Personal Voice Assistant

C.L.A.R.A (Conversational Learning Assistant with Responsive Actions) is a powerful, modular voice assistant built in Python. It supports a wide range of features and can be easily extended with new capabilities.

## Features

### Core Features

- Voice interaction with wake word detection ("Hey Clara")
- Natural language command processing
- Cross-platform support (Windows, Linux, macOS)
- Self-learning capabilities
- User preference management
- Conversation history tracking
- Emotional intelligence and personality adaptation

### Communication & Social

- WhatsApp integration
  - Send messages
  - Make calls
  - Contact management
- Email management
- Web search across multiple engines
  - Google
  - Wikipedia
  - YouTube
  - DuckDuckGo
  - Bing
  - Yahoo
  - GitHub
  - Stack Overflow
  - Reddit
  - Amazon

### Productivity & Organization

- Schedule Management
  - Add/remove schedules
  - Daily reminders
  - Recurring tasks
- Focus Mode
  - Productivity tracking
  - Distraction blocking
  - Session management
- App Launcher
  - Quick app access
  - Custom app configurations
  - Cross-platform support
- Password Management
  - Secure password storage
  - Master password protection
  - Service-specific passwords

### Entertainment & Media

- YouTube Controls
  - Play/pause
  - Search videos
  - Volume control
  - Fullscreen toggle
- Playlist Management
  - Create playlists
  - Add/remove songs
  - Play playlist
- Rock Paper Scissors Game
  - Score tracking
  - Multiple rounds
  - Statistics

### System & Utilities

- System Control
  - Shutdown/restart
  - Sleep/hibernate
  - System information
- Screenshot & Camera
  - Screen capture
  - Photo capture
  - Automatic file organization
- Internet Speed Test
  - Download speed
  - Upload speed
  - Ping measurement
- Language Translation
  - Multiple languages
  - Text translation
  - Language detection
- Calculator
  - Basic arithmetic
  - Complex calculations
  - Natural language processing

### Information & Updates

- Weather Information
  - Current conditions
  - Forecast
  - Location-based
- News Updates
  - Latest headlines
  - Category-specific news
  - Source selection
- IPL Live Scores
  - Match updates
  - Team scores
  - Match status

### Memory & Learning

- Remember System
  - Store information
  - Recall details
  - Context-aware memory
- Learning System
  - Command pattern recognition
  - User preference learning
  - Response optimization
  - Emotional adaptation

## Installation

1. Clone the repository:

```bash
git clone https://github.com/isubroto/c.l.a.r.a.git
cd c.l.a.r.a
```

2. Create and activate a virtual environment:

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install platform-specific dependencies:

- Windows: No additional steps required
- Linux: Install PortAudio and espeak

```bash
sudo apt-get install portaudio19-dev espeak
```

## Usage

1. Start C.L.A.R.A:

```bash
python clara_main.py
```

2. Use the wake word "Hey Clara" to activate the assistant

3. Available commands:

- "What's the weather like?"
- "Set an alarm for 7 AM"
- "Open YouTube"
- "Translate hello to Spanish"
- "Take a screenshot"
- "What's the time?"
- "Search for Python tutorials"
- "Play rock paper scissors"
- "Check IPL scores"
- "Start focus mode"
- "Send WhatsApp message to John"
- "Create a playlist called workout"
- "Calculate 25 times 13"
- "Test internet speed"
- "Show system information"
- "Remember that my favorite color is blue"
- And many more!

## Configuration

Configuration files are stored in JSON format:

- `user_preferences.json`: User preferences and settings
- `apps.json`: App launcher configurations
- `passwords.json`: Password manager data
- `schedule.json`: Schedule and reminder data
- `playlists.json`: Music playlist data
- `learning_data.json`: Learning system data
- `memory.json`: Remember system data

## Development

To contribute to the project:

1. Install development dependencies:

```bash
pip install -r requirements.txt[dev]
```

2. Run tests:

```bash
pytest
```

3. Check code style:

```bash
flake8
black .
mypy .
```

## Project Structure

```
c.l.a.r.a/
├── clara_main.py          # Main application file
├── command_handler.py     # Command processing
├── responses.py          # Response generation
├── learning.py          # Learning system
├── weather.py           # Weather information
├── temperature.py       # Temperature conversion
├── web_search.py        # Web search functionality
├── sayAndListen.py      # Speech interface
├── hotword_detector.py  # Wake word detection
├── alarm.py            # Alarm management
├── youtube_controls.py  # YouTube integration
├── remember.py         # Memory system
├── playlist.py         # Playlist management
├── calculator.py       # Calculator functionality
├── whatsapp.py         # WhatsApp integration
├── system_control.py   # System controls
├── password_protection.py # Password management
├── schedule.py         # Schedule management
├── app_launcher.py     # App launcher
├── speed_test.py       # Internet speed test
├── ipl_score.py        # IPL score updates
├── rock_paper_scissors.py # Game implementation
├── screenshot_camera.py # Screenshot and camera
└── translator.py       # Language translation
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- GitHub: [isubroto](https://github.com/isubroto)

## Acknowledgments

- Thanks to all contributors and users of C.L.A.R.A
- Built with Python and various open-source libraries
- Inspired by modern voice assistants and AI technology
