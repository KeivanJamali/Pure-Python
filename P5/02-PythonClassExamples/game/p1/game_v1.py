# game.py

import random

class StonePaperScissors:
    CHOICES = ["stone", "paper", "scissors"]

    def __init__(self, mode="computer", difficulty="easy"):
        self.mode = mode
        self.difficulty = difficulty
        self.user1_score = 0
        self.user2_score = 0
        self.last_user_choice = None
        self.last_result = None

    def determine_winner(self, choice1, choice2):
        if choice1 == choice2:
            return "draw"
        elif (choice1 == "stone" and choice2 == "scissors") \
             or (choice1 == "scissors" and choice2 == "paper") \
             or (choice1 == "paper" and choice2 == "stone"):
            return "user1"
        else:
            return "user2"

    def get_computer_choice(self, user_choice=None):
        if self.difficulty == "easy":
            return random.choice(self.CHOICES)
        elif self.difficulty == "moderate":
            # Try to counter the user's previous move
            if self.last_user_choice:
                # Pick the move that beats the last user move
                return self._winning_move(self.last_user_choice)
            else:
                return random.choice(self.CHOICES)
        elif self.difficulty == "hard":
            # Always pick the move that beats the user's current move
            if user_choice:
                return self._winning_move(user_choice)
            else:
                return random.choice(self.CHOICES)
        else:
            return random.choice(self.CHOICES)

    def _winning_move(self, move):
        # Returns the move that beats the given move
        if move == "stone":
            return "paper"
        elif move == "paper":
            return "scissors"
        elif move == "scissors":
            return "stone"
        return random.choice(self.CHOICES)

    def update_last(self, user_choice, result):
        self.last_user_choice = user_choice
        self.last_result = result

    # --- New scoring helpers ---
    def apply_round_winner(self, winner: str):
        """Increment score based on round winner.

        Returns:
            match_winner (str|None): 'user1' or 'user2' if someone reached 3, else None
        """
        if winner == "user1":
            self.user1_score += 1
        elif winner == "user2":
            self.user2_score += 1

        if self.user1_score >= 3:
            return "user1"
        if self.user2_score >= 3:
            return "user2"
        return None

    def reset_scores(self):
        self.user1_score = 0
        self.user2_score = 0
