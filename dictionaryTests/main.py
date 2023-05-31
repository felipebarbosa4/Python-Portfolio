student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


student_grades = {}

for add_grades in student_scores:
    student_grades[add_grades] = student_scores[add_grades]
    if student_grades[add_grades] > 90:
        student_grades[add_grades] = "Outstanding"
    elif student_grades[add_grades] > 80:
        student_grades[add_grades] = "Exceeds Expectations"
    elif student_grades[add_grades] > 70:
        student_grades[add_grades] = "Acceptable"
    else:
        student_grades[add_grades] = "Fail"

print(student_grades)