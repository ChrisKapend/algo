import random, hangman_art, hangman_word, os

# Step 1
stages = hangman_art.stages
word_list = hangman_word.word_list

# TODO - 1 Randomly choose a word from the world_list and assign it to a variable called chosen_word
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
lives = 6
for i in range(word_length):
    display += "_"
# TODO - 2 Ask the user to guess a letter and assign their answer to a variable called guess. Make Guess lowercase
while "_" in display and lives > 0:
    guess = str(input("Guess a letter: "))[0].lower()
    # Clearing the screen
    clear = lambda: os.system('cls')
    clear()
    # TODO - 3 Check if the letter the user guessed (guess) is one of the letters in the chosen_word
    if guess in display:
        # Give user feedback on what he guessed
        print(f"You've already guessed the letter '{guess}'.")
    if guess not in chosen_word.lower():
        # Give user feedback on his guess
        print(f"You've guessed the word '{guess}'. but it is not in the word")
        lives -= 1
        print(stages[lives])
    for i in range(word_length):
        letter = chosen_word[i]
        if letter.lower() == guess:
            display[i] = letter
    # Print the word instead of the array containing the letters
    print(f"{' '.join(display)}")
else:
    if "_" not in display:
        print(f"You win")
    else:
        print(f"The word was: {chosen_word}")
        print(f"Game Over")
