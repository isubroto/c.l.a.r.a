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

_Need more help? Check our [Support](Support) page or join our [Discord community](https://discord.gg/clara-assistant)._
