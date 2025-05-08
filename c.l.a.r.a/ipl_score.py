import requests
import json
from sayAndListen import SayAndListen

class IPLScore:
    def __init__(self):
        self.speech = SayAndListen()
        self.api_url = "https://cricapi.com/api/matches"  # You'll need to sign up for an API key
        self.api_key = "YOUR_API_KEY"  # Replace with your actual API key
    
    def get_live_scores(self):
        """Get live IPL match scores"""
        try:
            # Make API request
            response = requests.get(f"{self.api_url}?apikey={self.api_key}")
            data = response.json()
            
            # Filter for IPL matches
            ipl_matches = [match for match in data['matches'] if 'IPL' in match['name']]
            
            if not ipl_matches:
                return "No live IPL matches found"
            
            # Format scores
            scores = "Live IPL Scores:\n"
            for match in ipl_matches:
                scores += f"{match['name']}\n"
                scores += f"{match['status']}\n"
                if 'score' in match:
                    for team in match['score']:
                        scores += f"{team['name']}: {team['score']}\n"
                scores += "\n"
            
            return scores
        except Exception as e:
            return f"Error getting IPL scores: {str(e)}"
    
    def process_ipl_command(self, command):
        """Process IPL-related commands"""
        command = command.lower()
        
        if "ipl score" in command or "live score" in command:
            return self.get_live_scores()
        
        return "I didn't understand that IPL command" 