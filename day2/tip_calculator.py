print("Welcome to the Tip Calculator")
total_bill = float(input("What is your total bill? $"))
tip_percent = float(input("what percentage tip would you like to give %"))
number_of_people = int(input("How many people to split the bill? "))
total = total_bill * (1 + (tip_percent / 100))

print(f"The total bill is ${"{:.2f}".format(total)}")
print(f"Each person should pay: ${round(total/number_of_people,2)}")
