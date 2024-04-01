# print the average height from a list of students height

student_heights = (input("Enter student heights separated by a comma: ").split(", "))
total_height = 0
number_of_students = 0
for height in student_heights:
    total_height += float(height)
    number_of_students += 1
print(f"The average height for these {len(student_heights)} student ts is {round(total_height/number_of_students, 2)}")