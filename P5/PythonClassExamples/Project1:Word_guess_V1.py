import random

words = ["python", "elephant", "banana", "unicorn", "laptop"]
original = random.choice(words)

shuffled = list(original)
random.shuffle(shuffled)
shuffled_word = ''.join(shuffled)

print("🎮 Welcome to Guess Word!")
print("Can you guess the correct word from this jumble?")
print("Shuffled word:", shuffled_word)

lives = 3

while lives > 0:
    guess = input("Your guess: ").lower()

    if guess == original:
        print("✅ Correct! You win! 🎉")
        break
    else:
        lives -= 1
        print("❌ Nope! Try again.")
        if lives > 0:
            hint = original[:lives]  
            print(f"Hint: The word starts with '{hint}'")
            print(f"Lives left: {lives}")
        else:
            print("💀 Game over! The word was:", original)
