student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key in student_scores:
  point = student_scores[key]
  if point >= 91:
    student_grades[key] = "Outstanding"
  elif point >= 81:
    student_grades[key] = "Exceeds Expectations"
  elif point >= 71:
    student_grades[key] = "Acceptable"
  else:
    student_grades[key] = "Fail"

print(student_grades)
