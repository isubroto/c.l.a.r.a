import json
import os
import webbrowser
import pyautogui
import time
from sayAndListen import SayAndListen

class PlaylistManager:
    def __init__(self):
        self.playlists_file = 'playlists.json'
        self.playlists = {}
        self.speech = SayAndListen()
        self.load_playlists()
    
    def load_playlists(self):
        """Load saved playlists from file"""
        try:
            if os.path.exists(self.playlists_file):
                with open(self.playlists_file, 'r') as f:
                    self.playlists = json.load(f)
        except Exception as e:
            print(f"Error loading playlists: {e}")
            self.playlists = {}
    
    def save_playlists(self):
        """Save playlists to file"""
        try:
            with open(self.playlists_file, 'w') as f:
                json.dump(self.playlists, f, indent=4)
        except Exception as e:
            print(f"Error saving playlists: {e}")
    
    def create_playlist(self, name):
        """Create a new playlist"""
        try:
            if name in self.playlists:
                return f"Playlist '{name}' already exists"
            
            self.playlists[name] = []
            self.save_playlists()
            return f"Created new playlist '{name}'"
        except Exception as e:
            return f"Error creating playlist: {str(e)}"
    
    def add_to_playlist(self, playlist_name, song):
        """Add a song to a playlist"""
        try:
            if playlist_name not in self.playlists:
                return f"Playlist '{playlist_name}' doesn't exist"
            
            self.playlists[playlist_name].append(song)
            self.save_playlists()
            return f"Added '{song}' to playlist '{playlist_name}'"
        except Exception as e:
            return f"Error adding to playlist: {str(e)}"
    
    def remove_from_playlist(self, playlist_name, song):
        """Remove a song from a playlist"""
        try:
            if playlist_name not in self.playlists:
                return f"Playlist '{playlist_name}' doesn't exist"
            
            if song in self.playlists[playlist_name]:
                self.playlists[playlist_name].remove(song)
                self.save_playlists()
                return f"Removed '{song}' from playlist '{playlist_name}'"
            return f"Song '{song}' not found in playlist '{playlist_name}'"
        except Exception as e:
            return f"Error removing from playlist: {str(e)}"
    
    def list_playlists(self):
        """List all playlists"""
        if not self.playlists:
            return "No playlists found"
        
        playlist_list = "Available playlists:\n"
        for name, songs in self.playlists.items():
            playlist_list += f"- {name} ({len(songs)} songs)\n"
        return playlist_list
    
    def show_playlist(self, playlist_name):
        """Show songs in a playlist"""
        try:
            if playlist_name not in self.playlists:
                return f"Playlist '{playlist_name}' doesn't exist"
            
            if not self.playlists[playlist_name]:
                return f"Playlist '{playlist_name}' is empty"
            
            song_list = f"Songs in playlist '{playlist_name}':\n"
            for i, song in enumerate(self.playlists[playlist_name], 1):
                song_list += f"{i}. {song}\n"
            return song_list
        except Exception as e:
            return f"Error showing playlist: {str(e)}"
    
    def play_playlist(self, playlist_name):
        """Play a playlist on YouTube"""
        try:
            if playlist_name not in self.playlists:
                return f"Playlist '{playlist_name}' doesn't exist"
            
            if not self.playlists[playlist_name]:
                return f"Playlist '{playlist_name}' is empty"
            
            # Open YouTube
            webbrowser.open("https://www.youtube.com")
            time.sleep(2)
            
            # Search for first song
            first_song = self.playlists[playlist_name][0]
            pyautogui.hotkey('ctrl', 'l')
            pyautogui.write(f"https://www.youtube.com/results?search_query={first_song.replace(' ', '+')}")
            pyautogui.press('enter')
            
            return f"Playing playlist '{playlist_name}'"
        except Exception as e:
            return f"Error playing playlist: {str(e)}"
    
    def delete_playlist(self, playlist_name):
        """Delete a playlist"""
        try:
            if playlist_name not in self.playlists:
                return f"Playlist '{playlist_name}' doesn't exist"
            
            del self.playlists[playlist_name]
            self.save_playlists()
            return f"Deleted playlist '{playlist_name}'"
        except Exception as e:
            return f"Error deleting playlist: {str(e)}"
    
    def process_playlist_command(self, command):
        """Process playlist-related commands"""
        command = command.lower()
        
        if "create playlist" in command:
            # Extract playlist name
            name = command.replace("create playlist", "").strip()
            if name:
                return self.create_playlist(name)
            return "Please specify a playlist name"
        
        elif "add to playlist" in command:
            # Extract playlist name and song
            try:
                parts = command.replace("add to playlist", "").strip().split(" song ", 1)
                if len(parts) == 2:
                    playlist_name, song = parts
                    return self.add_to_playlist(playlist_name.strip(), song.strip())
                return "Please specify playlist name and song"
            except Exception as e:
                return f"Error processing add command: {str(e)}"
        
        elif "remove from playlist" in command:
            # Extract playlist name and song
            try:
                parts = command.replace("remove from playlist", "").strip().split(" song ", 1)
                if len(parts) == 2:
                    playlist_name, song = parts
                    return self.remove_from_playlist(playlist_name.strip(), song.strip())
                return "Please specify playlist name and song"
            except Exception as e:
                return f"Error processing remove command: {str(e)}"
        
        elif "list playlists" in command:
            return self.list_playlists()
        
        elif "show playlist" in command:
            # Extract playlist name
            name = command.replace("show playlist", "").strip()
            if name:
                return self.show_playlist(name)
            return "Please specify a playlist name"
        
        elif "play playlist" in command:
            # Extract playlist name
            name = command.replace("play playlist", "").strip()
            if name:
                return self.play_playlist(name)
            return "Please specify a playlist name"
        
        elif "delete playlist" in command:
            # Extract playlist name
            name = command.replace("delete playlist", "").strip()
            if name:
                return self.delete_playlist(name)
            return "Please specify a playlist name"
        
        return "I didn't understand that playlist command" 