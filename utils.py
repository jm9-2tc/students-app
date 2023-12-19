from models import Table

def get_student_with_best_average_score(students: Table, grades: Table, classes: Table):
  classes_ids = [record['IDprzedmiotu'] for record in classes.records]

  best_student = None
  best_average_score = 0.0

  for student in students.records:
    student_grades = list(filter(lambda record: record['IDucznia'] == student['IDucznia'], grades.records))
    grades_per_class = [list(map(lambda record: record['Ocena'], list(filter(lambda record: record['IDprzedmiotu'] == class_id, student_grades)))) for class_id in classes_ids]
    average_score_per_class = [sum(grades) / len(grades) for grades in grades_per_class if len(grades) > 0]

    if len(average_score_per_class) > 0:
      average_score = sum(average_score_per_class) / len(average_score_per_class)
      if average_score > best_average_score:
        best_average_score = average_score
        best_student = f"{student['imie']} {student['nazwisko']}"

  return {
      "best_student": best_student,
      "best_average_score": best_average_score
  }