import random

# List of words for the game
word_list = ['python', 'developer', 'program', 'hangman', 'computer', 'algorithm']

# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to display the current state of the word
def display_word(word, correct_guesses):
    display = ''.join([letter if letter in correct_guesses else '_' for letter in word])
    return display

# Main hangman game function
def hangman_game():
    word = choose_word()
    correct_guesses = []
    incorrect_guesses = []
    attempts = 6  # Maximum number of incorrect guesses

    print("Welcome to Hangman!")

    # Main game loop
    while attempts > 0:
        print(f"\nWord: {display_word(word, correct_guesses)}")
        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
        print(f"Remaining attempts: {attempts}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in correct_guesses or guess in incorrect_guesses:
            print("You've already guessed that letter.")
            continue

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            correct_guesses.append(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses.append(guess)
            attempts -= 1

        # Check if the player has guessed the whole word
        if all(letter in correct_guesses for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nGame over! The word was: {word}")

# Run the game
if __name__ == "__main__":
    hangman_game()
