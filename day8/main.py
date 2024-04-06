# Simple Function
def great():
    print("Hello Joy")
    print("How do you do?")
    print("Isn't the weather nice today?\n")


great()


# Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?\n")


# greet_with_name("Jane")
# greet_with_name("Eliott")
# greet_with_name("Josiane")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Isn't the weather nice in {location}?\n")


# Function call with positional params
greet_with('Chris', "New York")
greet_with("Jane", "Montreal")

# Call function with keyword params
greet_with(location="Lubumbashi", name="Joy Kapend")