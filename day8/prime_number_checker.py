def is_number_prime(number):
    is_not_prime = False
    divisors = ""
    if number <= 1:
        print(f"Can't prime numbers less than 1")
    elif number == 2:
        print(f"{number} is a prime number")
    else:
        for i in range(2, number):
            if number % i == 0:
                is_not_prime = True
                divisors += f"{i} "
        if is_not_prime:
            print(f"{number} is is not a prime number\n")
            print(f"Because it can be divided by \n{divisors}\n")
        else:
            print(f"{number} is a prime number")


n = int(input("Enter a number: "))
is_number_prime(number=n)