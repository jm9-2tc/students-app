from models import Table
from utils import get_student_with_best_average_score

DATA_FILES_BASE_PATH = './data'

def load_data():
  with open(f'{DATA_FILES_BASE_PATH}/uczniowie.txt', 'r') as file:
    students_data = file.read()
  with open(f'{DATA_FILES_BASE_PATH}/oceny.txt', 'r') as file:
    grades_data = file.read()
  with open(f'{DATA_FILES_BASE_PATH}/przedmioty.txt', 'r') as file:
    classes_data = file.read()
  return (students_data, grades_data, classes_data)

students_raw_data, grades_raw_data, classes_raw_data = load_data()

students_table = Table.from_csv(students_raw_data)
grades_table = Table.from_csv(grades_raw_data)
classes_table = Table.from_csv(classes_raw_data)

print(get_student_with_best_average_score(students_table, grades_table, classes_table))
