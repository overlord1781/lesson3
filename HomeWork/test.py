# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
from typing import Counter


students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
list_name = []
for student in students:
    for name in student.values():
        list_name.append(name)
list_name = Counter(list_name)
print(type(list_name))