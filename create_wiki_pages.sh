#!/bin/bash

# Create wiki directory if it doesn't exist
mkdir -p c.l.a.r.a.wiki

# Create all wiki pages
cat > c.l.a.r.a.wiki/Home.md << 'EOL'
# Welcome to C.L.A.R.A Wiki

C.L.A.R.A (Conversational Learning Assistant with Responsive Actions) is an advanced AI assistant designed to help you with various tasks through natural conversation. This wiki serves as the central documentation for understanding, using, and contributing to C.L.A.R.A.

## Quick Links

- [Getting Started](Getting-Started)
- [Features](Features)
- [Installation Guide](Installation-Guide)
- [User Guide](User-Guide)
- [Developer Guide](Developer-Guide)
- [Security](Security)
- [FAQ](FAQ)

## What is C.L.A.R.A?

C.L.A.R.A is a Python-based AI assistant that combines natural language processing, voice recognition, and various integrated services to provide a comprehensive personal assistant experience. It's designed to be:

- **Conversational**: Natural language interaction
- **Learning**: Adapts to your preferences and usage patterns
- **Responsive**: Quick and accurate responses
- **Adaptable**: Customizable to your needs

## Core Features

- Voice command recognition
- Natural language processing
- Task automation
- System control
- Web services integration
- Learning capabilities
- Security features

## Getting Started

To get started with C.L.A.R.A:

1. Check the [Installation Guide](Installation-Guide) for setup instructions
2. Read the [User Guide](User-Guide) for basic usage
3. Explore [Features](Features) to learn about available capabilities
4. Visit [FAQ](FAQ) for common questions

## Contributing

We welcome contributions! To get involved:

1. Read our [Contributing Guidelines](Contributing-Guidelines)
2. Check the [Developer Guide](Developer-Guide)
3. Review our [Code of Conduct](Code-of-Conduct)
4. Join our [Discord community](https://discord.gg/clara-assistant)

## Support

Need help? Here's how to get support:

- [GitHub Issues](https://github.com/isubroto/c.l.a.r.a/issues)
- [Discord Server](https://discord.gg/clara-assistant)
- [Documentation](Documentation)
- [FAQ](FAQ)

## Security

Security is a top priority. Please review our:

- [Security Policy](Security)
- [Vulnerability Reporting](Vulnerability-Reporting)
- [Privacy Policy](Privacy-Policy)

## License

C.L.A.R.A is licensed under the MIT License. See the [LICENSE](https://github.com/isubroto/c.l.a.r.a/blob/main/LICENSE) file for details.

## Stay Updated

- [GitHub Releases](https://github.com/isubroto/c.l.a.r.a/releases)
- [Changelog](Changelog)
- [Blog](https://clara-assistant.com/blog)
- [Twitter](https://twitter.com/clara_assistant)

---

*This wiki is maintained by the C.L.A.R.A community. Feel free to contribute by submitting pull requests or opening issues for improvements.*
EOL

cat > c.l.a.r.a.wiki/Getting-Started.md << 'EOL'
# Getting Started with C.L.A.R.A

This guide will help you get up and running with C.L.A.R.A quickly and efficiently.

## Prerequisites

Before installing C.L.A.R.A, ensure you have:

- Python 3.13 or higher
- pip (Python package manager)
- Git
- A microphone (for voice commands)
- Speakers (for voice responses)
- Internet connection

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/isubroto/c.l.a.r.a.git
cd c.l.a.r.a
```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
# API Keys (if needed)
OPENAI_API_KEY=your_openai_api_key
WEATHER_API_KEY=your_weather_api_key

# Configuration
DEBUG=False
LOG_LEVEL=INFO
```

## First Run

1. Start C.L.A.R.A:
```bash
python clara_main.py
```

2. Wait for the initialization message
3. Say "Hey Clara" to activate
4. Try a simple command like "What time is it?"

## Basic Commands

Here are some commands to get you started:

- "Hey Clara" - Wake up the assistant
- "What time is it?" - Get current time
- "What's the weather like?" - Get weather information
- "Open Chrome" - Launch applications
- "Take a screenshot" - Capture screen
- "Set an alarm for 7 AM" - Set alarms
- "Remember that I have a meeting at 3 PM" - Set reminders

## Configuration

### Voice Settings

You can adjust voice settings in `config.json`:

```json
{
  "voice": {
    "rate": 1.0,
    "volume": 1.0,
    "voice_id": "default"
  }
}
```

### Wake Word

Customize wake words in `hotword_detector.py`:

```python
self.wake_words = [
    "hey clara",
    "hi clara",
    "hello clara"
]
```

## Troubleshooting

### Common Issues

1. **Microphone not working**
   - Check system permissions
   - Verify microphone is selected as input device
   - Test microphone in system settings

2. **Voice recognition issues**
   - Ensure clear pronunciation
   - Reduce background noise
   - Check internet connection

3. **Command not recognized**
   - Try rephrasing the command
   - Check command syntax in documentation
   - Verify feature is enabled

### Getting Help

If you encounter issues:

1. Check the [FAQ](FAQ)
2. Search [GitHub Issues](https://github.com/isubroto/c.l.a.r.a/issues)
3. Join our [Discord](https://discord.gg/clara-assistant)
4. Review the [Documentation](Documentation)

## Next Steps

Now that you're set up, explore:

- [Features](Features) - Discover all capabilities
- [User Guide](User-Guide) - Learn advanced usage
- [Developer Guide](Developer-Guide) - Contribute to the project
- [Security](Security) - Understand security features

## Feedback

We value your feedback! Help us improve by:

- Reporting issues on GitHub
- Suggesting new features
- Contributing to documentation
- Sharing your experience

---

*Need more help? Check our [Support](Support) page or join our [Discord community](https://discord.gg/clara-assistant).*
EOL

cat > c.l.a.r.a.wiki/Features.md << 'EOL'
# C.L.A.R.A Features

C.L.A.R.A comes with a comprehensive set of features designed to make your life easier. Here's a detailed overview of what C.L.A.R.A can do.

## Core Features

### Voice Interaction
- Natural language processing
- Voice command recognition
- Text-to-speech responses
- Wake word detection
- Ambient noise adaptation

### Learning System
- Command history tracking
- User preference learning
- Pattern recognition
- Usage analysis
- Smart suggestions

### System Control
- Application launching
- System volume control
- Screen brightness adjustment
- Power management
- Screenshot capture
- Camera access

## Communication Features

### Messaging
- WhatsApp integration
- Message composition
- Contact management
- Message scheduling
- Read receipts

### Email
- Email composition
- Inbox management
- Email scheduling
- Attachment handling
- Email templates

## Productivity Tools

### Task Management
- To-do list creation
- Task reminders
- Priority setting
- Due date tracking
- Task categories

### Calendar
- Event scheduling
- Meeting reminders
- Calendar sync
- Recurring events
- Availability checking

### Notes
- Voice notes
- Text notes
- Note organization
- Search functionality
- Note sharing

## Entertainment

### Media Control
- YouTube video playback
- Music control
- Playlist management
- Volume control
- Playback commands

### Games
- Rock Paper Scissors
- Word games
- Trivia
- Number games
- Memory games

## Information Services

### Weather
- Current conditions
- Forecast
- Weather alerts
- Location-based weather
- Weather history

### News
- Headline updates
- Category-based news
- Source selection
- News search
- News alerts

### Sports
- Live scores
- Team updates
- Player statistics
- Match schedules
- Sports news

## Utilities

### Calculator
- Basic arithmetic
- Scientific calculations
- Unit conversion
- Currency conversion
- Calculation history

### Translation
- Text translation
- Voice translation
- Language detection
- Phrase book
- Translation history

### Internet
- Speed testing
- Connection status
- Network diagnostics
- IP information
- DNS lookup

## Security Features

### Password Management
- Secure storage
- Password generation
- Password strength checking
- Auto-fill capability
- Password sharing

### System Security
- File encryption
- Secure communication
- Access control
- Activity logging
- Security alerts

## Customization

### Voice Settings
- Voice selection
- Speech rate
- Volume control
- Pitch adjustment
- Accent options

### Interface
- Theme selection
- Layout customization
- Command shortcuts
- Display preferences
- Notification settings

### Integration
- API connections
- Service linking
- Custom commands
- Plugin support
- Webhook integration

## Advanced Features

### Automation
- Task scheduling
- Event triggers
- Conditional actions
- Workflow creation
- Macro support

### Analytics
- Usage statistics
- Performance metrics
- Error tracking
- User behavior analysis
- System health monitoring

### Development
- API documentation
- Plugin development
- Custom module creation
- Testing tools
- Debugging support

## Platform Support

### Operating Systems
- Windows
- Linux
- macOS
- Mobile devices
- Web interface

### Devices
- Desktop computers
- Laptops
- Smartphones
- Tablets
- Smart speakers

## Future Features

We're constantly working on new features. Here's what's coming:

- [ ] Advanced AI capabilities
- [ ] More language support
- [ ] Enhanced security features
- [ ] Additional integrations
- [ ] Mobile app development

---

*Want to suggest a new feature? Visit our [GitHub Issues](https://github.com/isubroto/c.l.a.r.a/issues) or join our [Discord community](https://discord.gg/clara-assistant).*
EOL

cat > c.l.a.r.a.wiki/_Sidebar.md << 'EOL'
# Navigation

* [Home](Home)
* [Getting Started](Getting-Started)
* [Features](Features)
* [Installation Guide](Installation-Guide)
* [User Guide](User-Guide)
* [Developer Guide](Developer-Guide)
* [Security](Security)
* [FAQ](FAQ)
* [Contributing Guidelines](Contributing-Guidelines)
* [Code of Conduct](Code-of-Conduct)
* [Vulnerability Reporting](Vulnerability-Reporting)
* [Privacy Policy](Privacy-Policy)
* [Changelog](Changelog)
EOL

# Make the script executable
chmod +x create_wiki_pages.sh

echo "Wiki pages created successfully!" 