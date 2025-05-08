import webbrowser
import requests
from bs4 import BeautifulSoup
import wikipedia
from sayAndListen import SayAndListen
import json
import os
from datetime import datetime

class WebSearch:
    def __init__(self):
        # Search engine URLs
        self.search_engines = {
            'google': "https://www.google.com/search?q=",
            'youtube': "https://www.youtube.com/results?search_query=",
            'duckduckgo': "https://duckduckgo.com/?q=",
            'bing': "https://www.bing.com/search?q=",
            'yahoo': "https://search.yahoo.com/search?p=",
            'github': "https://github.com/search?q=",
            'stackoverflow': "https://stackoverflow.com/search?q=",
            'reddit': "https://www.reddit.com/search/?q=",
            'amazon': "https://www.amazon.com/s?k=",
            'wikipedia': "https://en.wikipedia.org/wiki/Special:Search?search="
        }
        
        # Search history file
        self.history_file = 'search_history.json'
        self.load_search_history()
        self.speech = SayAndListen()
        
    def load_search_history(self):
        """Load search history from file"""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r') as f:
                    self.search_history = json.load(f)
            else:
                self.search_history = []
        except Exception:
            self.search_history = []
    
    def save_search_history(self, engine, query):
        """Save search to history"""
        try:
            self.search_history.append({
                'engine': engine,
                'query': query,
                'timestamp': datetime.now().isoformat()
            })
            # Keep only last 100 searches
            self.search_history = self.search_history[-100:]
            with open(self.history_file, 'w') as f:
                json.dump(self.search_history, f)
        except Exception:
            pass  # Silently fail if can't save history
    
    def get_search_engine(self, query):
        """Dynamically determine search engine from query"""
        query = query.lower()
        for engine in self.search_engines:
            if engine in query:
                return engine
        return 'google'  # Default to Google
    
    def search(self, query, engine=None):
        """Perform a search using specified or detected engine"""
        try:
            # Determine search engine if not specified
            if not engine:
                engine = self.get_search_engine(query)
            
            # Clean query
            query = self.clean_query(query, engine)
            
            # Get search URL
            if engine in self.search_engines:
                search_url = self.search_engines[engine] + query.replace(" ", "+")
                webbrowser.open(search_url)
                self.speech.speak(f"Searching {engine.title()} for {query}")
                self.save_search_history(engine, query)
            else:
                self.speech.speak(f"Sorry, I don't support searching on {engine}")
                
        except Exception as e:
            self.speech.speak(f"Sorry, I couldn't perform the search on {engine}")
    
    def clean_query(self, query, engine):
        """Clean and format query based on search engine"""
        # Remove engine name and common prefixes
        prefixes = [
            f"search {engine} for",
            f"search on {engine} for",
            f"search {engine}",
            f"look up on {engine}",
            f"find on {engine}",
            engine
        ]
        
        for prefix in prefixes:
            query = query.replace(prefix, "").strip()
        
        return query
    
    def wikipedia_search(self, query):
        """Enhanced Wikipedia search with more features"""
        try:
            # Clean query
            query = self.clean_query(query, 'wikipedia')
            
            # Search Wikipedia
            search_results = wikipedia.search(query)
            if not search_results:
                self.speech.speak(f"Sorry, I couldn't find any Wikipedia articles about {query}")
                return

            # Get the first result
            page = wikipedia.page(search_results[0])
            
            # Get summary with more sentences
            summary = wikipedia.summary(search_results[0], sentences=3)
            self.speech.speak(summary)
            
            # Get related topics
            related = page.links[:3]  # Get first 3 related topics
            if related:
                self.speech.speak("Related topics include: " + ", ".join(related))
            
            # Ask if user wants to read more
            self.speech.speak("Would you like me to open the full article in your browser?")
            
            # Save to history
            self.save_search_history('wikipedia', query)
            
        except wikipedia.exceptions.DisambiguationError as e:
            self.speech.speak(f"There are multiple results for {query}. Here are some options: {', '.join(e.options[:5])}")
        except Exception as e:
            self.speech.speak("Sorry, I couldn't search Wikipedia at the moment")
    
    def get_search_history(self, limit=5):
        """Get recent search history"""
        if not self.search_history:
            self.speech.speak("You haven't made any searches yet.")
            return
        
        recent = self.search_history[-limit:]
        self.speech.speak("Here are your recent searches:")
        for search in recent:
            self.speech.speak(f"Searched {search['engine']} for {search['query']}")
    
    def process_search_command(self, query):
        """Process different types of search commands"""
        query = query.lower()
        
        # Handle history request
        if "search history" in query or "recent searches" in query:
            self.get_search_history()
            return
        
        # Handle Wikipedia search
        if "wikipedia" in query:
            self.wikipedia_search(query)
            return
        
        # Handle other search engines
        engine = self.get_search_engine(query)
        self.search(query, engine) 