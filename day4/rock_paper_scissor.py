from random import randint

print("Welcome to Daddy's rock paper scissors game!")
user_input = int(input("Select 0 for rock, 1 for paper, 2 for scissors\n"))
computer_choice = randint(0,2)

logos_choices = ["🪨", "🧻", "✂️"]

if user_input == computer_choice:
    print("it's a tie, you've both chose", logos_choices[user_input])
elif 0 < user_input > 2:
    print("please enter a valid number")
elif user_input == 0 and computer_choice == 2:
    print(f"You've won!")
    print(f"You      : {logos_choices[user_input]}")
    print(f"Computer : {logos_choices[computer_choice]}")
elif user_input == 1 and computer_choice == 0:
    print(f"You've won!")
    print(f"You      : {logos_choices[user_input]}")
    print(f"Computer : {logos_choices[computer_choice]}")
elif user_input == 2 and computer_choice == 1:
    print(f"You've won!")
    print(f"You      : {logos_choices[user_input]}")
    print(f"Computer : {logos_choices[computer_choice]}")
else:
    print("You've lost")
    print(f"You      : {logos_choices[user_input]}")
    print(f"Computer : {logos_choices[computer_choice]}")

# end
