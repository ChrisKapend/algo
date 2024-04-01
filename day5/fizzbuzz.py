# Print each number from 1 to 100 in turn
# when a number is divisible by 3 print instead 'Fizz'
# when a number is divisible by 5 print instead 'Buzz'
# if the number is divisible by both 3 and 5 print FizzBuzz
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)