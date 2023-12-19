DATA_FILES_BASE_PATH = './data'

def load_data():
  with open(f'{DATA_FILES_BASE_PATH}/uczniowie.txt', 'r') as file:
    students_data = file.read()
  with open(f'{DATA_FILES_BASE_PATH}/oceny.txt', 'r') as file:
    grades_data = file.read()
  with open(f'{DATA_FILES_BASE_PATH}/przedmioty.txt', 'r') as file:
    classes_data = file.read()
  return (students_data, grades_data, classes_data)
