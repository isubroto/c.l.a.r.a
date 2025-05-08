# C.L.A.R.A - Command Line Assistant with Real-time Audio

A powerful command-line assistant that combines speech recognition, text-to-speech, and natural language processing to provide a seamless voice interaction experience.

## Features

- 🎤 Real-time speech recognition
- 🔊 Text-to-speech capabilities
- 🌤️ Weather information
- 📰 News updates
- 🎵 Music control
- 📝 Note-taking
- 🔍 Advanced Web Search
  - Google search (default)
  - Wikipedia search with summaries
  - YouTube search
  - DuckDuckGo search
  - Bing search
  - Yahoo search
  - GitHub search
  - Stack Overflow search
  - Reddit search
  - Amazon search
- 📧 Email management
- 🎮 System control
- 🤖 AI-powered responses
- 📚 Search history tracking
- 🔄 Dynamic command processing

## Requirements

- Python 3.13 or higher
- Windows 10/11 (for full functionality)
- Microphone and speakers
- Internet connection

## Installation

1. Clone the repository:

```bash
git clone https://github.com/isubroto/c.l.a.r.a.git
cd c.l.a.r.a
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the assistant:

```bash
python c.l.a.r.a/Jarvis_main.py
```

2. Use wake words:

- "Hey Clara"
- "Hello Clara"
- "Clara"

3. Available commands:

### Search Commands

- "Search for [query]" (Google)
- "Search Wikipedia for [query]"
- "Search YouTube for [query]"
- "Search GitHub for [query]"
- "Search Stack Overflow for [query]"
- "Search Reddit for [query]"
- "Search Amazon for [query]"
- "Search Bing for [query]"
- "Search Yahoo for [query]"
- "Search DuckDuckGo for [query]"
- "Show search history"
- "Recent searches"

### Other Commands

- "What's the weather in [city]?"
- "Tell me the news"
- "Play music"
- "Take a note"
- "Send email"
- "System status"

## Development

### Project Structure

```
c.l.a.r.a/
├── Jarvis_main.py      # Main application entry
├── command_handler.py  # Command processing
├── responses.py        # Response generation
├── learning.py         # Learning system
├── weather.py          # Weather module
├── sayAndListen.py     # Speech handling
├── web_search.py       # Web search functionality
└── tests/             # Test suite
```

### Running Tests

```bash
python -m unittest discover c.l.a.r.a/tests
```

### Development Dependencies

Install development dependencies:

```bash
pip install -r requirements.txt[dev]
```

## Docker Support

Build and run with Docker:

```bash
docker build -t isubroto/clara .
docker run -it isubroto/clara
```

## CI/CD Pipeline

The project uses GitHub Actions for continuous integration and deployment:

- Automated testing on Windows
- Docker image building and publishing
- Code quality checks

## Platform Support

- Windows: Full support with all features
- Linux: Basic functionality (limited system control)
- macOS: Basic functionality (limited system control)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- isubroto

## Acknowledgments

- OpenAI for language models
- Google for speech recognition
- Microsoft for Windows integration
- Wikipedia for knowledge base
- Various search engines for web search capabilities
