height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
height = height / 100
bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, your have normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi}, your are overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, your are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")
