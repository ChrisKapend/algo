def scoring_criterion(grade):
    if grade > 90:
        return "Outstanding"
    if grade > 80:
        return "Exceeds Expectations"
    if grade > 71:
        return "Acceptable"
    else:
        return "Fail"


students_scores = {
    "Jane": 91,
    "Eliott": 92,
    "Joy": 93,
    "Josiane": 79,
    "Chris": 78,
    "Hervé": 71,
}

students_grades = {}
for student in students_scores:
    students_grades[student] = scoring_criterion(students_scores[student])

print(students_grades)
