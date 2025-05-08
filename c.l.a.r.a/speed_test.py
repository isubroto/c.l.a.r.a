import speedtest
import time
import requests
from sayAndListen import SayAndListen

class SpeedTester:
    def __init__(self):
        """Initialize the SpeedTester with speech interface."""
        self.speech = SayAndListen()
        self.st = None
        self.initialize_speedtest()
        
    def initialize_speedtest(self):
        """Initialize speedtest with error handling."""
        try:
            self.st = speedtest.Speedtest()
            self.st.get_best_server()
        except Exception as e:
            print(f"Warning: Could not initialize speedtest: {str(e)}")
            self.st = None
    
    def test_speed(self):
        """Test internet speed and return formatted results."""
        try:
            if not self.st:
                # Try to reinitialize if not available
                self.initialize_speedtest()
                if not self.st:
                    return self.test_speed_alternative()
            
            # Get best server
            self.speech.speak("Finding best server...")
            self.st.get_best_server()
            
            # Test download speed
            self.speech.speak("Testing download speed...")
            download_speed = self.st.download() / 1_000_000  # Convert to Mbps
            
            # Test upload speed
            self.speech.speak("Testing upload speed...")
            upload_speed = self.st.upload() / 1_000_000  # Convert to Mbps
            
            # Get ping
            ping = self.st.results.ping
            
            # Format results
            results = {
                'download': round(download_speed, 2),
                'upload': round(upload_speed, 2),
                'ping': round(ping, 2)
            }
            
            return results
            
        except Exception as e:
            print(f"Error in speedtest: {str(e)}")
            return self.test_speed_alternative()
    
    def test_speed_alternative(self):
        """Alternative speed test using direct download test."""
        try:
            self.speech.speak("Using alternative speed test method...")
            
            # Test download speed using a large file
            test_url = "http://speedtest.ftp.otenet.gr/files/test100Mb.db"
            start_time = time.time()
            
            response = requests.get(test_url, stream=True)
            total_size = 0
            
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    total_size += len(chunk)
                    if time.time() - start_time >= 10:  # Test for 10 seconds
                        break
            
            duration = time.time() - start_time
            download_speed = (total_size * 8) / (1_000_000 * duration)  # Convert to Mbps
            
            # Simple ping test
            ping = self.test_ping()
            
            results = {
                'download': round(download_speed, 2),
                'upload': 'N/A',  # Upload test not available in alternative method
                'ping': round(ping, 2) if ping else 'N/A'
            }
            
            return results
            
        except Exception as e:
            return f"Error in alternative speed test: {str(e)}"
    
    def test_ping(self):
        """Test ping to a reliable server."""
        try:
            start_time = time.time()
            requests.get("http://www.google.com", timeout=5)
            return (time.time() - start_time) * 1000  # Convert to milliseconds
        except:
            return None
    
    def process_speed_command(self, command):
        """Process speed test related commands."""
        command = command.lower()
        
        if "test" in command and "speed" in command:
            self.speech.speak("Starting internet speed test. This may take a minute...")
            results = self.test_speed()
            
            if isinstance(results, dict):
                response = (
                    f"Speed test results:\n"
                    f"Download: {results['download']} Mbps\n"
                    f"Upload: {results['upload']} Mbps\n"
                    f"Ping: {results['ping']} ms"
                )
            else:
                response = results
                
            return response
            
        return "I can help you test your internet speed. Just say 'test speed' or 'check internet speed'." 