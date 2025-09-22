import random
import time

words = [
    "python", "elephant", "banana", "unicorn", "laptop",
    "astronomy", "architecture", "biochemistry", "dictionary",
    "encyclopedia", "galaxy", "helicopter", "jellyfish", "kaleidoscope",
    "labyrinth", "microphone", "nightmare", "oxygen", "parachute",
    "quarantine", "rhinoceros", "saxophone", "television", "umbrella",
    "vocabulary", "watermelon", "xylophone", "yacht", "zeppelin", "zoology"
]

def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

score = 0
rounds = 5
time_limit = 30  # seconds per round

print("🎮 Welcome to Guess Word Extreme!")
print(f"You have {rounds} rounds. Each round you have {time_limit} seconds to guess.")

for round_num in range(1, rounds + 1):
    original = random.choice(words)
    lives = 5
    scrambled = scramble_word(original)

    print(f"\nRound {round_num}!")
    print("Shuffled word:", scrambled)
    start_time = time.time()

    while lives > 0:
        elapsed = time.time() - start_time
        if elapsed > time_limit:
            print("⏰ Time's up!")
            break

        guess = input(f"You have {int(time_limit - elapsed)} seconds left. Your guess: ").lower()

        if guess == original:
            print("✅ Correct! You win this round! 🎉")
            score += 1
            break
        else:
            lives -= 1
            matches = sum(min(guess.count(c), original.count(c)) for c in set(guess))
            print(f"❌ Nope! Letters matched: {matches}")

            if lives > 3:
                print(f"Hint: The word has {len(original)} letters.")
            elif lives > 1:
                vowels = sum(c in "aeiou" for c in original)
                print(f"Hint: It contains {vowels} vowels.")
            else:
                print("Last chance! Here's the first letter:", original[0])

            scrambled = scramble_word(original)
            print("New shuffled word:", scrambled)
            print(f"Lives left: {lives}")

    else:
        if lives == 0:
            print(f"💀 Game over! The word was: {original}")

print(f"\n🎉 Game finished! Your total score: {score} out of {rounds}")
