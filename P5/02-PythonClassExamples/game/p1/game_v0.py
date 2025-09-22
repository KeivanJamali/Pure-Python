import random

class StonePaperScissors:
    CHOICES = ["stone", "paper", "scissors"]

    def __init__(self, mode="computer"):
        """
        mode: "computer" -> play vs computer
              "friend"   -> play vs another person
        """
        self.mode = mode
        self.user1_score = 0
        self.user2_score = 0

    def get_user_choice(self, player_name="Player"):
        """Ask a player for a valid choice."""
        choice = input(f"{player_name}, enter stone, paper, or scissors: ").strip().lower()
        while choice not in self.CHOICES:
            print("Invalid choice! Try again.")
            choice = input(f"{player_name}, enter stone, paper, or scissors: ").strip().lower()
        return choice

    def get_computer_choice(self):
        """Randomly pick a choice for the computer."""
        return random.choice(self.CHOICES)

    def determine_winner(self, choice1, choice2):
        """Determine the winner between two choices."""
        if choice1 == choice2:
            return "draw"
        elif (choice1 == "stone" and choice2 == "scissors") \
             or (choice1 == "scissors" and choice2 == "paper") \
             or (choice1 == "paper" and choice2 == "stone"):
            return "user1"
        else:
            return "user2"

    def play_round(self):
        """Play one round based on mode."""
        if self.mode == "computer":
            user_choice = self.get_user_choice("You")
            computer_choice = self.get_computer_choice()

            print(f"\nYou chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")

            winner = self.determine_winner(user_choice, computer_choice)
            if winner == "draw":
                print("It's a draw!")
            elif winner == "user1":
                print("You win this round! 🎉")
                self.user1_score += 1
            else:
                print("Computer wins this round! 💻")
                self.user2_score += 1

        elif self.mode == "friend":
            user1_choice = self.get_user_choice("Player 1")
            print("\n" * 50)  # clear screen so Player 2 doesn't see Player 1's choice
            user2_choice = self.get_user_choice("Player 2")

            print(f"\nPlayer 1 chose: {user1_choice}")
            print(f"Player 2 chose: {user2_choice}")

            winner = self.determine_winner(user1_choice, user2_choice)
            if winner == "draw":
                print("It's a draw!")
            elif winner == "user1":
                print("Player 1 wins this round! 🏆")
                self.user1_score += 1
            else:
                print("Player 2 wins this round! 🏆")
                self.user2_score += 1

        print(f"Score -> Player 1: {self.user1_score}, Player 2: {self.user2_score}\n")

    def play_game(self):
        """Main game loop."""
        mode_name = "Computer" if self.mode == "computer" else "Friend"
        print(f"=== Welcome to Stone, Paper, Scissors ({mode_name} Mode) ===")
        while True:
            self.play_round()
            again = input("Do you want to play again? (yes/no): ").strip().lower()
            if again != "yes":
                print("\nFinal Score:")
                print(f"Player 1: {self.user1_score} | Player 2: {self.user2_score}")
                print("Thanks for playing! Goodbye 👋")
                break


if __name__ == "__main__":
    print("Choose game mode:")
    print("1. Play vs Computer")
    print("2. Play vs Friend")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        game = StonePaperScissors(mode="computer")
    else:
        game = StonePaperScissors(mode="friend")

    game.play_game()
