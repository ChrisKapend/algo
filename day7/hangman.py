import random

# Step 1

world_list = ["Jane", "Chris", "Eliott", "Joy", "Josiane"]

# TODO - 1 Randomly choose a word from the world_list and assign it to a variable called chosen_word
chosen_word = random.choice(world_list)
display = []
word_length = len(chosen_word)
for i in range(word_length):
    display += "_"
# TODO - 2 Ask the user to guess a letter and assign their answer to a variable called guess. Make Guess lowercase
while "_" in display:
    guess = str(input("Guess a letter: "))[0].lower()
# TODO - 3 Check if the letter the user guessed (guess) is one of the letters in the chosen_word
    for i in range(word_length):
        letter = chosen_word[i]
        if letter.lower() == guess:
            display[i] = letter

    print(display)
else:
    print(f"You win")