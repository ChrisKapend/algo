age = input("What is your age? ")
years_left_till_90 = 90 - int(age)
days_left = years_left_till_90 * 365
weeks_left = years_left_till_90 * 52
months_left = years_left_till_90 * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left till you are 90")

