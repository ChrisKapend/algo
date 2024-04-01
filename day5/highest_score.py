# from a list of scores chose the highest

scores = input("Enter scores separated by a space: ").split()
highest = 0
for score in scores:
    if int(score) > highest:
        highest = int(score)
        print(highest)
print(f"The highest score is {highest}")