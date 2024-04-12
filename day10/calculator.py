# Calculator
# Add
def add(num1, num2):
    return num1 + num2


# Subtract
def subtract(num1, num2):
    return num1 - num2


# Multiply
def multiply(num1, num2):
    return num1 * num2


# Divide
def divide(num1, num2):
    return num1 / num2


def calculator():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    run = "y"
    number1 = float(input("Enter first number: "))
    while run == "y":
        number2 = float(input("Enter the next number: "))
        for symbol in operations:
            print(symbol)
        operation_symbol = input("What operation would you like to do: ")
        user_operation = operations[operation_symbol]
        result = user_operation(number1, number2)
        print(f"{number1} {operation_symbol} {number2} = {result}")
        run = input(f"Type 'y' to continue calculating with {result}, s to start over or n to exit: ").lower()
        if run == "y":
            number1 = result
        else:
            calculator()
    print(f"Thanks for using the calculator, bye")


"""
number1 = float(input("Enter first number: "))
while run == "y":
    number2 = float(input("Enter the next: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("What operation would you like to do: ")
    user_operation = operations[operation_symbol]
    result = user_operation(number1, number2)
    print(f"{number1} {operation_symbol} {number2} = {result}")
    carry_on = "y"
    while carry_on == "y":
        carry_on = input(f"Type 'y' to continue calculating with {result}, or n to exit: ").lower()
        if carry_on == "y":
            next_number = float(input("Enter next number: "))
            operation_symbol = input("What operation would you like to do: ")
            user_operation = operations[operation_symbol]
            result1 = result
            result = user_operation(next_number, result)
            print(f"{result1} {operation_symbol} {next_number} = {result}")
        else:
            run = input(f"Would you like to continue calculating y/n: ").lower()"""
calculator()
