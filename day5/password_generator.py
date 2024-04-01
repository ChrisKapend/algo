# imports
import random
import string

# Declarations
letters = string.ascii_letters
digits = string.digits
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# Gathering user input
print(f"Welcome to the password generator")
n_letters = int(input("How many letters would you want you in your password? "))
n_digits = int(input("How many digits would you want in your password? "))
n_symbols = int(input("How many symbols would you want in your password? "))

# Selecting random characters
# letters_placeholder = random.choices(letters, k=n_letters)
# digits_placeholder = random.choices(digits, k=n_digits)
# symbols_placeholder = random.choices(symbols, k=n_symbols)

letters_placeholder = ""
digits_placeholder = ""
symbols_placeholder = ""

for i in range(n_letters):
    letters_placeholder += letters[random.randint(0, len(letters) - 1)]
for i in range(n_digits):
    digits_placeholder += digits[random.randint(0, len(digits) - 1)]
for i in range(n_symbols):
    symbols_placeholder += symbols[random.randint(0, len(symbols) -1)]

password_table = letters_placeholder + digits_placeholder + symbols_placeholder

print(f"The password table is {password_table} and the password is below \n")

# Shuffling the password so that items positions aren't kept the same

password_table = random.sample(password_table, k=len(password_table))

# Password Generation
password = ""
for n in range(0, len(password_table)):
    password += password_table[n]


print(f"{password}\n")