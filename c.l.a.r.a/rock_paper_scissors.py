import random
from sayAndListen import SayAndListen

class RockPaperScissors:
    def __init__(self):
        self.speech = SayAndListen()
        self.choices = ['rock', 'paper', 'scissors']
        self.score = {'user': 0, 'computer': 0}
    
    def get_computer_choice(self):
        """Get computer's choice"""
        return random.choice(self.choices)
    
    def determine_winner(self, user_choice, computer_choice):
        """Determine the winner of the game"""
        if user_choice == computer_choice:
            return "It's a tie!"
        
        winning_combinations = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
        
        if winning_combinations[user_choice] == computer_choice:
            self.score['user'] += 1
            return "You win!"
        else:
            self.score['computer'] += 1
            return "Computer wins!"
    
    def play_round(self, user_choice):
        """Play a round of rock paper scissors"""
        try:
            user_choice = user_choice.lower()
            if user_choice not in self.choices:
                return "Invalid choice. Please choose rock, paper, or scissors."
            
            computer_choice = self.get_computer_choice()
            result = self.determine_winner(user_choice, computer_choice)
            
            return f"You chose {user_choice}. Computer chose {computer_choice}. {result}\nScore - You: {self.score['user']}, Computer: {self.score['computer']}"
        except Exception as e:
            return f"Error playing game: {str(e)}"
    
    def reset_score(self):
        """Reset the score"""
        self.score = {'user': 0, 'computer': 0}
        return "Score reset"
    
    def get_score(self):
        """Get current score"""
        return f"Score - You: {self.score['user']}, Computer: {self.score['computer']}"
    
    def process_game_command(self, command):
        """Process game-related commands"""
        command = command.lower()
        
        if "play" in command:
            # Extract user's choice
            for choice in self.choices:
                if choice in command:
                    return self.play_round(choice)
            return "Please choose rock, paper, or scissors"
        
        elif "reset score" in command:
            return self.reset_score()
        
        elif "score" in command:
            return self.get_score()
        
        return "I didn't understand that game command" 